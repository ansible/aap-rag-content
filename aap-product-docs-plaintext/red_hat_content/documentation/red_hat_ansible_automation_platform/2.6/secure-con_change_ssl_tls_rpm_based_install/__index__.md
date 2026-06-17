# RPM-based installations

To renew or change SSL/TLS certificates for RPM-based installations, you can edit the inventory file and run the installation program. The installation program verifies that all Ansible Automation Platform components are working.

Alternatively, you can change the SSL/TLS certificates manually. This is quicker, but there is no automatic verification.

Red Hat recommends that you use the installation program to make changes to your Ansible Automation Platform deployment.

## Renewing the self-signed SSL/TLS certificates

The following steps regenerate new SSL/TLS certificates for all Ansible Automation Platform components.

### Procedure

1.  Add `aap_service_regen_cert=true` to the inventory file in the `[all:vars]` section:


```
[all:vars]
aap_service_regen_cert=true
```

2.  Run the installation program.

### Results

- Validate the CA file and certificate file on Event-Driven Ansible controller:

```
openssl verify -CAfile ansible-automation-platform-managed-ca-cert.crt /etc/ansible-automation-platform/eda/server.cert
openssl s_client -connect <EDA_FQDN>:443
```

- Validate the CA file and certificate file on platform gateway:

```
openssl verify -CAfile ansible-automation-platform-managed-ca-cert.crt /etc/ansible-automation-platform/gateway/gateway.cert
openssl s_client -connect <GATEWAY_FQDN>:443
```

- Validate the CA file and certificate file on automation hub:

```
openssl verify -CAfile ansible-automation-platform-managed-ca-cert.crt /etc/pulp/certs/pulp_webserver.crt
openssl s_client -connect <HUB_FQDN>:443
```

- Validate the CA file and certificate file on automation controller:

```
openssl verify -CAfile ansible-automation-platform-managed-ca-cert.crt /etc/tower/tower.cert
openssl s_client -connect <CONTROLLER_FQDN>:443
```

## Change SSL/TLS certificates and keys using the installation program

The following procedure describes how to change the SSL/TLS certificate and key in the inventory file.

### Before you begin

- The certificates must be in PEM format.
- If there is an intermediate certificate authority, you must append it to the server certificate.
- Use the correct order for the certificates: The server certificate comes first, followed by the intermediate certificate authority.


For further information, see the [ssl certificate section of the NGINX documentation](http://nginx.org/en/docs/http/ngx_http_ssl_module.html#ssl_certificate).

### Procedure

1.  Copy the new SSL/TLS certificates and keys to a path relative to the Ansible Automation Platform installer.
2.  Add the absolute paths of the SSL/TLS certificates and keys to the inventory file. Refer to [Inventory file variables](/documentation/en-us/red_hat_ansible_automation_platform/2.6/install-assembly_appendix_inventory_file_vars "The following tables contain information about the variables used in Ansible Automation Platform’s installation inventory files.") for guidance on setting these variables.   - Event-Driven Ansible controller: `automationedacontroller_ssl_cert`, `automationedacontroller_ssl_key`, `custom_ca_cert`
- Platform gateway: `automationgateway_ssl_cert`, `automationgateway_ssl_key`, `custom_ca_cert`
- Automation hub: `automationhub_ssl_cert`, `automationhub_ssl_key`, `custom_ca_cert`
- Automation controller: `web_server_ssl_cert`, `web_server_ssl_key`, `custom_ca_cert`
Note:
The `custom_ca_cert` must be the root certificate authority that signed the intermediate certificate authority. This file is installed in `/etc/pki/ca-trust/source/anchors`.

3.  Run the installation program.

## Change SSL/TLS certificates and keys manually

The following procedure describes how to change SSL/TLS certificates and keys manually for all Ansible Automation Platform components.

### Procedure

1.  Backup the current SSL/TLS certificate:


```
cp <CERT_PATH> <CERT_PATH>-$(date +%F)
```

2.  Backup the current key files:


```
cp <KEY_PATH> <KEY_PATH>-$(date +%F)
```

3.  Copy the new SSL/TLS certificate to the certificate path.
4.  Copy the new key to the key path.
5.  Restore the SELinux context:


```
restorecon -v <CERT_PATH> <KEY_PATH>
```

6.  Set appropriate permissions for the certificate and key files:


```
chown <OWNER>:<GROUP> <CERT_PATH> <KEY_PATH>
chmod 0600 <CERT_PATH> <KEY_PATH>
```

7.  Test the NGINX configuration:


```
nginx -t
```

8.  Reload NGINX:


```
systemctl reload nginx.service
```

9.  Restart services on each platform gateway server:


```
automation-gateway-service restart
```

10.  Verify that new SSL/TLS certificate and key have been installed:


```
true | openssl s_client -showcerts -connect <COMPONENT_FQDN>:443
```
*Table 1. SSL/TLS certificate and key file paths per service*

| Service                             | Certificate file path                                        | Key file path                                               | Owner:Group         |
| ----------------------------------- | ------------------------------------------------------------ | ----------------------------------------------------------- | ------------------- |
| <br>Automation controller           | <br> `/etc/tower/tower.cert`                                 | <br> `/etc/tower/tower.key`                                 | <br> `root:awx`     |
| <br>Automation hub                  | <br> `/etc/pulp/certs/pulp_webserver.crt`                    | <br> `/etc/pulp/certs/pulp_webserver.key`                   | <br> `root:pulp`    |
| <br>Event-Driven Ansible controller | <br> `/etc/ansible-automation-platform/eda/server.cert`      | <br> `/etc/ansible-automation-platform/eda/server.key`      | <br> `root:eda`     |
| <br>Platform gateway                | <br> `/etc/ansible-automation-platform/gateway/gateway.cert` | <br> `/etc/ansible-automation-platform/gateway/gateway.key` | <br> `root:gateway` |
