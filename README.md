# aap-rag-content

## Overview

This repository was originally created based on the codes found in the
[openshift/lighspeed-rag-content](https://github.com/openshift/lightspeed-rag-content)
for building a RAG (Retrieval-Augmented Generation)
vector database, which is used with the Ansible Automation
Platform (AAP) Chatbot.

Initially, the Asciidoc files stored in the [ansible/aap-docs](https://github.com/ansible/aap-docs)
repository are used as the source documents and later it was changed
to use the markdown files extracted from the "Mimir" archive,
which provides off-line access to Red Hat product documentation.
The copy of markdown files are stored in this repository.

There are two versions of AAP Chatbot: [road-core/service](https://github.com/road-core/service)
based and [llama-stack](https://github.com/meta-llama/llama-stack)
based implementations. Each implementation uses a different format for
the vector DB and this repo provides two scripts for generating
vector DBs.

For generating embeddings, the same embedding model (`sentence-transformers/all-mpnet-base-v2`)
is used for both vector DB formats. Some files of the embedding model
are stored in this repository under the `/embeddings_model`, but
the [model.safetensors](https://huggingface.co/sentence-transformers/all-mpnet-base-v2/blob/main/model.safetensors)
is not included for its size (437,971,872 bytes).

## Prerequisites

After cloning the repository to your local directory,
install [uv](https://docs.astral.sh/uv/) and create & activate venv with the
following commands:

```commandline
uv venv
source .venv/bin/activate
```

## Setup

```commandline
make install-deps
```

## Input files for Vector DBs

Input files that are used as the source of vector DBs are stored
in the following directories:

- `/red_hat_content` This directory stores the Markdown files extracted from
the Mimir archive.
- `/aap-product-docs-plaintext` This directory has Markdown files and
their metadata files that are generated from the raw files
under `/red_hat_content`. Metadata are stored in the `.metadata`
subdirectory with the same file name as its source and `.json` file
extension.
- `/additional_docs` This directory contains additional Markdown files that are
used as the input for vector DB.  Its `.metadata` subdirectory contains
metadata JSON files.

### Build a vector DB for road-core/service
```commandline
make build-road-core-db
```
The generated DB is found in `/vector_db/aap_product_docs/2.5`

### Build a vector DB for llama-stack
```commandline
make build-llama-stack-db
```
The generated DB is found in `/llama_stack_vector_db/aap_product_docs/2.5`

### Build a container image
```commandline
make build-image-aap
```

### Push a container image to quay.io
```commandline
podman login quay.io
podman push aap-rag-content quay.io/ansible/aap-rag-content
```

### How to update product documentation files using Mimir archive
1. Remove `/red_hat_content` and `/aap-product-docs-plaintext` directories:
   ```commandline
   rm -rf ./red_hat_content ./aap-product-docs-plaintext
   ```
2. Create `/mimir` directory in the project root and copy `mimir-extract-latest.tgz.enc` file
   there.
   ```commandline
   mkdir -p ./mimir
   cp ~/git/customer-platform/mimir-extracted-content-for-ai/mimir-extract-latest.tgz.enc mimir
   ```
3. Run `mimir-parser.py`
   ```commandline
   uv run python3 ./scripts/mimir-parser.py
   ```
4. Check in changes if any differnces from the files in the repo were found.

#### How to include Knowlege Base articles

If you want to include Knowledge Base articles, which are stored
under the `red_hat_content/solutions` folder in the Mimir archive,
run the `mimir-parser.py` with the `--add-kb-articles` option, i.e.,
```commandline
uv run python3 ./scripts/mimir-parser.py --add-kb-articles
```
The script extracts only the articles whose `[products]` metadata
contains `Red Hat Ansible Automation Platform`. The metadata is
defined in the beginning of each Knowledge Base markdown file.


## Experiment Postgres (PGVector) Vector Store

**Note: as of today (2025-07-01) This instruction for PGVector is for road-core/service based implementation only**

By default, Faiss Vector Store is used for saving embeddings and
the result is included in container images. You can also use
Postgresql database as the vector store with its PGVector extension.

### Start Postgres with PGVector extension
```commandline
make start-postgres-debug
```
The `data` directory of Postgres is created under `./postgresql/data`.

### Generate embeddings
```commandline
make generate-embeddings-postgres
```
The result is saved in the `data_aap_product_docs_2_5` table.
```commandline
$ podman exec -it pgvector bash
root@7894ab5c94e2:/# psql -U postgres
psql (16.4 (Debian 16.4-1.pgdg120+2))
Type "help" for help.

postgres=# \dt
                   List of relations
 Schema |           Name            | Type  |  Owner
--------+---------------------------+-------+----------
 public | data_aap_product_docs_2_5 | table | postgres
(1 row)

postgres=#
```
