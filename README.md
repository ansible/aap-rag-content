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

For generating vector DB, we use the `aap_rag_content` Python package
located in the `src/` directory, which provides document processing and
vector database generation capabilities. The [custom_processor_aap.py script](./scripts/custom_processor_aap.py)
uses this package to process AAP documentation and build the vector database.


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

## Development Setup

Before running tests or working with the codebase, set up your development environment:

```commandline
make setup
```

This command will:
- Create a virtual environment (`.venv/`)
- Install all project dependencies
- Install development tools (pytest, black, mypy, ruff, etc.)

The project uses [uv](https://github.com/astral-sh/uv) for dependency management, which provides fast and reliable package installation.

## Running Unit Tests

To run the unit tests for the `aap_rag_content` package:

```commandline
make unit-test
```

This will execute all tests in the `tests/` directory using pytest with verbose output.
The test suite includes tests for:
- Metadata processing
- Document processing
- Vector database generation
- Utility functions

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
