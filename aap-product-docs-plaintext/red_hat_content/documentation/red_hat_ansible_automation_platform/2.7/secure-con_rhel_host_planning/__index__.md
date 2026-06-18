# Secure your Red Hat Enterprise Linux hosts

The security of Ansible Automation Platform relies in part on the configuration of the underlying Red Hat Enterprise Linux servers.

For this reason, the underlying Red Hat Enterprise Linux hosts for each Ansible Automation Platform component must be installed and configured in accordance with the Security hardening for Red Hat Enterprise Linux 8, Security hardening for Red Hat Enterprise Linux 9, or Security hardening for Red Hat Enterprise Linux 10 (depending on which operating system is used). In addition, install and configure any security profile requirements (*Center for Internet Security* (CIS), STIG, *Health Insurance Portability and Accountability Act* (HIPAA), and so on) used by your organization. This document recommends Red Hat Enterprise Linux 9 for all new deployments. When using the container-based installation method, Red Hat Enterprise Linux 9 is required.

## Ansible Automation Platform and additional software

Dedicate your Red Hat Enterprise Linux servers exclusively to Ansible Automation Platform components. Avoiding the installation of additional server capabilities helps protect system security and performance while maintaining a supported configuration.

Similarly, when Ansible Automation Platform is deployed on a Red Hat Enterprise Linux host, it installs software such as the nginx web server, the Pulp software repository, and the PostgreSQL database server (unless a user-provided external database is used). This software should not be modified or used in a more generic fashion (for example, do not use nginx to serve additional website content or PostgreSQL to host additional databases) as this is an unsupported configuration and might affect the security and performance of Ansible Automation Platform. The configuration of this software is managed by the Ansible Automation Platform installation program, and any manual changes might be undone when performing upgrades.
