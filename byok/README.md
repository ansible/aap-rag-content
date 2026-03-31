## Introduction

This document describes how to generate a vector database from your own documentation files
for use with Ansible Lightspeed. The process uses the prebuilt `rag-tool` container images —
no access to the `rag-content` source repository is required.

The tool reads your Markdown (`.md`) files, generates embeddings, and packages the resulting
vector database into a **container image archive** (`.tar` file) that can be loaded into any
container runtime and pushed to a registry for deployment.

---

## Container Image Variants

Two image variants are available depending on your hardware:

| Variant | Base image | Use when |
|---------|-----------|----------|
| **CPU** | `registry.access.redhat.com/ubi9/ubi-minimal` | Standard hardware, no GPU available. Smaller image. |
| **GPU** | `nvcr.io/nvidia/cuda:12.9.1-devel-ubi9` | NVIDIA GPU available. Faster embedding generation. |

Both variants include the `lightspeed_rag_content` library and the default embedding model
(`sentence-transformers/all-mpnet-base-v2`) pre-downloaded at `/rag-content/embeddings_model`.

Obtain the appropriate image reference from your Red Hat registry or internal image repository.
In the commands below, replace `<rag-tool-image>:<tag>` with the actual image reference.

---

## Step 1 — Pull the Tool Image

**CPU variant (standard hardware):**

```bash
podman pull <rag-tool-image>:<tag>
```

**GPU variant (NVIDIA GPU required):**

```bash
podman pull <rag-tool-image-gpu>:<tag>
```

---

## Step 2 — Prepare Your Markdown Files

Put your `.md` files in a local directory, e.g.:

```
./ansible-collection-docs/
  README.md
  ...
```

---

## Step 3 — Create the Output Directory

```bash
mkdir -p ./output
```

---

## Step 4 — Run the Container

The tool generates a vector database from your documents and packages it into a container
image archive (`.tar` file).

**CPU variant:**

```bash
podman run --rm \
  --userns=keep-id \
  -v "$(pwd)/ansible-collection-docs:/input:Z" \
  -v "$(pwd)/output:/output:Z" \
  <rag-tool-image>:<tag> \
  python /rag-content/scripts/generate_embeddings.py \
    -f /input \
    -o /output/vector_db \
    -i my-docs-index \
    --output-image /output/rag-content-output-latest.tar \
    --image-name rag-content-output \
    --image-tag latest
```

**GPU variant** (add `--device nvidia.com/gpu=all` to pass through the GPU):

```bash
podman run --rm \
  --userns=keep-id \
  --device nvidia.com/gpu=all \
  -v "$(pwd)/ansible-collection-docs:/input:Z" \
  -v "$(pwd)/output:/output:Z" \
  <rag-tool-image-gpu>:<tag> \
  python /rag-content/scripts/generate_embeddings.py \
    -f /input \
    -o /output/vector_db \
    -i my-docs-index \
    --output-image /output/rag-content-output-latest.tar \
    --image-name rag-content-output \
    --image-tag latest
```

### Key Parameters

| Flag | Long form | Description |
|------|-----------|-------------|
| `-f` | `--folder` | Directory with input MD files (required) |
| `-o` | `--output` | Output directory for the vector DB (required) |
| `-i` | `--index`  | Index name for the vector store (required) |
| | `--output-image` | Path for the output `.tar` image archive (required) |
| | `--image-name` | Repository name embedded in the image archive (default: `rag-content-output`) |
| | `--image-tag` | Tag embedded in the image archive (default: `latest`) |
| | `--no-include-model` | Exclude the embedding model from the output image (included by default) |

> **Note:** `--userns=keep-id` is required so the container process runs as your host UID
> and can write to the output directory.

---

## Step 5 — Verify the Output

After the run, `./output` will contain:

```
output/
  vector_db/
    faiss_store.db.gz
    faiss_store.db.gz.sha256
    llama-stack.yaml
    provider_vector_db_id.ind
  rag-content-output-latest.tar
```

The `.tar` file is the container image archive holding the generated vector database
(and by default the embedding model). It can be loaded into any container runtime:

```bash
podman load < ./output/rag-content-output-latest.tar
```

Then push it to your registry for deployment:

```bash
podman push rag-content-output:latest <your-registry>/rag-content-output:latest
```

---

## Step 6 — Query the Generated Store (Optional)

To verify the content of the vector database before deploying, run the query script
against the `vector_db` directory produced in Step 4:

```bash
podman run --rm \
  --userns=keep-id \
  -v "$(pwd)/output/vector_db:/db:Z" \
  <rag-tool-image>:<tag> \
  python /rag-content/scripts/query_rag.py \
    -p /db \
    -x my-docs-index \
    -m /rag-content/embeddings_model \
    -k 5 \
    -q "your test query here"
```

---

## Using a Custom Embedding Model

To use a different HuggingFace model, download it locally first:

```bash
podman run --rm \
  -v "$(pwd)/my_embeddings:/embeddings:Z" \
  <rag-tool-image>:<tag> \
  python /rag-content/scripts/download_embeddings_model.py \
    -l /embeddings \
    -r <hf-repo-id>
```

Then pass `-d /embeddings` and `-m <hf-repo-id>` to `generate_embeddings.py`.

---

## Notes

- The `:Z` SELinux label on volume mounts is required on Fedora/RHEL systems.
- `--userns=keep-id` is required on Fedora/RHEL so the container writes files as your host user.
- Replace `podman` with `docker` if you use Docker instead.
- The embedding model is baked into the tool image at `/rag-content/embeddings_model`,
  so no separate download is needed for `sentence-transformers/all-mpnet-base-v2`.
- The output image archive includes the vector database and (by default) the embedding model,
  so the deployed image is self-contained and does not require the tool image at runtime.
- URL warnings (`URL not reachable`) during processing are harmless — they reflect that
  metadata URLs in YAML frontmatter are not publicly accessible, but do not affect embeddings.

---

## YAML Frontmatter Support

The embedding pipeline works correctly with Markdown files that include YAML frontmatter.
Frontmatter is read automatically. When a file starts with `---`, the `title:` and `url:`
fields are extracted and used as document metadata.

| File has YAML frontmatter? | Title source        | URL source          |
|----------------------------|---------------------|---------------------|
| Yes (`title:` + `url:`)    | YAML `title:` field | YAML `url:` field   |
| Yes (`title:` only)        | YAML `title:` field | fallback → filename |
| No                         | First `# ` heading  | fallback → filename |

Example frontmatter that will be picked up automatically:

```markdown
---
title: "Module: mycompany.infrastructure.create_server"
url: "https://docs.example.com/modules/create_server"
---
