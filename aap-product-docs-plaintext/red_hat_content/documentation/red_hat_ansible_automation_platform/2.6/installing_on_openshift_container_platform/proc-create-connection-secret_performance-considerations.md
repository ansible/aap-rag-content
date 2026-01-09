# 13. Ansible Automation Platform Resource Operator
## 13.4. Creating a automation controller connection secret for Resource Operator




To make your connection information available to the Resource Operator, create a k8s secret with the token and host value.

**Procedure**

1. The following is an example of the YAML for the connection secret. Save the following example to a file, for example, `    automation-controller-connection-secret.yml` .


```
apiVersion: v1    kind: Secret    metadata:      name: controller-access      type: Opaque    stringData:      token: &lt;generated-token&gt;      host: https://my-controller-host.example.com/
```


1. Edit the file with your host and token value.
1. Apply it to your cluster by running the `    kubectl create` command:


```
kubectl create -f controller-connection-secret.yml
```

