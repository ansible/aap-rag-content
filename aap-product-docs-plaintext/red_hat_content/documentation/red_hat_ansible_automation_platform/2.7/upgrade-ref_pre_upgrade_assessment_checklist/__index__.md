# Pre-upgrade migration checklist

Before upgrading to Red Hat Ansible Automation Platform 2.7, assess the environment to identify components and integrations that require migration to gateway-based authentication.

Before upgrading, identify the following items in your environment:

- Scripts using direct component URLs (for example, `controller.example.com`, `hub.example.com`, or `eda.example.com`).
- Configuration as Code (CaC) implementations.
- Active Personal Access Tokens (PATs).
- API integrations and custom applications.
- Container registry workflows, such as `podman login` or `docker login`.
- Certified collection usage, specifically the latest versions of `ansible.controller`, `ansible.hub`, and `ansible.eda` (these may be replaced by `ansible.platform`).
- Third-party authentication provider configurations, including LDAP, SAML, RADIUS, and TACACS+.

## Pre-upgrade detection tooling

A CLI detection tool is available to identify direct API usage in Ansible Automation Platform 2.5 or 2.6 environments. The tool analyzes NGINX logs to detect requests that bypass platform gateway.

You can run the tool directly from the GitHub repository using `uvx`.

**Prerequisites**

- Ansible Automation Platform 2.5 or 2.6 is installed.
- You have one of the following, depending on your deployment type:
* Containerized deployments: An SOSReport.
* OpenShift Container Platform deployments: A must-gather or ocp-inspect output.


Note:

The tool requires NGINX log format updates introduced in the Ansible Automation Platform 2.6 patch released March 25, 2026. If you are running an earlier 2.6.x patch and your logs do not contain the required fields, apply the provided patch script or upgrade to the latest 2.6.x release.

**Scan a containerized or RPM SOSReport:**

```
$ uvx --from "git+https://github.com/ansible/aap-detect-direct-component-access" aap-detect-direct-component-access /path/to/sosreport/
```
**Scan an OpenShift must-gather tarball:**

```
$ uvx --from "git+https://github.com/ansible/aap-detect-direct-component-access" aap-detect-direct-component-access /path/to/must-gather/
```
**Scan an OpenShift Container Platform inspect output:**

```
$ uvx --from "git+https://github.com/ansible/aap-detect-direct-component-access" aap-detect-direct-component-access /path/to/ocp-inspect/
```
