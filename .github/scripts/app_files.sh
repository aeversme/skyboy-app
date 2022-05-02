#!/usr/bin/env bash

sed "s|TOKEN_PLACEHOLDER|$TOKEN|g" ./app/.streamlit/config.template > ./app/.streamlit/config.toml
sed "s|BUCKET_NAME|$BUCKET_NAME|g" ./app/src/modules/demo.template > ./app/src/modules/demo.py
