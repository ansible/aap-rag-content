# 1. Installing Red Hat Ansible Automation Platform Operator on Red Hat OpenShift Container Platform
## 1.4. Installing Red Hat Ansible Automation Platform Operator from the Red Hat OpenShift Container Platform CLI
### 1.4.6. Decoding the platform gateway password




After you have fetched your gateway password, you must decode it from base64.

- Run the following command to decode your password from base64:


```
oc get secret/example-admin-password -o jsonpath={.data.password} | base64 --decode
```

