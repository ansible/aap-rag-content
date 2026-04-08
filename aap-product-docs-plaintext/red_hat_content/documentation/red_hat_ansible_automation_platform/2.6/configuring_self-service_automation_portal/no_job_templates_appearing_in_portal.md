# 5. Troubleshooting Ansible Automation Platform synchronization
## 5.1. No Job Templates appearing in portal




**Issue:** Expected Job Templates are missing from the portal interface.

**Solutions:**

- Verify the `    surveyEnabled` setting in your Helm values file matches the status of your Job Templates.
- Confirm the `    labels` filter includes the correct, approved Ansible Automation Platform Label names.
- Try temporarily removing filters to confirm if the Job Templates appear without restrictions.
- Verify the Ansible Automation Platform Organization name spelling is exact (it is case-sensitive).
- Check Ansible Automation Platform connectivity and the configured token permissions.


