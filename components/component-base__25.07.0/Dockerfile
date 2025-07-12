FROM ubuntu:noble AS base

RUN apt-get update && \
    apt-get install -y \
    build-essential \
    git \
    curl \
    wget \
    ca-certificates \
    software-properties-common

RUN mkdir -p /products

ENV PRODUCT_DIR=/products
