# 10. Ansible Automation Platform Resource Operator
## 10.3. Connecting Resource Operator to platform gateway




To connect Resource Operator with platform gateway you must create a Kubernetes secret with the connection information for your automation controller instance.

Use the following procedure to create an OAuth2 token for your user in the platform gateway UI.

Note
You can only create OAuth 2 Tokens for your own user through the API or UI, which means you can only configure or view tokens from your own user profile.



**Procedure**

1. Log in to Red Hat OpenShift Container Platform.
1. In the navigation panel, selectAccess Management→Users.
1. Select the username you want to create a token for.
1. SelectTokens→Automation Execution
1. ClickCreate Token.
1. You can leave **Applications** empty. Add a description and select **Read** or **Write** for the **Scope** .

Note
Make sure you provide a valid user when creating tokens. Otherwise, you get an error message that you tried to issue the command without either specifying a user, or supplying a username that does not exist.




<span id="proc-create-connection-secret_performance-considerations"></span>
= Creating a automation controller connection secret for Resource Operator





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

