#!/bin/bash

kail -n knative-serving --since 10m > $NAME.log &

watches=(replicaset pods deployment)

for t in ${watches[@]}; do
  kubectl get $t -o yaml -w > $NAME-$t.log &
done

kn service create test-1 --image gcr.io/knative-samples/helloworld-go --request cpu=200m --limit cpu=500m  --force

kill $(jobs -p)