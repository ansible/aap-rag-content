# 2. Installing the Ansible plug-ins with a Helm chart on OpenShift Container Platform
## 2.3. Choose a plug-in delivery method
### 2.3.1. Use OCI container delivery method




Red Hat Developer Hub pulls the Ansible plug-ins directly from `registry.redhat.io` as OCI artifacts. This the **recommended method** that requires a registry authentication secret in the same OpenShift project as your Red Hat Developer Hub deployment.

**Prerequisites**

- You have a Red Hat account with access to registry.redhat.io.
- You have a registry service account token from the Red Hat Customer Portal. For more information, see [Registry Service Accounts](https://access.redhat.com/terms-based-registry/) .
- You have access to the OpenShift project. In the same project you had installed Red Hat Developer Hub.
- You have installed the OpenShift CLI (oc) and logged in to your cluster.


**Procedure**

1. Create an auth.json file on your local machine with your registry.redhat.io credentials:


```
{      "auths": {        "registry.redhat.io": {          "auth": "&lt;base64-encoded-username:password&gt;"        }      }    }
```

To generate the base64-encoded value use the `    printf '%s' '&lt;username&gt;:&lt;password&gt;' | base64` command.


1. Create the authentication secret in the OpenShift project where you installed Red Hat Developer Hub.

The secret name must follow the pattern `    &lt;deployment-name&gt;-dynamic-plugins-registry-auth` , where `    &lt;deployment-name&gt;` matches your Red Hat Developer Hub deployment name.


- For a default Red Hat Developer Hub Helm installation with release name `        developer-hub` :


```
oc create secret generic developer-hub-dynamic-plugins-registry-auth \          --from-file=auth.json=./auth.json
```


- If you use a different Helm release name:


```
oc create secret generic &lt;deployment-name&gt;-dynamic-plugins-registry-auth \          --from-file=auth.json=./auth.json
```


- If you already have Podman credentials configured locally:


```
oc create secret generic &lt;deployment-name&gt;-dynamic-plugins-registry-auth \          --from-file=auth.json=${XDG_RUNTIME_DIR}/containers/auth.json
```

Important
Create this secret in the same OpenShift project as your Red Hat Developer Hub deployment, and create it before you configure the plug-ins. Use a Red Hat Registry service account token, not your personal Red Hat account credentials.







**Verification**

- Verify that the secret exists in the project:


```
oc get secret &lt;deployment-name&gt;-dynamic-plugins-registry-auth
```




