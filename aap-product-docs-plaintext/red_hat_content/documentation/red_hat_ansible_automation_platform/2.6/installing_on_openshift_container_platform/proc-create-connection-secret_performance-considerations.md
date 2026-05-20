# 13. Ansible Automation Platform Resource Operator
## 13.4. Creating a Ansible Automation Platform connection secret for Resource Operator

To make your connection information available to the Resource Operator, create a k8s secret with the token and host value.

**Procedure**

1. The following is an example of the YAML for the connection secret. Save the following example to a file, for example, `aap-connection-secret.yml`.

apiVersion: v1
kind: Secret
metadata:
name: aap-access
type: Opaque
stringData:
token: <generated-token>
host: https://aap-host.example.com/

2. Edit the file with your host and token value.

3. Apply it to your cluster by running the `kubectl create` command:

kubectl create -f aap-connection-secret.yml

