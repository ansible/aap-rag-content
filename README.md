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

## Build RAG container image
### Extract plaintext files from aap-docs repo

```commandline
 ./scripts/get_aap_plaintext_docs.sh 2.5
```

### Build image
```commandline
make build-image-aap
```

### Push image to quay.io
_(It is pushed to Tami's account temporarily)_
```commandline
podman login quay.io
podman push aap-rag-content quay.io/ttakamiy/aap-rag-content
```

## pgvector (Postgres vector extension) support

Instead of building an image of RAG data using `FaissVectorStore`, you
can store the vector data in a Postgresql DB with 
[the pgvector extension](https://github.com/pgvector/pgvector).

### Extract plaintext files from aap-docs repo

This is the same procedure as the one that is required for building an image.
```commandline
 ./scripts/get_aap_plaintext_docs.sh 2.5
```

### Download embedding model
In building an image, this step is invoked from container file. For using
pgvector, you need to run the script using `Makefile`:
```commandline
make download-embeddings-model
```

### Start Postgres on localhost
```commandline
make start-postgresql
```

### Generate embeddings and store results
```commandline
make generate-embeddings-aap
```

