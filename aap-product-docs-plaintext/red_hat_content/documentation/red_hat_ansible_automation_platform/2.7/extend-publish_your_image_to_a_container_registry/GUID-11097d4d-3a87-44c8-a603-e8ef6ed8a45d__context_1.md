# Publish your image to a container registry
## About this task

After building your custom RAG container image, upload it to a central container registry to make it accessible for deployment. Publishing the image ensures that your organization’s AI services can securely pull and use the vector database from any authorized environment.

## Procedure

1.  Load the image archive:


```
$ podman load < output/rag-content-output-latest.tar
```

2.  Tag the image for your registry:


```
$ podman tag localhost/rag-content-output:latest registry.example.com/aap/my-org-byok-rag:1.0
```

3.  Log in to your container registry:


```
$ podman login registry.example.com
```

4.  **For containerized Ansible deployments only:** Manually pull the image in the containerized installer Ansible Lightspeed instance VM:


```
$ podman pull registry.example.com/aap/my-org-byok-rag:1.0
```

5.  Push the image:


```
$ podman push registry.example.com/aap/my-org-byok-rag:1.0
```

