# Ansible Automation Platform patch release June 17, 2026
## Platform-gateway

- Removed the `FEATURE_CASE_INSENSITIVE_AUTH_MAPS_ENABLED` feature flag, making case-insensitive matching for authenticator maps always enabled. (AAP-75521)
- Case-insensitive authentication map matching is now always enabled. The `FEATURE_CASE_INSENSITIVE_AUTH_MAPS_ENABLED` feature flag has been removed. (AAP-61226)

