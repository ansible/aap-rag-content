# Define arguments for pgvector support
POSTGRES_USER ?= postgres
POSTGRES_PASSWORD ?= somesecret
POSTGRES_HOST ?= localhost
POSTGRES_PORT ?= 15432
POSTGRES_DATABASE ?= postgres
EMBEDDINGS_MODEL ?= sentence-transformers/all-mpnet-base-v2
RAG_CONTENT_IMAGE ?= quay.io/ansible/aap-rag-content:latest

OUTPUT_FOLDER ?= ./output
PG_DUMP_FILE ?= backup.tar

AAP_VERSION ?= 2.6
AAP_VERSION_STR := $(shell echo $(AAP_VERSION) | sed 's/\./_/g')

AAP_VERSION_2_5 ?= 2.5
AAP_VERSION_2_5_STR := $(shell echo $(AAP_VERSION_2_5) | sed 's/\./_/g')

uv-lock-check: ## Check that the uv.lock file is in a good shape
	uv lock --check

install-deps: uv-lock-check download-embeddings-model ## Install all required dependencies, according to uv.lock
	uv sync --frozen

download-embeddings-model:
	@echo "Download model.safetensors file and existing vector DBs..."
	podman run -d --rm --name rag-content $(RAG_CONTENT_IMAGE) sleep infinity
	podman cp rag-content:/rag/embeddings_model/model.safetensors ./embeddings_model
	rm -rf ./vector_db ./vector_db_save ./llama_stack_vector_db ./llama_stack_vector_db_save
	mkdir -p ./vector_db ./vector_db_save ./llama_stack_vector_db ./llama_stack_vector_db_save
	podman cp rag-content:/rag/embeddings_model/model.safetensors ./embeddings_model
	podman cp rag-content:/rag/vector_db .
	podman cp rag-content:/rag/llama_stack_vector_db .
	podman cp rag-content:/rag/vector_db ./vector_db_save
	podman cp rag-content:/rag/llama_stack_vector_db ./llama_stack_vector_db_save
	gzip -d ./llama_stack_vector_db/faiss_store.db.gz
	podman kill rag-content

export-deps: ## Check pyproject.toml for changes, update the lock file if needed, then sync.
	uv export --format requirements.txt -o requirements.txt

check-types: ## Checks type hints in sources
	mypy --explicit-package-bases --disallow-untyped-calls --disallow-untyped-defs --disallow-incomplete-defs scripts

print-llama-stack-deps: ## Print llama stack distribution dependencies
	llama stack build --config build.yaml --image-type venv --print-deps-only

format: ## Format the code into unified format
	black scripts
	ruff check scripts --fix --per-file-ignores=scripts/*:S101

verify: ## Verify the code using various linters
	black --check scripts
	ruff check scripts --per-file-ignores=scripts/*:S101

update-docs: ## Update the plaintext OCP docs in ocp-product-docs-plaintext/
	@set -e && for OCP_VERSION in $$(ls -1 ocp-product-docs-plaintext); do \
		scripts/get_ocp_plaintext_docs.sh $$OCP_VERSION; \
	done
	scripts/get_runbooks.sh

build-road-core-db:
	rm -rf ./vector_db
	mkdir -p ./vector_db
	uv run python3 scripts/generate_embeddings-aap.py \
  -f aap-product-docs-plaintext \
  -mn $(EMBEDDINGS_MODEL) \
  -o vector_db/aap_product_docs/$(AAP_VERSION_2_5) \
  -i aap-product-docs-$(AAP_VERSION_2_5_STR) \
  -v $(AAP_VERSION_2_5) \
  -c 200 \
  -l 10

build-llama-stack-db:
	rm -rf ./llama_stack_vector_db
	mkdir -p ./llama_stack_vector_db
	uv run python3 scripts/generate_embeddings-llama-stack.py \
  -f aap-product-docs-plaintext \
  -i aap-product-docs-$(AAP_VERSION_STR) \
  -c 200

build-llama-stack-db-extra-docs:
	rm -rf ./llama_stack_vector_db
	mkdir -p ./llama_stack_vector_db
	cp ./llama_stack_vector_db_save/llama_stack_vector_db/faiss_store.db.gz ./llama_stack_vector_db
	gzip -d ./llama_stack_vector_db/faiss_store.db.gz
	uv run python3 scripts/generate_embeddings-llama-stack.py \
  -f aap-product-docs-plaintext \
  -i aap-product-docs-$(AAP_VERSION_STR) \
  -c 200 \
  --skip-ping \
  --extra-docs-folder extra_docs

build-image: ## Build a rag-content container image.
	podman build -t rag-content .

build-image-aap: ## Build a rag-content container image.
	podman build -t aap-rag-content -f Containerfile-aap .

build-image-aap-llama-stack: ## Build a rag-content container image.
	podman build -t aap-rag-content -f Containerfile-aap --build-arg BUILD_ROAD_CORE_DB=false .

build-image-embeddings: ## Build an embeddings container image.
	podman build -t aap-rag-embeddings-image -f Containerfile-embeddings .

start-postgres: ## Start postgresql from the pgvector container image
	podman run -d --name pgvector --rm -e POSTGRES_PASSWORD=$(POSTGRES_PASSWORD) \
	 -p $(POSTGRES_PORT):5432 \
	 -v $(PWD)/postgresql/data:/var/lib/postgresql/data:Z \
	 pgvector/pgvector:pg16

start-postgres-debug: ## Start postgresql from the pgvector container image with debugging enabled
	mkdir -pv ./postgresql/data ./pg_dump
	podman run --name pgvector --rm -e POSTGRES_PASSWORD=$(POSTGRES_PASSWORD) \
	 -p $(POSTGRES_PORT):5432 \
	 -v ./postgresql/data:/var/lib/postgresql/data:Z \
	 -v ./pg_dump:/pg_dump:Z \
	 pgvector/pgvector:pg16 \
	 postgres -c log_statement=all -c log_destination=stderr

generate-embeddings-postgres: ## Generate embeddings for postgres vector store
	POSTGRES_USER=$(POSTGRES_USER) \
	POSTGRES_PASSWORD=$(POSTGRES_PASSWORD) \
	POSTGRES_HOST=$(POSTGRES_HOST) \
	POSTGRES_PORT=$(POSTGRES_PORT) \
	POSTGRES_DATABASE=$(POSTGRES_DATABASE) \
	python3 ./scripts/generate_embeddings-aap.py \
	 -f aap-product-docs-plaintext \
	 -mn $(EMBEDDINGS_MODEL) \
	 -o $(OUTPUT_FOLDER) \
	 -i aap-product-docs-$(subst .,_,$(AAP_VERSION_2_5)) \
	 -v ${AAP_VERSION_2_5} \
	 -c 200 \
	 -l 10 \
	 --vector-store-type postgres

dump-postgres: ## Dump database using pg_dump utility
	podman exec pgvector pg_dump -U $(POSTGRES_USER) -Ft $(POSTGRES_DATABASE) -f /pg_dump/$(PG_DUMP_FILE)

restore-postgres: ## Restore database using pg_restore utility
	podman exec pgvector pg_restore -U $(POSTGRES_USER) -d $(POSTGRES_DATABASE) /pg_dump/$(PG_DUMP_FILE)

help: ## Show this help screen
	@echo 'Usage: make <OPTIONS> ... <TARGETS>'
	@echo ''
	@echo 'Available targets are:'
	@echo ''
	@grep -E '^[ a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-25s\033[0m %s\n", $$1, $$2}'
	@echo ''
