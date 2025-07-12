FROM mcr.microsoft.com/devcontainers/base:noble

ARG USER=vscode
RUN adduser ${USER} sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

USER ${USER}

RUN sudo apt-get update && \
    sudo apt-get install -y \
    build-essential \
    git \
    curl \
    wget \
    ca-certificates \
    software-properties-common

ENV USER_OPT="/extra"
ENV SHELL=/usr/bin/zsh
ENV BUILD_DIR="/build"

RUN sudo mkdir ${USER_OPT} && \
    sudo chown vscode:vscode ${USER_OPT}
RUN sudo mkdir ${BUILD_DIR} && \
    sudo chown vscode:vscode ${BUILD_DIR}

WORKDIR ${BUILD_DIR}

RUN bash ./Miniconda3-25.07.0-Linux-0.sh -b -p "${USER_OPT}/miniconda3" && \
    conda init && \
    conda config --set auto_update_conda false && \
    conda config --set changeps1 false && \
    conda config --set show_channel_urls true

RUN sudo rm -rvf "${BUILD_DIR}/*"

