# 1. View key usage metrics with Automation Dashboard
## 1.2. Installing Automation Dashboard




Install Automation Dashboard to collect and analyze key metrics related to job execution, efficiency, and automation savings across your Ansible Automation Platform deployments.

**Prerequisites**

- One of the following tested configurations:


- RHEL 9 x86 or ARM based physical or virtual host.
- With an external database: PostgreSQL v15 database.

Important
Do not attempt to install Automation Dashboard on the same host(s) as Ansible Automation Platform.





- Automation Dashboard installation has been tested with the following configuration:


- 80 GB hard drive (depending on data growth)
- 4 vCPUs x 16 GB RAM
- Disk IOPS - 3000
- Handle up to 10,000 jobs/month and 47M summaries/month
- Connects to three Ansible Automation Platform deployments of the same version

- Access to _baseos_ and _Ansible Automation Platformstream_ repository packages for the RHEL 9 host.
- A non-root login account to the RHEL 9 host for installation.


- This requires passwordless `        sudo` access to root.
- By default, we use the `        $HOMEDIR` of the user account.

- URL details for access to your Ansible Automation Platform instances.
- An Ansible Automation Platform OAuth2 token, which is used for communication between the Ansible Automation Platform instances and Automation Dashboard.
- Access to download the installation bundle providing installation components for the Automation Dashboard.
- Open firewall access to allow for bidirectional communication between AAP instances and the Automation Dashboard.


- This includes HTTPS/443 (or your Ansible Automation Platform configured port) from the dashboard to the Ansible Automation Platform instance(s).
- Port 8447 is the default ingress port for the Automation Dashboard. This port can be configured during installation.
- RHEL firewall ports that might block 5432 to PostgreSQL.

- A supported version of `    ansible-core` installed on supported RHEL versions.


**Procedure**

1. Download the latest installer tar file from access.redhat.com. Navigate to Downloads > Red Hat Ansible Automation Platform Product Software.
1. Copy the installation source file to your RHEL 9 host.
1. Extract the installation source. This will require ~500Mb. of disk space. Throughout this example we will use the ec2-user home directory: `    /home/&lt;username&gt;` .


```
tar -xzvf ansible-automation-dashboard-containerized-setup-bundle-0.1-x86_64.tar.gz    cd ansible-automation-dashboard-containerized-setup/
```


1. Verify that the installation of necessary software by running the following commands:


```
cd ansible-automation-dashboard-containerized-setup    sudo dnf install ansible-core    ansible-galaxy collection install -r requirements.yml
```


1. Create an application `    client_id/client_secret` in your Ansible Automation Platform instance:


1. Create an OAuth2 application using the following steps :


1.  **For Ansible 2.4** :


