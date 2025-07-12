#!/usr/bin/env bash

bash ./Miniconda3-25.07.0-Linux-0.sh -b -p "${USER_OPT}/miniconda3"
conda init
conda config --set auto_update_conda false
conda config --set changeps1 false
conda config --set show_channel_urls true

bash ./install-uv.sh
