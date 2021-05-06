#!/usr/bin/env bash

# generate .env file
_generate_config_json() {
  cat > /etc/aerpawNodeAgent.json << EOF
{
  "port": "${SERVICE_PORT}",
  "containerStore": "${CONTAINER_STORE}"
}
EOF
}

# main
_generate_config_json
cat /etc/aerpawNodeAgent.json
PATH=$(pwd):$PATH
./aerpawNodeAgent.py

exit 0;