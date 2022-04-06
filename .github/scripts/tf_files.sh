#!/usr/bin/env bash

sed "s/WORKSPACE_NAME/$WORKSPACE/g" ./terraform/backends.template > ./terraform/backends.tf
cat ./terraform/backends.tf
sed "s/IMAGE_URI/$IMAGE/g" ./terraform/containers/task-definitions/skyboy.template > ./terraform/containers/task-definitions/skyboy.json
cat ./terraform/containers/task-definitions/skyboy.json
cat ./terraform/loadbalancing/$LISTENERS >> ./terraform/loadbalancing/main.template
mv ./terraform/loadbalancing/main.template ./terraform/loadbalancing/main.tf
cat ./terraform/loadbalancing/main.tf