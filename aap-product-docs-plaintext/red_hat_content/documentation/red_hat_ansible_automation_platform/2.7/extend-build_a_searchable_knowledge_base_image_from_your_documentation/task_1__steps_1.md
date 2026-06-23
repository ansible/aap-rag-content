# Build a searchable knowledge base image from your documentation
## Create a vector database from your documentation
### Procedure

1.  Create a directory for your knowledge sources and outputs:


```
mkdir -p knowledge-sources/my-org-docs
mkdir -p output/vector_db
cp -r /path/to/your/prepared/files/* knowledge-sources/my-org-docs/
```

2.  Optional: Configure a metadata processor to add URL references (key="url") to indexed chunks. Use one of the following options:
1.  Include the [YAML frontmatter](https://github.com/lightspeed-core/rag-content?tab=readme-ov-file#yaml-frontmatter-support) in the sources.
2.  Write a custom data processor, as shown in the following example:


```
# custom_processor.py
def add_metadata(chunk, source_file):
chunk.metadata['url'] = f"https://docs.example.com/{source_file}"
chunk.metadata['title'] = source_file.replace('-', ' ').title()
return chunk
```

3.  Run the `rag-content` tool to generate the vector database:


```
podman run --rm \
-u 0 \
-v "$(pwd)/knowledge-sources/my-org-docs:/input:Z" \
-v "$(pwd)/output:/output:Z" \
registry.redhat.io/lightspeed-core/rag-tool-rhel9:v0.5-latest \
python /rag-content/scripts/generate_embeddings.py \
-f /input \
-o /output/vector_db \
-i my-docs-index \
--exclude-model \
--output-image /output/rag-content-output-latest.tar \
--image-name rag-content-output \
--image-tag latest
```

### Example

Replace the values in the command above with your own paths and names. Use the table below as a reference.

| Parameter                               | Description          | What to provide                                                                                                                                                            |
| --------------------------------------- | -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `$(pwd)/knowledge-sources/my-org-docs`  | Source data path     | The full path to the folder containing your raw documents (PDFs, TXT, etc.).                                                                                               |
| `$(pwd)/output`                         | Local output path    | <br>The folder on your computer where you want the finished database to be saved.<br>**Note**: The HASH may differ depending on which container image was used previously. |
| `/output/vector_db`                     | Database folder Name | <br>The name of the subdirectory created inside your output folder to store the database.                                                                                  |
| <br>`my-docs-index`                     | Search index name    | A unique, descriptive name for this specific collection of data.                                                                                                           |
| `/output/rag-content-output-latest.tar` | Export filename      | The name of the compressed file (.tar) that contains your portable database.                                                                                               |
| `rag-content-output`                    | Internal image Name  | The name assigned to the container is used if you load this data into another system later.                                                                                |
| `latest`                                | Version tag          | A version label (for example, v1.0 or April-2026) to track your database updates.                                                                                          |


Note:

If you encounter the following error message, you can ignore it, as it does not affect vector database creation:

`AttributeError: 'SqliteKVStoreImpl' object has no attribute 'close'`
