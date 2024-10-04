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

## Extract plaintext files from aap-docs repo

```commandline
 ./scripts/get_aap_plaintext_docs.sh 2.5
```

## Build image
```commandline
make build-image-aap
```

## Push image to quay.io
_(It is pushed to Tami's account temporarily)_
```commandline
podman login quay.io
podman push aap-rag-content quay.io/ttakamiy/aap-rag-content
```


