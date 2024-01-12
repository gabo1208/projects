#!/bin/bash

set -e
kubectl delete ksvc/bugsvc > /dev/null 2>&1 || true
kubectl delete ksvc/bugsvc2 > /dev/null 2>&1 || true

export CRASH=$(date -d "now 2 minutes" -u +'%H:%M')

echo "Will die: ${CRASH}"

kubectl apply -f - <<EOF
apiVersion: serving.knative.dev/v1
kind: Service
metadata:
  name: bugsvc
spec:
  template:
    spec:
      containers:
      - image: duglin/echo
        env:
          - name: CRASH
            value: "${CRASH}"
EOF
sleep 10
URL=$(kubectl get ksvc/bugsvc -o custom-columns=URL:.status.url --no-headers)

echo "Send curl just to make sure it works"
curl $URL

echo "Wait for it to scale to zero"
while kubectl get pods | grep bugsvc ; do
  sleep 10
done

echo "Sleep for 2 minutes just to make sure we're past the crash time"
sleep 120

echo "Create bugsvc2 so it fails immediately"
kubectl apply -f - <<EOF
apiVersion: serving.knative.dev/v1
kind: Service
metadata:
  name: bugsvc2
spec:
  template:
    spec:
      containers:
      - image: duglin/echo
        env:
          - name: CRASH
            value: "true"
EOF
echo "Now curl bugsvc again to force it to scale up to 1"
curl $URL &

echo "Pods should be failing, but bugsvc2 will eventually vanish"
kubectl get pods -w
