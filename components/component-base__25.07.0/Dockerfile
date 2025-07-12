FROM ubuntu:noble AS base

RUN sudo apt-get update && \
    sudo apt-get install -y \
    build-essential \
    git \
    curl \
    wget \
    ca-certificates \
    software-properties-common

RUN mkdir -p /products

ENV PRODUCT_DIR=/products