- Navigate to [https://AAP_CONTROLLER_FQDN/#/applications](https://AAP_CONTROLLER_FQDN/#/applications)

1.  **For Ansible 2.5 and 2.6** :


- Navigate to [https://AAP_GATEWAY_FQDN/access/applications](https://AAP_GATEWAY_FQDN/access/applications)

1. Add the following information:


-  **Name** : automation-dashboard-sso
-  **Authorization grant type** : authorization-code
-  **Organization** : Default
-  **Redirect URIs** : [https://AUTOMATION_DASHBOARD_FQDN/auth-callback](https://AUTOMATION_DASHBOARD_FQDN/auth-callback)
-  **Client type** : Confidential

Note
The values for **Name** , **Organization** , and HTTPS port number for Ansible Automation Platform are configurable. The examples provided in this document assume use of port 443.






1. Save the `        client_id` and `        client_secret information` inputs into the inventory file.
1. Create an Ansible Automation Platform access token:


1. Navigate to [https://AAP_GATEWAY_FQDN/#/users/<id>/tokens](https://AAP_GATEWAY_FQDN/#/users/<id>/tokens) , and create a token using the following information:


- OAuth application: automation-dashboard-sso
- Scope: read

1. Store this access token value. `            clusters.yaml` uses this access token.


1. Copy the example inventory and change it before running the installation program.


```
cp -i inventory.example inventory    vi inventory
```

Important

- This is an example tested inventory containing default values for Ansible Automation Platform 2.4, 2.5, and 2.6.
- You must change the following values to use this inventory configuration in your environment:


- Change the RHEL 9 host occurrences from `            host.example.com` to your FQDN host
- Change the phrase `            TODO` to match your passwords within all `            _admin_password` or `            _pg_password` values.

- For more information, see the [Inventory variables](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_dashboard/assembly-appendix-inventory-file-automation-dashboard#ref-automation-dashboard-inventory-variables) section of this document.



```
# This is our Automation Dashboard front-end application    [automationdashboard]    host.example.com ansible_connection=local        # These are required vars for the installation and should not be removed    [automationdashboard:vars]    # Configure AAP OAuth2 authentication.    # aap_auth_provider_name - name as shown on login page.    aap_auth_provider_name=Ansible Automation Platform    # aap_auth_provider_protocol - http or https    aap_auth_provider_protocol=https    # AAP version - 2.4, 2.5 or 2.6    aap_auth_provider_aap_version=2.5    # aap_auth_provider_host - AAP IP or DNS name, with optional port    aap_auth_provider_host=my-aap.example.com    # aap_auth_provider_check_ssl - enforce TLS check or not.    aap_auth_provider_check_ssl=true    # aap_auth_provider_client_id and aap_auth_provider_client_secret -    # they are obtained from AAP when OAuth2 application is created in AAP.    aap_auth_provider_client_id=TODO    aap_auth_provider_client_secret=TODO            # Specify amount of old data to synchronoize after installation.    # The initial_sync_days=N requests N days of old data, counting from "today".    # The initial_sync_since requests data from the specified data until "today".    # If both are specified, the initial_sync_since will be used.    initial_sync_days=1    # initial_sync_since=2025-08-08        # Hide warnings when insecure https request are made.    # Use this if your AAP uses self-signed TLS certificate.    # show_urllib3_insecure_request_warning=False        # Force clean install-like    # dashboard_update_secret=true        # HTTP/HTTPS settings    # nginx_disable_https=true    # Change nginx_http_port or nginx_https_port if you want to access dashboard on a different TCP port.    # nginx_http_port=8083    # nginx_https_port=8447    # TLS certificate configuration    # The dashboard_tls_cert needs:    #   - contain server certificate, intermediate CA certificates and root CA certificate.    #   - the server certificate must be the first one in the file.    # dashboard_tls_cert=/path/to/tls/dashboard.crt    # dashboard_tls_key=/path/to/tls/dashboard.key        # Enable Django DEBUG.    # django_debug=True        [database]    host.example.com ansible_connection=local        [all:vars]    postgresql_admin_username=postgres    postgresql_admin_password=TODO        # AAP Dashboard - mandatory    # --------------------------    dashboard_pg_containerized=True    dashboard_admin_password=TODO    dashboard_pg_host=host.example.com    dashboard_pg_username=aapdashboard    dashboard_pg_password=TODO    dashboard_pg_database=aapdashboard    #    bundle_install=true    # &lt;full path to the bundle directory&gt;    bundle_dir='{{ lookup("ansible.builtin.env", "PWD") }}/bundle'
```


1. Run the installation program.


```
ansible-playbook -i inventory ansible.containerized_installer.dashboard_install
```




**Verification**

For reference, see the following example output:


```
PLAY RECAP *********************************************************************************************************************************************
ec2-54-147-26-173.compute-1.amazonaws.com : ok=126  changed=51   unreachable=0    failed=0    skipped=42   rescued=0    ignored=0
localhost                  : ok=12   changed=0    unreachable=0    failed=0    skipped=9    rescued=0    ignored=0
```

Alternative configurations are possible (for example, the database for Automation Dashboard can be set on a different host). This requires additional changes to variables in the inventory file. Consult the [Inventory variables](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_dashboard/assembly-appendix-inventory-file-automation-dashboard#ref-automation-dashboard-inventory-variables) section of this document for available variables.

