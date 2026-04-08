# 14. Troubleshooting the Red Hat Ansible Automation Platform Operator on OpenShift Container Platform
## 14.11. Operator service account error




Manually modifying the `aap_operator_service_account` user in the Ansible Automation Platform database or UI removes the required `is_superuser` flag. This action causes a critical failure in the platform gateway operator’s reconciliation loop.

You see the following error:

```
TASK [ansibleautomationplatform : Create operator service account user] … CommandError: Error: That username is already taken
```

The Ansible Automation Platform operator automatically recreates the service account when the account is missing. To restore the required superuser privileges, you must remove the existing, incorrectly configured user.

After you delete the user, the platform gateway operator automatically runs its idempotency logic, recreates the account, and ensures it has the necessary `is_superuser=True` flag, restoring the reconciliation loop’s functionality.

