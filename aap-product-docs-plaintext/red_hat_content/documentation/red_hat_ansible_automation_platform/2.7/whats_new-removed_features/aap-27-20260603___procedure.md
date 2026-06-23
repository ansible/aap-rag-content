# Removed features
## Procedure

1.      Scan a containerized or RPM SOSReport:

`$ uvx --from "git+https://github.com/ansible/aap-detect-direct-component-access" aap-detect-direct-component-access /path/to/sosreport/`

2.      Scan an OpenShift Container Platform must-gather tarball:

`$ uvx --from "git+https://github.com/ansible/aap-detect-direct-component-access" aap-detect-direct-component-access /path/to/must-gather/`

3.      Scan an OpenShift Container Platform inspect output:

`$ uvx --from "git+https://github.com/ansible/aap-detect-direct-component-access" aap-detect-direct-component-access /path/to/ocp-inspect/`

The tool produces a summary of direct-access requests organized by component, source IP, and request path. Internal traffic such as health checks and readiness probes is excluded automatically.

