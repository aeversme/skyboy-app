#!/usr/bin/env bash

echo "credentials \"app.terraform.io\" {" > .terraformrc
echo "  token = \"$TOKEN\"" >> .terraformrc
echo "}" >> .terraformrc
mv .terraformrc $HOME/.terraformrc
export TF_CLI_CONFIG_FILE="$HOME/.terraformrc"