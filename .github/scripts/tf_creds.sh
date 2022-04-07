#!/usr/bin/env bash

echo "credentials \"app.terraform.io\" {" > tf.tfrc
echo "  token = \"$TOKEN\"" >> tf.tfrc
echo "}" >> tf.tfrc
mv tf.tfrc $HOME/tf.tfrc
export TF_CLI_CONFIG_FILE="$HOME/tf.tfrc"