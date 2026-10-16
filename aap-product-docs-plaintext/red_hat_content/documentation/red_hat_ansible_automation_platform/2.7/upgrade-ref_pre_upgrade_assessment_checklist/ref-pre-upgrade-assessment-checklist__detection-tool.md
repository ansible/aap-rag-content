# Pre-upgrade checklist
## Run the pre-upgrade detection tool

Use the pre-upgrade detection tool to identify direct API usage in your Ansible Automation Platform 2.6 environment. The tool analyzes NGINX logs to detect requests that bypass platform gateway.

- For containerized deployments, collect an SOSReport from your deployment.
- For OpenShift Container Platform deployments, collect a must-gather or `ocp-inspect` output.

Note:

The tool requires NGINX log format updates introduced in the Ansible Automation Platform 2.6 patch released March 25, 2026. If your logs do not contain the required fields, apply the provided patch script or upgrade to the latest 2.6.x release before running the detection tool.

For more information, see *Pre-upgrade detection tooling*.

