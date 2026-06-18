# Troubleshooting BYOK for the intelligent assistant

Resolve common issues when deploying or using BYOK with the intelligent assistant.

## Procedure

Begin by retrieving and reviewing the chatbot container logs.

For operator-based installations, run the following command to view the chatbot pod logs:

```
oc logs deployment/<aap-instance>-lightspeed-chatbot-api -n <aap_namespace>
```

In the log output, look for the following entries:

- `BYOK_IMAGE` is set: this confirms that the BYOK image is configured.
- `Knowledge_search` tool results indicate that the intelligent assistant is querying the BYOK RAG pipeline.
- Vector database initialization messages confirm that the BYOK database loaded correctly.
- Errors referring to a missing BYOK image indicate a configuration or deployment error.

## Issue: The containerized installer fails because the BYOK image is not loaded

**Symptom:** The containerized installer fails and displays an error stating that the image is not loaded in Podman.

### About this task

**Cause:** The BYOK image was not pulled to the target Lightspeed node before running the installer. The installer expects the image to be available locally on the node.

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

### The intelligent assistant does not return BYOK-enhanced responses after deployment

**Symptom:** After you deploy the BYOK image, the intelligent assistant responds to queries, but does not incorporate your custom BYOK content.

#### About this task

**Cause:** The chatbot service might not have restarted after the BYOK configuration change, or the BYOK image did not load correctly.

#### Procedure

For containerized installations:

1.  Restart the chatbot service:


```
systemctl --user restart ansible-lightspeed-chatbot.service
```

2.  Verify that the service has restarted:


```
systemctl --user status ansible-lightspeed-chatbot.service
```

3.  Review the chatbot container logs to confirm that the BYOK image loaded:


```
podman logs ansible-lightspeed-chatbot 2>&1 | grep -i "byok"
```

For operator-based installations:

4.  Roll out a restart of the chatbot deployment:


```
oc rollout restart deployment/<aap-instance>-lightspeed-chatbot-api -n <aap_namespace>
```

5.  Wait for the rollout to complete. You can run the following command to check on the status:


```
oc rollout status deployment/<aap-instance>-lightspeed-chatbot-api -n <aap_namespace>
```

6.  Review the chatbot pod logs to confirm that the BYOK image loaded:


```
oc logs deployment/<aap-instance>-lightspeed-chatbot-api -n <aap_namespace> | grep -i "byok"
```
