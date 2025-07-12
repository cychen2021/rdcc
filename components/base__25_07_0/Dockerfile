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

RUN sudo mkdir /extra && \
    sudo chown vscode:vscode /extra

ENV USER_OPT="/extra"
ENV SHEL=/usr/bin/zsh
