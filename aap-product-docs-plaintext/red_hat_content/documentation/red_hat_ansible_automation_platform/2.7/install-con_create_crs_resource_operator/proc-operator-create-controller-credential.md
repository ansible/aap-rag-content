# Create a custom resource for Resource Operator
## Create an automation controller credential custom resource

Credentials authenticate the automation controller user when launching jobs against machines, synchronizing with inventory sources, and importing project content from a version control system.

### About this task

SSH and AWS are the most commonly used credentials. For a full list of supported credentials see[Credential types](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-ref_controller_credential_types "Ansible Automation Platform supports a number of credential types.") .

For help with defining values you can refer to the [OpenAPI (Swagger) file for Red Hat Ansible Automation Platform API](https://access.redhat.com/login?redirectTo=https%3A%2F%2Faccess.redhat.com%2Fsolutions%2F7050627) KCS article.

Note:

You can use `https://<aap-instance>/api/controller/v2/credential_types/` to view the list of credential types on your instance. To get the full list use the following `curl` command:

```
export AAP_TOKEN="your-oauth2-token"
export AAP_URL="https://your-aap-controller.example.com"

curl -s -H "Authorization: Bearer $AAP_TOKEN" "$AAP_URL/api/controller/v2/credential_types/" | jq -r '.results[].name'
```

### Procedure

Create an AWS or SSH credential on automation controller by creating a credential custom resource:

- SSH credential:

```
apiVersion: tower.ansible.com/v1alpha1
kind: AnsibleCredential
metadata:
name: ssh-cred
spec:
name: ssh-cred
organization: Default
connection_secret: aap-access
description: "SSH credential"
type: "Machine"
ssh_username: "cat"
ssh_secret: my-ssh-secret
runner_pull_policy: IfNotPresent
```

- AWS credential:

```
apiVersion: tower.ansible.com/v1alpha1
kind: AnsibleCredential
metadata:
name: aws-cred
spec:
name: aws-access
organization: Default
connection_secret: aap-access
description: "This is a test credential"
type: "Amazon Web Services"
username_secret: aws-secret
password_secret: aws-secret
runner_pull_policy: IfNotPresent
```
