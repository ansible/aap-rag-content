# 3. Installing the Ansible plug-ins with the Operator on OpenShift Container Platform
## 3.4. Choose a plug-in delivery method when using the Operator
### 3.4.1. Use the OCI container delivery with the Operator




Red Hat Developer Hub pulls the Ansible plug-ins directly from `registry.redhat.io` as OCI artifacts. This method requires a registry authentication secret in the same OpenShift project as your Red Hat Developer Hub deployment.

**Prerequisites**

- You have a Red Hat account with access to `    registry.redhat.io` .
- You have a registry service account token from the Red Hat Customer Portal. For more information, see [Registry Service Accounts](https://access.redhat.com/terms-based-registry/) .
- You have access to the OpenShift project where you had installed Red Hat Developer Hub.
- You have installed the OpenShift CLI ( `    oc` ) and logged in to your cluster.


**Procedure**

1. Create an auth.json file on your local machine with your registry.redhat.io credentials:


```
{      "auths": {        "registry.redhat.io": {          "auth": "&lt;base64-encoded-username:password&gt;"        }      }    }
```

To generate the base64-encoded value, use the `    printf '%s' '&lt;username&gt;:&lt;password&gt;' | base64` command.


1. Create the authentication secret in the OpenShift project where you had installed Red Hat Developer Hub.

The secret name must follow the pattern `    &lt;deployment-name&gt;-dynamic-plugins-registry-auth` , where `    &lt;deployment-name&gt;` matches the `    metadata.name` of your Backstage custom resource.


- For a default Operator installation with name `        developer-hub` :


```
oc create secret generic developer-hub-dynamic-plugins-registry-auth \          --from-file=auth.json=./auth.json
```


- If you already have Podman credentials configured locally:


```
oc create secret generic &lt;deployment-name&gt;-dynamic-plugins-registry-auth \          --from-file=auth.json=${XDG_RUNTIME_DIR}/containers/auth.json
```

Important
Create this secret in the same OpenShift project as your Red Hat Developer Hub deployment, and create it before you configure the plug-ins.







**Verification**

- Verify that the secret exists in the project:


```
oc get secret &lt;deployment-name&gt;-dynamic-plugins-registry-auth
```




