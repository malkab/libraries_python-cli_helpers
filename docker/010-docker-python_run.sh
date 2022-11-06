#/!bin/bash

# -----------------------------------------------------------------
#
# Runs an interactive Python container for development.
#
# -----------------------------------------------------------------
docker run -ti --rm \
    --name cli_helpers_python_dev \
    --hostname cli_helpers_python_dev \
    --user 1000:1000 \
    -e PYTHONPATH=$PYTHONPATH:$(pwd)/src \
    -v $(pwd)/../src:$(pwd)/../src \
    --workdir $(pwd)/../src \
    malkab/python:3.9-buster
