# Configure feature flags for a containerized installation

Turn on the feature flags capability for your containerized installation.

## Procedure

To enable the feature flags UI page, add the `RUNTIME_FEATURE_FLAGS` setting to `gateway_extra_settings` in your inventory file:

```
gateway_extra_settings=[{"setting": "RUNTIME_FEATURE_FLAGS", "value": "@bool True"}]
```

To lock specific feature flags at install time, add a `feature_flags` block, as in the following example, to your inventory file. Flags set at install time are read-only and cannot be changed at runtime.

```
feature_flags:
FEATURE_EDA_ANALYTICS_ENABLED: True
FEATURE_POLICY_AS_CODE_ENABLED: True
```
