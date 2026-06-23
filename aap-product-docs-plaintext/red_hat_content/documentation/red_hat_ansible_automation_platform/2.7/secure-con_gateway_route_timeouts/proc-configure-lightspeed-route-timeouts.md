# Configure platform gateway route timeouts
## Configure Ansible Lightspeed route timeouts

If you use Red Hat Ansible Lightspeed and need to adjust streaming timeouts, configure the `request_timeout_seconds` and `idle_timeout_seconds` fields on the Lightspeed route.

### Before you begin

- You have platform gateway administrator access.
- The `ansible.platform` collection is installed.

### About this task

These fields replace the `max_stream_duration` and `stream_idle_timeout` global proxy settings that were available in Ansible Automation Platform 2.6.

| Removed setting (2.6) | Replacement field (2.7)   | Default |
| --------------------- | ------------------------- | ------- |
| `max_stream_duration` | `request_timeout_seconds` | 3600    |
| `stream_idle_timeout` | `idle_timeout_seconds`    | 60      |

### Procedure

1.  Create or edit a playbook to configure the Ansible Lightspeed route timeouts:


```
---
- name: Configure Ansible Lightspeed route timeouts
hosts: localhost
tasks:
- name: Set Ansible Lightspeed streaming timeouts
ansible.platform.route:
name: 'lightspeed api'
request_timeout_seconds: 3600
idle_timeout_seconds: 60
```
- `request_timeout_seconds` - Maximum total duration in seconds for streaming requests. Replaces the former `max_stream_duration` setting.
- `idle_timeout_seconds` - Idle timeout in seconds. The connection closes if no data is transmitted within this period. Replaces the former `stream_idle_timeout` setting.

2.  Run the playbook:


```
$ ansible-playbook configure-lightspeed-timeouts.yml
```

### Results

Verify the updated timeout settings by querying the route through the API:

```
$ curl -s -k \
-H "Authorization: Bearer <token>" \
https://<gateway-host>/api/gateway/v1/routes/ \
| python3 -m json.tool
```
Locate the Lightspeed route and confirm that `effective_timeout_seconds` and `effective_idle_timeout_seconds` reflect the expected values.

