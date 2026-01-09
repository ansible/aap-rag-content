# 2. Configuring the Red Hat Ansible Automation Platform Operator on Red Hat OpenShift Container Platform
## 2.4. Accessing platform gateway through the OpenShift Container Platform CLI
### 2.4.3. Decoding the platform gateway password




After you have fetched your gateway password, you must decode it from base64.

**Procedure**

- Run the following command to decode your password from base64:


```
oc get secret/example-admin-password -o jsonpath={.data.password} | base64 --decode
```

**Additional resources**

-  [OpenShift Container Platform product documentation](https://docs.redhat.com/en/documentation/openshift_container_platform/)


