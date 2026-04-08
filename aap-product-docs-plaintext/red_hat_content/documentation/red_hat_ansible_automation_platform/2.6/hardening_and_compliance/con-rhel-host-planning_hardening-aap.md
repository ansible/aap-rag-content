# 2. Hardening Ansible Automation Platform
## 2.1. Planning considerations
### 2.1.6. Red Hat Enterprise Linux host planning




The security of Ansible Automation Platform relies in part on the configuration of the underlying Red Hat Enterprise Linux servers.

For this reason, the underlying Red Hat Enterprise Linux hosts for each Ansible Automation Platform component must be installed and configured in accordance with [Security hardening for Red Hat Enterprise Linux 8](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/8/html-single/security_hardening/index) , [Security hardening for Red Hat Enterprise Linux 9](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/security_hardening/index) , or [Security hardening for Red Hat Enterprise Linux 10](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/security_hardening/index) depending on which operating system is used. Also apply any security profiles ( _Center for Internet Security_ (CIS), DISA STIG for RHEL, _Health Insurance Portability and Accountability Act_ (HIPAA), and so on) required by your organization. Red Hat Enterprise Linux hardening and compliance requirements must be applied for all new before Ansible Automation Platform is installed.

Red Hat Enterprise Linux 9 or higher is recommended for all new deployments. When using the container-based installation method, Red Hat Enterprise Linux 9 or higher is required.

The RPM installation method is no longer available for Red Hat Enterprise Linux 10.

#### 2.1.6.1. Ansible Automation Platform and additional software




When installing the Ansible Automation Platform components on Red Hat Enterprise Linux servers, the Red Hat Enterprise Linux servers should be dedicated to that use alone. Additional server capabilities must not be installed in addition to Ansible Automation Platform, as this is an unsupported configuration and might affect the security and performance of the Ansible Automation Platform software.

Similarly, when Ansible Automation Platform is deployed on a Red Hat Enterprise Linux host, it installs software such as the nginx web server, the Pulp software repository, and the PostgreSQL database server (unless a user-provided external database is used). This software should not be modified or used in a more generic fashion (for example, do not use nginx to serve additional website content or PostgreSQL to host additional databases) as this is an unsupported configuration and might affect the security and performance of Ansible Automation Platform. The configuration of this software is managed by the Ansible Automation Platform installation program, and any manual changes might be undone when performing upgrades.

