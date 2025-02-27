# aap-rag-content

## Overview

This repository was created based on the codes found in the
[openshift/lighspeed-rag-content](https://github.com/openshift/lightspeed-rag-content)
for building a RAG (Retrieval-Augmented Generation)
vector database, which is used with the Ansible Automation
Platform (AAP) chatbot from the documentation sources stored 
in the [ansible/aap-docs](https://github.com/ansible/aap-docs)
repository.

## Prerequisites

- [PDM](https://pdm-project.org/en/latest/)
- [Asciidoctor](https://asciidoctor.org/)

## Setup

```commandline
make install-tools
make install-deps
make install-deps-test
```

## Build aap-rag-content image manually

Currently, aap-rag-content images are built with Gitlab.cee
aap-rag-content repository, which references this repository
as a git submodule. However, If you need to build an image manually
from this repository, use the following steps.

### Extract Markdown files from Mimir archive

1. Obtain the access to the Mimir repository and clone the repository.
2. Create the `./mimir` folder in the project root.
3. Copy `mimir-extract-latest.tgz.enc` file to `./mimir`
4. Run `./scripts/mimir-parser.py`, which will extract markdown
   files in `./aap-product-docs-plaintext` folder.

    ```commandline
     ./scripts/mimir-parser.py
    ```

### Build image
```commandline
make build-image-aap
```

### Push image to quay.io
```commandline
podman login quay.io
podman push aap-rag-content quay.io/ansible/aap-rag-content
```

## Experiment Postgres (PGVector) Vector Store

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


