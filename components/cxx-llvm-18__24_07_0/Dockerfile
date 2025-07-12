FROM ghcr.io/cychen2021/rdcc_component-base:25.07.0

COPY ./install.sh "${PRODUCT_DIR}/install.sh"
COPY ./install-llvm.sh "${PRODUCT_DIR}/install-llvm.sh"
RUN case $(uname -m) in \
    x86_64) \
        wget -O "${PRODUCT_DIR}/install-cmake.sh" "https://github.com/Kitware/CMake/releases/download/v4.1.0-rc1/cmake-4.1.0-rc1-linux-x86_64.sh" \
        ;; \
    aarch64) \
        wget -O "${PRODUCT_DIR}/install-cmake.sh" "https://github.com/Kitware/CMake/releases/download/v4.1.0-rc1/cmake-4.1.0-rc1-linux-aarch64.sh" \
        ;; \
    *) \
        echo "Unsupported architecture: $(uname -m)" && exit 1 \
        ;; \
    esac
