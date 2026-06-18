# Update the Ansible Automation Platform connection

Change the Ansible Automation Platform host URL, OAuth client ID, API token, or OAuth client secret after deploying the Ansible automation portal RHEL appliance.

## About this task

To change the Ansible Automation Platform host URL or OAuth client ID after deployment, edit the configuration file directly. To update secrets (API token, OAuth client secret), use Podman secrets.

## Procedure

1.  To update the Ansible Automation Platform host URL or OAuth client ID, edit the configuration file:


```terminal
$ sudo vi /etc/portal/configs/app-config/app-config.production.yaml
```
Update `ansible.rhaap.baseUrl` and `auth.providers.rhaap.production.clientId` to the new values. Save the file.

2.  To rotate the Ansible Automation Platform API token:


```terminal
$ temp_file=$(mktemp -p /dev/shm)
$ printf '%s' '<new-aap-token>' > "$temp_file"
$ sudo podman secret create --replace portal_aap_token "$temp_file"
$ rm -f "$temp_file"
```

3.  To rotate the OAuth client secret:


```terminal
$ temp_file=$(mktemp -p /dev/shm)
$ printf '%s' '<new-oauth-client-secret>' > "$temp_file"
$ sudo podman secret create --replace portal_aap_oauth_client_secret "$temp_file"
$ rm -f "$temp_file"
```

4.  Restart the Ansible automation portal service:


```terminal
$ sudo systemctl restart portal
```

## Results

The Ansible automation portal reconnects to the Ansible Automation Platform instance using the updated credentials. Verify the connection by signing in to the portal and confirming that job templates are synchronized.
