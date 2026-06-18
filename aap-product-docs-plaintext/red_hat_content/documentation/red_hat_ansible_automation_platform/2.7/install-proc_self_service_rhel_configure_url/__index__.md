# Set a custom user-accessible URL or port

The Ansible automation portal RHEL appliance auto-detects the user-accessible URL from the VM IP address at each boot. To set a custom hostname or port, update the configuration file and restart the service.

## Before you begin

- SSH access to the appliance.
- The hostname or IP address and port that users will use to access Ansible automation portal.

## Procedure

1.  Edit the configuration file:


```terminal
$ sudo vi /etc/portal/configs/app-config/app-config.production.yaml
```

2.  Update the following three values.
This example uses port 8443. If you are using the standard port 443, you do not need to specify the port:

```yaml
app:
baseUrl: "https://portal.example.com:8443"
backend:
baseUrl: "https://portal.example.com:8443"
cors:
origin: "https://portal.example.com:8443"
```

3.  Save the file and restart the Ansible automation portal service.
Restarting the `portal` service also restarts `postgres` and `devtools` due to service dependencies:

```terminal
$ sudo systemctl restart portal
```

4.  If you set a custom port, open that port on any firewall and, for Red Hat OpenShift Virtualization deployments, update the OpenShift route.
5.  Update the OAuth redirect URI in Ansible Automation Platform to match the new URL.

## Results

Verify that Ansible automation portal is accessible at the new URL:

```terminal
$ curl -fk https://*new-url*
```
A successful response confirms that the URL and port are configured correctly.
