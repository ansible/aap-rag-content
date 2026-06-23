# Troubleshooting BYOK for the intelligent assistant
## Issue: The containerized installer fails because the BYOK image is not loaded
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
