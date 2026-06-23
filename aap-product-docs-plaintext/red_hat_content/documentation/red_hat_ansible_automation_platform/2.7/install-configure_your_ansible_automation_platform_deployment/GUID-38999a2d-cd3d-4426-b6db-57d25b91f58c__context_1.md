# Configure your Ansible Automation Platform deployment
## Enable feature flags in your CR
### About this task

To make feature flag information visible in the web UI to superusers and auditors, enable the `RUNTIME_FEATURE_FLAGS` setting. To lock specific feature flags to a fixed value, add them to the `feature_flags` field. Flags set in the CR are read-only and cannot be changed at runtime.

### Procedure

1.  Edit the `AnsibleAutomationPlatform` custom resource:


```
apiVersion:aap.ansible.com/v1alpha1
kind:AnsibleAutomationPlatform
metadata:
name:myaap
namespace:aap
spec:
extra_settings:
- setting:RUNTIME_FEATURE_FLAGS
value:'@bool True'
feature_flags:
FEATURE_EDA_ANALYTICS_ENABLED:True
FEATURE_POLICY_AS_CODE_ENABLED:True
```

2.  Save the custom resource. The operator applies the changes automatically.

