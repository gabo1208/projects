#!/bin/bash

set -e

function install_certmanager() {
kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.12.3/cert-manager.yaml
kubectl wait --for=condition=Established --all crd
kubectl wait --for=condition=Available -n cert-manager --all deployments
}

function install_kserving() {
ko apply --selector knative.dev/crd-install=true -Rf config/core/
kubectl wait --for=condition=Established --all crd

ko apply -Rf config/core/

}

function deploy_kingress() {
kubectl apply -f ./third_party/kourier-latest/kourier.yaml

kubectl patch configmap/config-network \
  -n knative-serving \
  --type merge \
  -p '{"data":{"ingress.class":"kourier.ingress.networking.knative.dev"}}'
}

export KO_DOCKER_REPO='kind.local'

install_certmanager
install_kserving
deploy_kingress
kubectl apply -f https://github.com/knative-extensions/net-certmanager/releases/download/knative-v1.12.1/net-certmanager.yaml
kubectl apply -f ./test/config/autotls/certmanager/selfsigned

kubectl patch configmap/config-network \
  -n knative-serving \
  --type merge \
  -p '{"data":{"auto-tls": "Enabled", "http-protocol": "Redirected"}}'

kubectl patch configmap/config-domain \
  -n knative-serving \
  --type merge \
  -p '{"data":{"exddampleexampleexampleexampleexampleexampleexampleexamplee.com": ""}}'

ko delete -f config/post-install/default-domain.yaml --ignore-not-found
ko apply -f config/post-install/default-domain.yaml
