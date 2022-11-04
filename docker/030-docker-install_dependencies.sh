#!/bin/bash

# -----------------------------------------------------------------
#
# Ejecuta una sesión bash en el Dev Container para usarla en
# terminales externos a VSCode.
#
# -----------------------------------------------------------------
docker exec -ti \
  -u 0:0 \
  -w /workspaces/ \
  -e PYTHONPATH=$PYTHONPATH:/workspaces/libraries_python/cli_helpers/src \
  priceless_hoover \
  /bin/bash -c "./pip_install.sh"
