+++
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-deploy_your_custom_image_to_an_operator_based_installation"
title = "Deploy your custom image to an operator-based installation - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-extend_the_intelligent_assistant_with_custom_knowledge/", "Extend the automation intelligent assistant with custom knowledge"]]
category = "Extend"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/extend-deploy_your_custom_image_to_an_operator_based_installation/aem-page/extend-deploy_your_custom_image_to_an_operator_based_installation.html"
last_crumb = "Deploy your custom image to an operator-based installation"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Deploy your custom image to an operator-based installation"
oversized = "false"
page_slug = "extend-deploy_your_custom_image_to_an_operator_based_installation"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/extend-deploy_your_custom_image_to_an_operator_based_installation"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/extend-deploy_your_custom_image_to_an_operator_based_installation/toc/toc.json"
type = "aem-page"
+++

# Deploy your custom image to an operator-based installation

Deploy the BYOK RAG image to the intelligent assistant for operator-based Ansible Automation Platform 2.7 installations.

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

## What to do next

**Verification**

1. Verify that the chat interface is running correctly.
2. Verify the BYOK configuration if you specified the `chatbot_byok_image `parameter. Ensure that the file `configmap lightspeed-ansible-lightspeed-lightspeed-stack-config` contains the `byok_rag` section.
3. Ask the intelligent assistant questions and evaluate whether responses reflect the BYOK content.
