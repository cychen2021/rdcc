FROM mcr.microsoft.com/devcontainers/base:noble

ENV USER=vscode
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
ENV RDCC_PRODUCT_DIR="/products"

RUN sudo mkdir ${USER_OPT} && \
    sudo chown vscode:vscode ${USER_OPT}
RUN sudo mkdir ${BUILD_DIR} && \
    sudo chown vscode:vscode ${BUILD_DIR}

WORKDIR ${BUILD_DIR}

RUN case $(uname -m) in \
    x86_64) \
        wget -O "Miniconda3.sh" "https://repo.anaconda.com/miniconda/Miniconda3-py313_25.5.1-0-Linux-x86_64.sh" \
        ;; \
    aarch64) \
        wget -O "Miniconda3.sh" "https://repo.anaconda.com/miniconda/Miniconda3-py313_25.5.1-0-Linux-aarch64.sh" \
        ;; \
    *) \
        echo "Unsupported architecture: $(uname -m)" \
        exit 1 \
        ;; \
    esac

RUN bash ./Miniconda3.sh -b -p "${USER_OPT}/miniconda3" && \
    "${USER_OPT}/miniconda3/bin/conda" init && \
    "${USER_OPT}/miniconda3/bin/conda" config --set auto_update_conda false && \
    "${USER_OPT}/miniconda3/bin/conda" config --set changeps1 false && \
    "${USER_OPT}/miniconda3/bin/conda" config --set show_channel_urls true

RUN sudo rm -rvf "${BUILD_DIR}/*"

