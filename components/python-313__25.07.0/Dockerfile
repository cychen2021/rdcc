FROM ghcr.io/cychen2021/rdcc_component-base:25.07.0

RUN case $(uname -m) in \
    x86_64) \
        wget -O "${PRODUCT_DIR}/Miniconda-py313_25.5.1-0.sh" "https://repo.anaconda.com/miniconda/Miniconda3-py313_25.5.1-0-Linux-x86_64.sh" \
        ;; \
    aarch64) \
        wget -O "${PRODUCT_DIR}/Miniconda-py313_25.5.1-0.sh" "https://repo.anaconda.com/miniconda/Miniconda3-py313_25.5.1-0-Linux-aarch64.sh" \
        ;; \
    *) \
        echo "Unsupported architecture: $(uname -m)" \
        exit 1 \
        ;; \
    esac

COPY install.sh "${PRODUCT_DIR}/install.sh"
COPY instal-uv.sh "${PRODUCT_DIR}/instal-uv.sh"
