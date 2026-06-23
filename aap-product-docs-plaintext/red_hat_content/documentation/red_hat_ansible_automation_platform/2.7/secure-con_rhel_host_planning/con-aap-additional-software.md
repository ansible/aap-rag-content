# Secure your Red Hat Enterprise Linux hosts
## Ansible Automation Platform and additional software

Dedicate your Red Hat Enterprise Linux servers exclusively to Ansible Automation Platform components. Avoiding the installation of additional server capabilities helps protect system security and performance while maintaining a supported configuration.

Similarly, when Ansible Automation Platform is deployed on a Red Hat Enterprise Linux host, it installs software such as the nginx web server, the Pulp software repository, and the PostgreSQL database server (unless a user-provided external database is used). This software should not be modified or used in a more generic fashion (for example, do not use nginx to serve additional website content or PostgreSQL to host additional databases) as this is an unsupported configuration and might affect the security and performance of Ansible Automation Platform. The configuration of this software is managed by the Ansible Automation Platform installation program, and any manual changes might be undone when performing upgrades.
