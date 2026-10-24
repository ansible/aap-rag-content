# Ansible Automation Platform 2.7 patch release September 28, 2026 (portal-2.2.8)
## Ansible automation portal operator Technology Preview

- OperatorHub catalog icon updated to the Ansible product icon. (AAP-92252)
- Fixed an issue where the operator pod entered CrashLoopBackOff after successful reconciliation due to health probe failures on port 8081. (AAP-92908)
- Added `spec.plugins.catalog.orgs` to scope catalog plugin discovery to specified AAP organizations; when omitted, existing single-org behavior is unchanged. (AAP-93823)
- Fixed an issue where the DevTools sidecar defaulted to the community `ghcr.io/ansible/community-ansible-dev-tools:devel` image when `spec.devtools.image` was omitted, instead of the documented production Red Hat stream. Override via `spec.devtools.image` for air-gapped installs. (AAP-92057)
- Fixed an issue where `app.baseUrl`, `backend.baseUrl`, and `backend.cors.origin` were not set in the generated portal-app-config when `spec.deployment.route.enabled` was false and a custom `spec.deployment.route.host` was used, causing the GitHub sign-in page instead of Sign in using Ansible Automation Platform. (AAP-94213)

