#!/usr/bin/env bash

sed "s/WORKSPACE_NAME/$WORKSPACE/g" ./backends.template > ./backends.tf
sed "s|IMAGE_URI|$IMAGE|g" ./containers/task-definitions/skyboy.template > ./containers/task-definitions/skyboy.json
cat ./loadbalancing/$LISTENERS >> ./loadbalancing/main.template
mv ./loadbalancing/main.template ./loadbalancing/main.tf