# Troubleshoot Ansible automation portal authentication
## Diagnose authentication failures

If the symptom table does not match your issue, use the following steps to gather diagnostic information.

1. Check portal backend logs for authentication errors:

```terminal
$ oc logs -n *namespace* deployment/*portal-deployment-name* -c backstage-backend | grep -i "auth\|rhaap\|error\|fetch\|token"
```

2. Check for certificate-related failures from inside the pod:

```terminal
$ oc exec -n *namespace* deployment/*portal-deployment-name* -c backstage-backend -- \
curl -k -s -o /dev/null -w "HTTP_CODE: %{http_code}\nSSL_VERIFY: %{ssl_verify_result}\n" \
https://*aap-host*/
```
- `HTTP_CODE: 200` confirms Ansible Automation Platform is reachable.
- `SSL_VERIFY: 0` means the certificate is trusted. `SSL_VERIFY: 20` means the issuer certificate is not in the trust store (self-signed CA).

3. Verify the Ansible Automation Platform OAuth application configuration:

```terminal
$ curl -k -s -u *admin-user*:*password* https://*aap-host*/api/gateway/v1/me/ | python3 -m json.tool
```
A successful response confirms Ansible Automation Platform credentials are valid and the API is accessible.

For a complete list of common log messages and their meanings, see [View Ansible automation portal logs for execution environment builder](/documentation/en-us/red_hat_ansible_automation_platform/2.7/troubleshoot-proc_view_ee_builder_logs "View Ansible automation portal logs to diagnose authentication failures, sync errors, catalog registration issues, and SCM connectivity problems.").
