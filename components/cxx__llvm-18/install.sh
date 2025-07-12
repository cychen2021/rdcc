#!/usr/bin/env bash

LLVM_VERSION=18
sudo bash ./install-llvm.sh "${LLVM_VERSION}"
LLVM_BINARIES=(
    # Core compilers
    "clang"
    "clang++"

    # Linkers
    "lld"
    "ld.lld"
    "ld64.lld"
    "wasm-ld"

    # Build tools
    "llvm-ar"
    "llvm-nm"
    "llvm-objcopy"
    "llvm-objdump"
    "llvm-readelf"
    "llvm-readobj"
    "llvm-ranlib"
    "llvm-size"
    "llvm-strings"
    "llvm-strip"
    "llvm-addr2line"

    # Configuration and analysis
    "llvm-config"
    "llvm-cov"
    "llvm-profdata"
    "llvm-symbolizer"
    "llvm-dwarfdump"

    # Optimization and analysis
    "opt"
    "llc"
    "lli"
    "llvm-as"
    "llvm-dis"
    "llvm-link"
    "llvm-extract"
    "llvm-bcanalyzer"

    # Debugging and profiling
    "lldb"
    "lldb-server"
    "llvm-pdbutil"
    "llvm-rtdyld"

    # Static analysis
    "clang-static-analyzer"
    "clang-tidy"
    "clang-format"
    "clang-check"
    "scan-build"
    "scan-view"

    # Cross-compilation and target-specific
    "llvm-mc"
    "llvm-mca"
    "llvm-ml"
    "llvm-mt"
    "llvm-rc"

    # Utilities
    "count"
    "FileCheck"
    "not"
    "yaml2obj"
    "obj2yaml"
    "clangd"
)

# Install the LLVM binaries
for binary in "${LLVM_BINARIES[@]}"; do
    sudo ln -s "/usr/bin/${binary}-${LLVM_VERSION}" "/usr/bin/${binary}" || true
done
