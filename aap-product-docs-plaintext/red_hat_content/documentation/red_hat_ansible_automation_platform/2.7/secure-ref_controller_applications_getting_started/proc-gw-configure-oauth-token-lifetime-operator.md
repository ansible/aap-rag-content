# Get started with OAuth Applications
## Configure the OAuth access token lifetime on OpenShift Container Platform

On an operator-based installation, set the OAuth access token lifetime in the `AnsibleAutomationPlatform` custom resource so platform gateway applies it across reconciliations.

### Before you begin

- Cluster access to edit the `AnsibleAutomationPlatform` custom resource (CR).

### About this task

Set the OAuth access token lifetime in the `AnsibleAutomationPlatform` CR by using `spec.extra_settings`.

Important:

Do not edit the operator-managed platform gateway settings Secret directly. The operator regenerates that Secret from the CR, so manual edits are lost on the next reconciliation.

### Procedure

1. Edit your `AnsibleAutomationPlatform` CR and add the setting under `spec.extra_settings`:


```
apiVersion: aap.ansible.com/v1alpha1
kind: AnsibleAutomationPlatform
metadata:
name: myaap
namespace: ansible-automation-platform
spec:
extra_settings:
- setting: OAUTH2_PROVIDER['ACCESS_TOKEN_EXPIRE_SECONDS']
value: '<seconds>'
```

Replace `myaap` and `ansible-automation-platform` with the name and namespace of your `AnsibleAutomationPlatform` instance. Set `value` to the required lifetime in seconds, as a quoted string. For example, `'28800'` limits token validity to 8 hours.

2. Save the CR.
The operator automatically applies this configuration to platform gateway on the next reconciliation. You do not need to redeploy manually

### What to do next

- Changing the lifetime affects only newly created tokens. Existing tokens keep their original expiration.
- Avoid extremely short lifetimes. A short lifetime can affect the operator service-account OAuth token if that token is recreated after the setting is applied.
