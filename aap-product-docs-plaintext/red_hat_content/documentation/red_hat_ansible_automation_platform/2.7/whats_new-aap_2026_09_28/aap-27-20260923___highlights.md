# Ansible Automation Platform 2.7 patch release September 28, 2026 (portal-2.2.8)
## Highlights

- **Security:** Third-party dependency updates address vulnerabilities in automation portal plugins, including urllib credential leakage, js-yaml denial of service, qs and undici hardening, isomorphic-git prototype pollution, compression memory leaks, adm-zip archive handling, multer upload handling, and vm2 sandbox issues. The automation portal operator image includes a Go/stdlib fix for XML decoding recursion depth denial of service (CVE-2026-56859).
- **Bug fix:** The SSH login MOTD "View config" command now opens the production app configuration file with `sudo less` instead of incorrectly duplicating the `portal-status` command. (AAP-92035)
- **Enhancement:** Configurable customer support URL via `spec.branding.customerSupportURL`. (AAP-93824)
- **Bug fix:** Configurable AAP organizations for catalog plugin discovery via `spec.plugins.catalog.orgs`. (AAP-93823)
- **Bug fix:** OperatorHub catalog icon updated to match other AAP platform operators. (AAP-92252)
- **Changed:** Operator configuration UI uses Ansible automation portal language instead of Backstage terminology. (AAP-92046)

