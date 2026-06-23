# Publish your image to a container registry
## What to do next

Verify that the image is available:

```
podman search registry.example.com/aap/my-org-byok-rag --list-tags
```


The command outputs a list of all available versions, as in the following example output:

```
NAME                                            TAG
registry.example.com/aap/my-org-byok-rag        1.0
```
