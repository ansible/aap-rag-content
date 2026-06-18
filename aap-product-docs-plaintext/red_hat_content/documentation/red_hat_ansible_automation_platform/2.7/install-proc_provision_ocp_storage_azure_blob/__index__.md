# Configure object storage on Azure Blob

Red Hat supports Azure Blob Storage for automation hub. You can configure it when deploying the `AnsibleAutomationPlatform` custom resource (CR), or you can configure it for an existing instance.

## Before you begin

- Create an Azure Storage blob container to store the objects.
- Note the name of the blob container.

## About this task

## Procedure

1.  Create a Kubernetes secret containing the credentials and connection details for your Azure account, and the name of your Azure Storage blob container. The following example creates a secret called `test-azure`:


```yaml
$ oc -n $HUB_NAMESPACE apply -f- <<EOF
apiVersion: v1
kind: Secret
metadata:
name: 'test-azure'
stringData:
azure-account-name: $AZURE_ACCOUNT_NAME
azure-account-key: $AZURE_ACCOUNT_KEY
azure-container: $AZURE_CONTAINER
azure-container-path: $AZURE_CONTAINER_PATH
azure-connection-string: $AZURE_CONNECTION_STRING
EOF
```

2.  Add the secret to the Ansible Automation Platform custom resource (CR) under the `hub` section in the `spec`:


```yaml
apiVersion: aap.ansible.com/v1alpha1
kind: AnsibleAutomationPlatform
metadata:
name: myaap
spec:
hub:
storage_type: azure
object_storage_azure_secret: test-azure
```

Note:
If you have an existing automation hub instance, specify its name using `hub.name: existing-hub-name` to apply these settings to the existing instance.

For more examples of Ansible Automation Platform custom resources, see [Red Hat Ansible Automation Platform custom resources](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-assembly_appendix_operator_crs#appendix-operator-crs_appendix-operator-crs "This appendix provides a reference for the Ansible Automation Platform custom resources for various deployment scenarios.")

3.  If you are applying this secret to an existing instance, restart the API pods for the change to take effect. `<hub-name>` is the name of your hub instance.

```bash
$ oc -n $HUB_NAMESPACE delete pod -l app.kubernetes.io/name=<hub-name>-api
```
