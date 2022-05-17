#!/usr/bin/env bash

sed "s/WORKSPACE_NAME/$WORKSPACE/g" ./backends.template > ./backends.tf
sed "s|DD_EXTERNAL_ID|$DD_ID|g" ./iam/variables.template > ./iam/variables.tf
sed "s|IMAGE_URI|$IMAGE|g" ./containers/task-definitions/skyboy.template |
  sed "s|USER_ID_ARN|$USER_ID_ARN|g" |
  sed "s|DATADOG_KEY|$DD_API_KEY|g" |
  sed "s|USER_KEY_ARN|$USER_KEY_ARN|g" > ./containers/task-definitions/skyboy.json
cat ./loadbalancing/$LISTENERS >> ./loadbalancing/main.template
mv ./loadbalancing/main.template ./loadbalancing/main.tf