# Terraform: Backend configuration

Terraform is a HashiCorp tool used to automate various infrastructure tasks. Select this credential type to enable synchronization with the Terraform inventory source.

The Terraform credential requires the **Backend configuration** attribute which must contain the data from a [Terraform backend block](https://developer.hashicorp.com/terraform/language/backend). Saving it stores the file path to the backend configuration in an environment variable `TF_BACKEND_CONFIG_FILE` that is made available to any job with the credential attached.

You can paste, drag a file, browse to upload a file, or click the ![Key](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/leftkey.png) icon to populate the field from an external [Secret Management System](/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-assembly_controller_secret_management "Configure machine and cloud credentials to allow your automation to securely access external services and machines. Encrypting and storing sensitive values like SSH keys and API tokens in the database helps ensure your authentication details remain protected.").

Terraform backend configuration requires the following inputs:

-  **Name**

- Credential type: Select **Terraform backend configuration**.

- Optional: **Organization**

- Optional: **Description**

- **Backend configuration**: Drag a file here or browse to upload. Example configuration for an S3 backend:



```
bucket = "my-terraform-state-bucket"
key = "path/to/terraform-state-file"
region = "us-east-1"
access_key = "my-aws-access-key"
secret_key = "my-aws-secret-access-key"
```

- Optional: **Google Cloud Platform account credentials**
