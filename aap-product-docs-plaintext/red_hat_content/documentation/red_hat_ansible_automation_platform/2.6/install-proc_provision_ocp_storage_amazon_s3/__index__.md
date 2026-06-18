# Configure object storage on Amazon S3

Red Hat supports Amazon Simple Storage Service (S3) for automation hub. You can configure it when deploying the `AnsibleAutomationPlatform` custom resource (CR), or you can configure it for an existing instance.

## Before you begin

- Create an Amazon S3 bucket to store the objects.
- Note the name of the S3 bucket.

## About this task

## Procedure

1.  Create a Kubernetes secret containing the AWS credentials and connection details, and the name of your Amazon S3 bucket. The following example creates a secret called `test-s3`:


```yaml
$ oc -n $HUB_NAMESPACE apply -f- <<EOF
apiVersion: v1
kind: Secret
metadata:
name: 'test-s3'
stringData:
s3-access-key-id: $S3_ACCESS_KEY_ID
s3-secret-access-key: $S3_SECRET_ACCESS_KEY
s3-bucket-name: $S3_BUCKET_NAME
s3-region: $S3_REGION
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
storage_type: S3
object_storage_s3_secret: test-s3
```

Note:
If you have an existing automation hub instance, specify its name using `hub.name: existing-hub-name` to apply these settings to the existing instance.

For more examples of Ansible Automation Platform custom resources, see [Red Hat Ansible Automation Platform custom resources](/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-assembly_appendix_operator_crs#appendix-operator-crs_appendix-operator-crs "This appendix provides a reference for the Ansible Automation Platform custom resources for various deployment scenarios.")

3.  If you are applying this secret to an existing instance, restart the API pods for the change to take effect. `<hub-name>` is the name of your hub instance.

```bash
$ oc -n $HUB_NAMESPACE delete pod -l app.kubernetes.io/name=<hub-name>-api
```
