# Access Ansible Automation Platform through the CLI
## Decode the platform gateway password

After you have fetched your gateway password, you must decode it from base64.

### About this task

### Procedure

Run the following command to decode your password from base64:

```
oc get secret/example-admin-password -o jsonpath={.data.password} | base64 --decode
```
