# Deploy your custom image to an operator-based installation
## Before you begin

- The BYOK RAG image built from your documentation has been published to a registry accessible from the OpenShift cluster.
- The Ansible Automation Platform operator installation is complete, and the intelligent assistant has been deployed. You can also install the BYOK image and the intelligent assistant simultaneously.
- `oc`CLI is configured with cluster access.

## Procedure

1.  Log in to Red Hat OpenShift Container Platform as an administrator.
2.  Navigate to the namespace where you want to deploy the BYOK RAG image.
3.  Select Operators> (and then)Installed Operators
4.  From the list of installed operators, select Ansible Automation Platform.
5.  In the **AnsibleAutomationPlatform** custom resource, select the YAML view, and set the following values in the `chatbot_extra_settings `parameters under the `spec: `section:


```
---
...
spec:
lightspeed:
...
chatbot_extra_settings:
chatbot_byok_image: 'quay.io/<repository>/rag-content-output'                                                          chatbot_byok_image_version: latest chatbot_byok_storage_size: '500Mi'                        chatbot_byok_score_multiplier: 1.2
```
The parameters above correspond to the values in the following table.

| Parameter                       | Description                                                                                                                                                                                                                       | Default value |
| ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| `chatbot_byok_image`            | The full registry path to your RAG image.                                                                                                                                                                                         | n/a           |
| `chatbot_byok_image_version`    | The specific version tag (for example,`1.0`) of the image to pull.                                                                                                                                                                | `latest`      |
| `chatbot_byok_storage_size`     | <br>The amount of persistent storage allocated for the BYOK volume.<br>Keep the BYOK data between 1 Mi and 999 Mi for best performance. While the system supports larger allocations up to 2 Gi, smaller volumes are recommended. | `2 Gi`        |
| `chatbot_byok_score_multiplier` | The score multiplier for BYOK content priority. It adjusts how heavily the AI weighs your custom data versus base knowledge.                                                                                                      | `1.2`         |

6.  If the BYOK image is in a private registry, you must create an image pull secret, and set the following values in the `chatbot_extra_settings` parameters under the `spec: `section:


```
spec:
lightspeed:
...
image_pull_secrets:
- my-image-pull-secret
```

7.  Click **Save**. The operator deployes the BYOK RAG image.

