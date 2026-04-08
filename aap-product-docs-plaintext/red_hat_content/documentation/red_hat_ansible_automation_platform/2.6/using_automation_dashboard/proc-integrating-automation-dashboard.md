# 1. View key usage metrics with automation dashboard
## 1.3. Integrating automation dashboard with your Ansible Automation Platform




Integrate your Ansible Automation Platform instances into the automation dashboard configuration to collect and visualise data and gain insights into your automation.

**Prerequisites**

- You have installed automation dashboard.
- You have verified that automation dashboard is running on HTTPS port 8447 on your Red Hat Enterprise Linux host.

Note

- This verification requires your Ansible Automation Platform login details.
- Port 8447 is enabled by default, but this is configurable.





**Procedure**

1. Configure a personal access token. For more information, see [Configuring access to external applications with token-based authentication](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/access_management_and_authentication/gw-token-based-authentication) .
1. Create or update the `    clusters.yaml` file. You must include the `    access_token` , `    refresh_token` , `    client_id` , and `    client_secret` to enable persistent authentication and automatic token rotation.


```
clusters:      - protocol: https        address: &lt;aap_controller_url&gt;        port: 443        access_token: &lt;access_token_string&gt;        refresh_token: &lt;refresh_token_string&gt;        client_id: &lt;client_id_string&gt;        client_secret: &lt;client_secret_string&gt;        verify_ssl: false        name: &lt;unique_cluster_name&gt;
```

**Configuring TLS verification**

When configuring the `    verify_ssl` parameter, choose the setting that matches your Ansible Automation Platform certificate type:


-  **Commercial certificates:** Set `        verify_ssl: true` .
-  **Self-signed certificates:** Set `        verify_ssl: false` .

Note
The automation dashboard cannot verify self-signed certificates against a custom Certificate Authority (CA).





1. You can add one or more Ansible Automation Platform instances (of the same Ansible Automation Platform version) into the automation dashboard configuration for pulling and combining data by using the following:

Note
If you only have one Ansible Automation Platform instance, then remove the second entry.




```
---    clusters:      - protocol: https			&lt;--- Normally https        address: my-aap.example.com  &lt;--- Can use IP or FQDN without http(s)://        port: 443				&lt;--- Normally 443        access_token: sampleToken	&lt;--- Your preconfigured Ansible Automation Platform read access token      Platform read access token        refresh_token: myRefreshToken        client_id: myClientID        client_secret: myClientSecret        verify_ssl: false		&lt;--- Can be used when using self signed certs        sync_schedules:          - name: Every 5 minutes sync            rrule: DTSTART;TZID=Europe/Ljubljana:20250630T070000 FREQ=MINUTELY;INTERVAL=5            enabled: true     # If there is one Ansible Automation Platform instance, then remove the second entry below.      # Alternately. If there is more than one AAP instance to connect, copy additional entries.      - protocol: https        address: aap2.example.com        port: 443        access_token: WRn2swiqg5spEwUndDkrJoCeg4Qwuw        verify_ssl: true        sync_schedules:          - name: Every 5 minutes sync            rrule: DTSTART;TZID=Europe/Ljubljana:20250630T070000 FREQ=MINUTELY;INTERVAL=5           enabled: true
```

Note
The `    access_token` , `    refresh_token` , and `    client_secret` are stored in the automation dashboard database. These values are encrypted for security.




1. Load and activate your automation dashboard configuration. You must copy the configuration file to the container’s `    /tmp/` directory. The system automatically removes the file from the container after successful processing.


```
podman cp clusters.yaml automation-dashboard-web:/tmp    podman exec -it automation-dashboard-web /venv/bin/python manage.py setclusters /tmp/clusters.yaml
```

Note
If the system cannot remove the file from the /tmp/ directory, it displays an error message and continues running.



Note
**Token Rotation:** The automation dashboard rotates tokens internally for security but does not update your local `    clusters.yaml` file. If you must re-run the `    setclusters` command later, your defined tokens might be expired.

To retrieve the current valid tokens, run the following command and save the output to a new file:


```
podman exec -it automation-dashboard-web /venv/bin/python manage.py getclusters --decrypt &gt; clusters_current.yaml
```






