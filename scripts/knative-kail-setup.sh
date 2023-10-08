#!/bin/bash

set -o errexit
set -o pipefail
set -x

readonly K8S_VERSION=v1.25.11
readonly KNATIVE_VERSION=v1.11.1
readonly CONTOUR_VERSION=v1.11.1
readonly KN_VERSION=v1.11.0
readonly KIND_IMAGE_SHA=sha256:227fa11ce74ea76a0474eeefb84cb75d8dad1b08638371ecf0e86259b35be0c8

SCRATCH=$(mktemp -d)

function kn {
  docker run \
    -v $SCRATCH/kubeconfig:/kubeconfig \
    -e KUBECONFIG=/kubeconfig \
    --network kind \
    gcr.io/knative-releases/knative.dev/client/cmd/kn:$KN_VERSION "$@"
}


cat > $SCRATCH/config <<EOF
apiVersion: kind.x-k8s.io/v1alpha4
kind: Cluster
# This is needed in order to support projected volumes with service account tokens.
# See: https://kubernetes.slack.com/archives/CEKK1KTN2/p1600268272383600
kubeadmConfigPatches:
- |
  apiVersion: kubeadm.k8s.io/v1beta2
  kind: ClusterConfiguration
  metadata:
    name: config
  apiServer:
    extraArgs:
      "service-account-issuer": "kubernetes.default.svc"
      "service-account-signing-key-file": "/etc/kubernetes/pki/sa.key"
nodes:
- role: control-plane
  image: kindest/node:${K8S_VERSION}@${KIND_IMAGE_SHA}
- role: worker
  image: kindest/node:${K8S_VERSION}@${KIND_IMAGE_SHA}
EOF


cat > $SCRATCH/limit.yaml <<EOF
apiVersion: v1
kind: LimitRange
metadata:
  name: limit
spec:
spec:
  limits:
  - default:
      cpu: 100m
    defaultRequest:
      cpu: 100m
    max:
      cpu: "8"
    min:
      cpu: 10m
    type: Container
EOF

if [ -z ${SKIP_SETUP} ]; then
  kind delete cluster --name debug-knative
  kind create cluster --config $SCRATCH/config --name debug-knative

  kubectl apply -f https://github.com/knative/serving/releases/download/knative-${KNATIVE_VERSION}/serving-crds.yaml
  kubectl apply -f https://github.com/knative/serving/releases/download/knative-${KNATIVE_VERSION}/serving-core.yaml

  curl -L https://github.com/knative/net-contour/releases/download/knative-${CONTOUR_VERSION}/contour.yaml | \
     sed 's/LoadBalancer/NodePort/g' | \
     sed 's/imagePullPolicy:/# DISABLED: imagePullPolicy:/g' | \
     kubectl apply -f -

  curl -L https://github.com/knative/net-contour/releases/download/knative-${CONTOUR_VERSION}/net-contour.yaml | \
     sed 's/LoadBalancer/NodePort/g' | \
     sed 's/imagePullPolicy:/# DISABLED: imagePullPolicy:/g' | \
     kubectl apply -f -

  kubectl patch configmap/config-network \
    --namespace knative-serving \
    --type merge \
    --patch '{"data":{"ingress.class":"contour.ingress.networking.knative.dev"}}'

  deployments=$(kubectl get deployments -n knative-serving -ojsonpath='{ .items[*].metadata.name }')
  for d in $deployments; do
    kubectl rollout restart deployments/$d -n knative-serving
  done

  sleep 2

  kubectl wait deployment --for=condition=Available -n contour-external -l '!job-name' --timeout=120s
  kubectl wait deployment --for=condition=Available -n contour-internal -l '!job-name' --timeout=120s
  kubectl wait deployment --for=condition=Available -n knative-serving  --all --timeout=120s

  kubectl apply -f $SCRATCH/limit.yaml
fi


kind get kubeconfig --internal --name debug-knative > $SCRATCH/kubeconfig

NAME=test-$RANDOM

kail -n knative-serving --since 10m > $NAME.log &


watches=(kpa sks config rev rt ksvc deployment)

for t in ${watches[@]}; do
  kubectl get $t -o yaml -w > $NAME-$t.log &
done

kn service create $NAME --image gcr.io/knative-samples/helloworld-go --request cpu=200m --limit cpu=500m  --force

kill $(jobs -p)
