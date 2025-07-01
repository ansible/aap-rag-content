# 7. Implementing policy enforcement
## 7.1. Enabling policy enforcement




During installation, you must configure your Ansible Automation Platform instance to include the policy enforcement feature. You can do this by modifying the feature flag variables in your configuration file. Follow the instructions below relevant to your installation type.

**OpenShift Container Platform Installation**

For OpenShift Container Platform installations, you must modify the Ansible Automation Platform custom resource. Add the following to the spec section:


```
spec:
feature_flags:
FEATURE_POLICY_AS_CODE_ENABLED: True
```

After applying the changes, wait for the operator to complete the update process. The operator automatically handles the necessary service restarts and configuration updates.

**RPM Installation**

For RPM-based installations, modify the inventory file used by the installer to add the following variable:


```
feature_flags:
FEATURE_POLICY_AS_CODE_ENABLED: True
```

See [Defining variables at runtime](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_variables.html#defining-variables-at-runtime) for more on adding vars. After modifying the inventory file, rerun the installer to apply changes.

**Containerized Installation**

For containerized installations, modify the inventory file used by the installer to add:


```
feature_flags:
FEATURE_POLICY_AS_CODE_ENABLED: True
```

After modifying the inventory file, rerun the installer to apply the changes.

**Verifying feature flag status**

To verify that the feature flag is enabled, you can check the feature flags state endpoint:


```
https://&lt;your-aap-host&gt;/api/controller/v2/feature_flags_state/
```

The endpoint will return a `JSON` response containing the current state of all feature flags, including `FEATURE_POLICY_AS_CODE_ENABLED` .

**Additional resources**

-  [How to set feature flags for Red Hat Ansible Automation Platform](https://access.redhat.com/articles/7109282)


