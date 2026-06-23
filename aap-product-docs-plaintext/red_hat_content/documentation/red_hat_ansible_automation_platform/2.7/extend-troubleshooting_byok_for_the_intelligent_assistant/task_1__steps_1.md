# Troubleshooting BYOK for the intelligent assistant
## Issue: The containerized installer fails because the BYOK image is not loaded
### Procedure

1.  Connect to the Lightspeed node through SSH:


```
ssh ansible@<lightspeed_node>
```

2.  Pull the BYOK image from your registry:


```
podman pull <your_registry>/<repository>/<image>:<label>
```

3.  Verify that the image is available locally:


```
podman images | grep <your-byok-image-name>
```

4.  Run the installer again.

