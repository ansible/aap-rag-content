# Resource Operator custom resources
## Resource Operator custom resources [tower.ansible.com/v1alpha1]
### AnsibleCredential

Creates a credential on the automation controller for authenticating with external systems.

| Field                | Type   | Description                                                                                 | Default        |
| -------------------- | ------ | ------------------------------------------------------------------------------------------- | -------------- |
| `connection_secret`  | String | Name of the Kubernetes secret containing the platform gateway connection details. Required. | -              |
| `name`               | String | Display name for the credential.                                                            | -              |
| `organization`       | String | Organization the credential belongs to.                                                     | -              |
| `description`        | String | Description of the credential.                                                              | -              |
| `type`               | String | Credential type, for example `Machine`, `Amazon Web Services`.                              | -              |
| `ssh_username`       | String | SSH username for Machine type credentials.                                                  | -              |
| `ssh_secret`         | String | Name of a Kubernetes secret containing the SSH private key for Machine type credentials.    | -              |
| `username_secret`    | String | Name of a Kubernetes secret containing the username for cloud credentials.                  | -              |
| `password_secret`    | String | Name of a Kubernetes secret containing the password for cloud credentials.                  | -              |
| `runner_pull_policy` | String | Image pull policy for the runner pod.                                                       | `IfNotPresent` |


**Example (SSH):**

```
apiVersion: tower.ansible.com/v1alpha1
kind: AnsibleCredential
metadata:
name: ssh-cred
spec:
connection_secret: aap-access
name: ssh-cred
organization: Default
type: "Machine"
ssh_username: "ansible"
ssh_secret: my-ssh-secret
```

