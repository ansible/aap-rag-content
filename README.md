# aap-rag-content

## Overview

This repository contains files
for building a RAG (Retrieval-Augmented Generation)
vector DB, which is used with the Ansible Lightspeed
Intelligent Assistant (ALIA).

The source documents saved here were
extracted from the document archive built for Red Hat Offline
Knowledge Portal (OKP), which provides off-line access to 
Red Hat product documentation.
Copies of markdown files are stored in this repository.

For generating vector DB, we are using scripts provided by
the [lightspeed-core/rag-content](https://github.com/lightspeed-core/rag-content/)
repository with our own [custom_processor-aap.py script](./scripts/custom_processor-aap.py).
See [the README.md file of lightspeed-core/rag-content](https://github.com/lightspeed-core/rag-content/blob/main/README.md)
for technical details.


## Input files for Vector DBs

Input files that are used as the source of vector DBs are stored
in the following directories:

- `/red_hat_content` This directory stores the Markdown files extracted from
the Mimir archive.
- `/aap-product-docs-plaintext` This directory has Markdown files and
their metadata files that are generated from the raw files
under `/red_hat_content`. Metadata files are stored in the `.metadata`
subdirectory with the same file name as its source and `.json` file
extension.
- `/additional_docs` This directory contains additional Markdown files that are
used as the input for vector DB.  Its `.metadata` subdirectory contains
metadata JSON files.

## Build a container image

Following command builds a container image, which includes the generated vector DB.
```commandline
make build-image-aap
```

## Push a container image to quay.io
```commandline
podman login quay.io
podman push aap-rag-content quay.io/ansible/aap-rag-content
```

