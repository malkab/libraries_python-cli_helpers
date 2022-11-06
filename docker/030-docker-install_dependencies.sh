#!/bin/bash

# -----------------------------------------------------------------
#
# Ejecuta una sesión bash en el Dev Container para usarla en
# terminales externos a VSCode.
#
# -----------------------------------------------------------------
docker exec -ti \
  -u 0:0 \
  -w /workspaces/cli_helpers/ \
  -e PYTHONPATH=$PYTHONPATH:/workspaces/cli_helpers/src \
  priceless_hoover \
  /bin/bash -c "./pip_install.sh"
