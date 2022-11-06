#!/bin/bash

# -----------------------------------------------------------------
#
# Ejecuta una sesión bash en el Dev Container para usarla en
# terminales externos a VSCode.
#
# -----------------------------------------------------------------
docker exec -ti \
  -u 1000:1000 \
  -w /workspaces/libraries_python/cli_helpers/src \
  -e PYTHONPATH=$PYTHONPATH:/workspaces/cli_helpers/src \
  confident_poincare \
  /bin/bash
