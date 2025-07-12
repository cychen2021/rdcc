FROM mcr.microsoft.com/devcontainers/base:noble

RUN sudo apt-get update && \
    sudo apt-get install -y \
    build-essential \
    git \
    curl \
    wget \
    ca-certificates \
    software-properties-common

RUN sudo mkdir /extra && \
    sudo chown vscode:vscode /extra

ENV USER_OPT="/extra"
