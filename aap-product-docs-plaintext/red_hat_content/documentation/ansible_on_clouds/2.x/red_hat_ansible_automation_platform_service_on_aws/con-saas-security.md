# 5. Red Hat Ansible Automation Platform Service on AWS Service Definition
## 5.2. Control plane
### 5.2.9. Security




The platform is a managed service with robust built-in security, including RBAC and data encryption at rest and in transit (AES-256).

#### 5.2.9.1. Identity and access management




Ansible Automation Platform includes a built-in user model for configuring users and RBAC permissions that define access.

Red Hat recommends using an enterprise identity provider with Ansible Automation Platform to implement multi-factor authentication for users. See the [Access management and authentication](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/access_management_and_authentication) guide for more information.

Note
Red Hat advises keeping at least one local administrator account with a long, complex password for emergency access.



#### 5.2.9.2. Encryption




Data is encrypted at rest in both the database and file system using AWS Key Management Service (KMS), which uses AES-256 encryption. Data in transit is encrypted with TLS 1.2 or higher.

We use AWS Customer Managed Keys (CMKs) to enforce encryption across databases, Amazon S3 buckets, and AWS Secrets Manager secrets. These KMS keys are securely stored in AWS Key Management Service (KMS) under Customer Managed Keys. KMS keys are automatically rotated every 365 days to reduce the risk of key compromise. The Amazon S3 bucket is used for automation hub configuration and backups. AWS Secrets Manager secrets is leveraged to store sensitive information such as credentials and configuration details.

