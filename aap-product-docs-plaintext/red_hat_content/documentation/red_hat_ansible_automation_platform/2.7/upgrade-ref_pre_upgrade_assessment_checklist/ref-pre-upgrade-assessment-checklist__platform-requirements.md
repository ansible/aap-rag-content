# Pre-upgrade checklist
## Platform and version requirements

Verify the following platform requirements before you begin the upgrade:

- Your deployment is running the latest Ansible Automation Platform 2.6 release.
- Your deployment uses a containerized or OpenShift Container Platform installation method. RPM-based deployments cannot upgrade directly to 2.7.
- For containerized deployments: Red Hat Enterprise Linux 9 or Red Hat Enterprise Linux 10.
- For Operator-based deployments: OpenShift Container Platform 4.18 through 4.23 with `cluster-admin` access.
- You have a valid Red Hat Ansible Automation Platform subscription.
- PostgreSQL version compatibility: PostgreSQL 15 for platform-managed databases, or PostgreSQL 15, 16, or 17 with International Components for Unicode (ICU) support for customer-provided databases.

