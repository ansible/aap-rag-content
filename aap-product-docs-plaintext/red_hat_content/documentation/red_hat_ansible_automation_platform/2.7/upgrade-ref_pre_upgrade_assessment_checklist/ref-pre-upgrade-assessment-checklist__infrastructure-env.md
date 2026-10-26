# Pre-upgrade checklist
## Infrastructure and environment checks

Verify the following infrastructure and environment settings before you upgrade:

- TLS certificates include Subject Alternative Name (SAN) entries for the platform gateway hostname in addition to existing component hostnames.
- For deployments that use proxy servers, verify that `no_proxy` entries use the correct case. The `no_proxy` environment variable is case-sensitive on Red Hat Enterprise Linux.
- For containerized deployments on Red Hat Enterprise Linux with custom mount points, verify that SELinux contexts are set correctly on all non-default paths used by Ansible Automation Platform.
- For deployments that use NFS-backed storage, verify that NFS mount permissions allow read and write access for the Ansible Automation Platform service accounts.
- For Operator-based deployments, verify that PersistentVolumeClaim (PVC) sizes are sufficient for post-upgrade data growth. Review the sizing guidelines in *Automation Orchestrator system requirements*.
- The `oc` CLI is installed and authenticated to your OpenShift cluster (Operator-based deployments only).

