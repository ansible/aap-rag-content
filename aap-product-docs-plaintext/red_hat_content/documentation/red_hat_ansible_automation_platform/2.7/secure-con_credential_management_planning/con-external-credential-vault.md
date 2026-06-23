# Manage platform credentials
## External credential vault considerations

Secrets management is an essential component of maintaining a secure automation platform. We recommend the following secrets management practice:

Use an external system to manage secrets. In cases where credentials need to be updated, an external system can retrieve updated credentials with less complexity than an internal system. External systems for managing secrets include CyberArk, HashiCorp Vault, {Azure} Key Management, and others.
