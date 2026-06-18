# Verify the vector database

Verify that you created a vector database of your documentation.

## Procedure

1.  Run the following command:


```
ls -lR output
```
The tool generates an image archive (.tar), which contains the vector database files and metadata. The following shows the structure of the output directory:

```
output
├── rag-content-output-latest.tar
└── vector_db
├── faiss_store.db
└── llama-stack.yaml
```
In the example above:
- `rag-content-output-latest.tar`is the generated image archive.
- `faiss_store.db`is the vector database file.
- `llama-stack.yaml`is the Llama Stack configuration file.

2.  Verify that you get the expected results by querying the generated vector database using the following command:


```
podman run --rm \
-u 0 \
-v "$(pwd)/output/vector_db:/vector_db:Z" \
registry.redhat.io/lightspeed-core/rag-tool-rhel9:v0.5-latest
\python scripts/query_rag.py \
-p /vector_db \
-x index \ -m embeddings_model \
-k 5 \
-q "Prerequisites for installation"
```
In the example above:
- `-k` tells the AI tool to find the five most relevant matches from your documentation.
- `-q` is your prompt; change the string according to your requirements.
The command displays the top five query results, along with the scores. Verify that the results are expected.
