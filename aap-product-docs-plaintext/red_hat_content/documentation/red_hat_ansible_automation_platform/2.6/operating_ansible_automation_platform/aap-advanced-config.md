# Chapter 4. Advanced configurations




As a platform administrator, you can implement advanced configurations to customize Ansible Automation Platform, including database connections, logging, caching, and gRPC server parameters.

## 4.1. `settings.py` file




As a platform administrator, you can modify the `settings.py` file to configure various aspects of Ansible Automation Platform, such as database connections, logging configurations, caching, and more.

There are two `settings.py` files; the default `settings.py` that is part of the codebase and must not be edited, and an override file that can be used to override the default values.

The location and management of the override `settings.py` file can differ based on your deployment (RPM-based, container-based installation, or operator-based installation).

### 4.1.1. RPM deployments




The override `settings.py` file in an RPM-based setup can be edited directly, and changes take effect after restarting the platform gateway service. If you choose to edit the file, be sure to use the proper syntax and values. The override `settings.py` file is located in the following directory:

```
/etc/ansible-automation-platform/gateway/settings.py
```

### 4.1.2. Container-based deployments




For container-based installation deployments, Ansible Automation Platform runs within containers and the `settings.py` file is included inside the container. However, directly editing the `settings.py` file in container-based installation deployments is not recommended because the `settings.py` file is overwritten during upgrades or new installs.

To customize settings in container-based installation deployments, you can use the `extra_settings` parameter to ensure that customizations persist through installer updates. For more information, see [Inventory file variables](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/containerized_installation/appendix-inventory-files-vars) in the Containerized installation guide.

### 4.1.3. Operator-based deployments




For operator-based installation deployments, the `settings.py` file is typically located inside the container, however, users cannot modify the `settings.py` files directly in the container because containers in Red Hat OpenShift Container Platform are read-only.

Instead, for operator-based deployments, you can modify the settings for the platform gateway using the `spec.extra_settings` parameter on the Ansible Automation Platform custom resource.

## 4.2. `grpc_settings.py` file




Platform administrators can use the `grpc_settings.py` file to define special or custom parameters for the gRPC server.

There are two gRPC settings files: the default `grpc_default.py` that is part of the codebase and must not be edited, and an override file that can be used to override the default values. The `grpc_default.py` file includes database keepalive OPTIONS to help maintain a healthy gRPC connection and prevent interruptions. If it was necessary to change these defaults, the `grpc_settings.py` file can be used to override values from the `grpc_defauly.py` file.

The location and management of the override `grpc_settings.py` file can differ based on your deployment (RPM-based, container-based installation or operator-based installation).

### 4.2.1. RPM deployments




The override `grpc_settings.py` file in an RPM-based setup can be edited directly, and changes take effect after restarting the gateway systemd service. If you choose to edit the file, be sure to use the proper syntax and values. The override `grpc_settings.py` file is located in the following directory:

```
/etc/ansible-automation-platform/gateway/grpc_settings.py
```

### 4.2.2. Impacts of modifying the `grpc_settings.py` file




The gRPC server is responsible for helping with authentication between the different platform services. Altering the settings in the `grpc_settings.py` file can significantly impact the behavior and performance of the gRPC connection, especially in terms of connection stability.

It is important to thoroughly test any changes made to the gRPC settings before deploying them to production to ensure that the gRPC server functions as expected.

## 4.3. Loading order of settings




The platform gateway uses the Dynaconf library for managing its application settings. Dynaconf follows a layered configuration approach, where settings are loaded from multiple sources in a defined order, with later sources overriding earlier ones.

Ansible Automation Platform loads settings in the following sequence:

1.  **Application settings.py:** This file is in the application itself and defines the loading order and location of additional settings files.
1.  **Application default settings:** The platform loads default settings from a defaults.py file, which is part of the application itself. This file includes general configurations for both the API Server and the gRPC server.
1.  **Customer override file:** The `    /etc/ansible-automation-platform/gateway/settings.py` file is automatically installed and can be used to override any configuration in `    defaults.py` . Changes to this file affect both the API and gRPC servers.
1.  **Application gRPC default settings:** After the customer override file, the application loads additional default settings for the gRPC server only from the `    grpc_default.py` file. Specifically, this file includes database OPTIONS for the gRPC server, such as the keepalive parameters.
1.  **Customer gRPC override file:** The file `    /etc/ansible-automation-platform/gateway/grpc_settings.py` , if present, is loaded next and any settings contained in this file are applied only to the gRPC server.
1.  **Platform override settings file:** Any settings in the `    /etc/ansible-automation-platform/settings.py` file are applied to both the gRPC server and the API server. If there are multiple Ansible Automation Platform services on a single node, items in this file are applied to all services.
1.  **ENV vars:** Environment variables, where you can configure certain Ansible Automation Platform settings outside of the configuration files, are loaded last. They override any previously loaded settings.


# Chapter 5. Managing usability analytics and data collection from automation controller




You can change how you participate in usability analytics and data collection from automation controller by opting out or changing your settings in the automation controller user interface.

## 5.1. Usability analytics and data collection




Usability data collection is included with automation controller to collect data to better understand how automation controller users specifically interact with automation controller, to help enhance future releases, and to continue streamlining your user experience.

Only users installing a trial of automation controller or a fresh installation of automation controller are opted-in for this data collection.

**Additional resources**

-  [Red Hat privacy policy](https://www.redhat.com/en/about/privacy-policy)


### 5.1.1. Controlling data collection from automation controller




You can control how automation controller collects data from theSettings→Automation Execution→Systemmenu.

**Procedure**

1. Log in to your automation controller.
1. From the navigation panel, selectSettings→Automation Execution→System.
1. Select **Gather data for Automation Analytics** to enable automation controller to gather data on automation and send it to Automation Analytics.


# Chapter 6. Renewing and changing the SSL/TLS certificates




If your current SSL/TLS certificates have expired or will expire soon, you can either renew or replace the SSL/TLS certificates used by Ansible Automation Platform.

You must renew the SSL/TLS certificates if you need to regenerate them with new information such as new hosts.

You must replace the SSL/TLS certificates if you want to use certificates signed by an internal certificate authority.

## 6.1. Container-based installations




You can change the TLS certificates and keys for your container-based Ansible Automation Platform installation. This process involves a preparation step, either providing new custom certificates or deleting or moving the old certificates, followed by running the installation program.

### 6.1.1. Changing TLS certificates and keys using the installation program




The following procedure describes how to update the TLS certificates and keys by using the installation program.

**Procedure**

1. To prepare the certificates and keys, choose one of the following methods:


- To provide custom certificates - For each service that requires updated TLS certificates, copy the new certificates and keys to a path relative to the Ansible Automation Platform installer. Then update the inventory file variables with the absolute paths to the new files.


```
# Platform gateway        gateway_tls_cert=&lt;path_to_tls_certificate&gt;        gateway_tls_key=&lt;path_to_tls_key&gt;        gateway_pg_tls_cert=&lt;path_to_tls_certificate&gt;        gateway_pg_tls_key=&lt;path_to_tls_key&gt;        gateway_redis_tls_cert=&lt;path_to_tls_certificate&gt;        gateway_redis_tls_key=&lt;path_to_tls_key&gt;                # Automation controller        controller_tls_cert=&lt;path_to_tls_certificate&gt;        controller_tls_key=&lt;path_to_tls_key&gt;        controller_pg_tls_cert=&lt;path_to_tls_certificate&gt;        controller_pg_tls_key=&lt;path_to_tls_key&gt;                # Automation hub        hub_tls_cert=&lt;path_to_tls_certificate&gt;        hub_tls_key=&lt;path_to_tls_key&gt;        hub_pg_tls_cert=&lt;path_to_tls_certificate&gt;        hub_pg_tls_key=&lt;path_to_tls_key&gt;                # Event-Driven Ansible        eda_tls_cert=&lt;path_to_tls_certificate&gt;        eda_tls_key=&lt;path_to_tls_key&gt;        eda_pg_tls_cert=&lt;path_to_tls_certificate&gt;        eda_pg_tls_key=&lt;path_to_tls_key&gt;        eda_redis_tls_cert=&lt;path_to_tls_certificate&gt;        eda_redis_tls_key=&lt;path_to_tls_key&gt;                # PostgreSQL        postgresql_tls_cert=&lt;path_to_tls_certificate&gt;        postgresql_tls_key=&lt;path_to_tls_key&gt;                # Receptor        receptor_tls_cert=&lt;path_to_tls_certificate&gt;        receptor_tls_key=&lt;path_to_tls_key&gt;
```


- To generate new certificates - If you want the installation program to generate a new certificate for a service, delete or move the existing certificates and keys.


<span id="idm140162030352448"></span>
**Table 6.1. Certificate and key file paths per service**

| Service | Certificate file path | Key file path |
| --- | --- | --- |
| Automation controller |  `~/aap/controller/etc/tower.cert` |  `~/aap/controller/etc/tower.key` |
| Event-Driven Ansible |  `~/aap/eda/etc/eda.cert` |  `~/aap/eda/etc/eda.key` |
| Platform gateway |  `~/aap/gateway/etc/gateway.cert` |  `~/aap/gateway/etc/gateway.key` |
| Automation hub |  `~/aap/hub/etc/pulp.cert` |  `~/aap/hub/etc/pulp.key` |
| PostgreSQL |  `~/aap/postgresql/server.crt` |  `~/aap/postgresql/server.key` |
| Receptor |  `~/aap/receptor/etc/receptor.crt` |  `~/aap/receptor/etc/receptor.key` |
| Redis |  `~/aap/redis/server.crt` |  `~/aap/redis/server.key` |






1. After preparing your certificates, run the `    install` playbook from your installation directory:


```
ansible-playbook -i &lt;inventory_file_name&gt; ansible.containerized_installer.install
```




**Verification**

Verify that the new TLS certificates are in use by checking that the services are running and accessible. To do this, check a specific endpoint by using `curl` :


```
$ curl -vk https://&lt;hostname_or_ip&gt;:&lt;port_number&gt;/api/v2/
```

The output of this command gives details about the TLS handshake. Look for the following output to confirm the correct certificate is being used:

```
*  SSL certificate verify OK
```

**Additional resources**

-  [Using custom TLS certificates](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/containerized_installation/advanced-configuration-containerized#using-custom-tls-certificates)
-  [Troubleshooting SSL/TLS issues](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/troubleshooting_ansible_automation_platform/troubleshoot-networking#troubleshooting-ssl-tls-issues)
-  [Diagnosing the problem](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/containerized_installation/troubleshooting-containerized-ansible-automation-platform#diagnosing-the-problem_troubleshooting-containerized-aap)


## 6.2. Operator-based installations




### 6.2.1. Changing the automation controller SSL/TLS certificate and key on OpenShift Container Platform




The following procedure describes how to change the SSL/TLS certificate and key for automation controller running on OpenShift Container Platform.

**Procedure**

1. Copy the signed SSL/TLS certificate and key to a secure location.
1. Create a TLS secret within OpenShift:


```
oc create secret tls ${CONTROLLER_INSTANCE}-certs-$(date +%F) --cert=/path/to/ssl.crt --key=/path/to/ssl.key
```


1. Modify the automation controller custom resource to add `    route_tls_secret` and the name of the new secret to the spec section.


```
oc edit automationcontroller/${CONTROLLER_INSTANCE}
```


```
...    spec:      route_tls_secret: automation-controller-certs-2023-04-06    ...
```




The name of the TLS secret is arbitrary. In this example, it is timestamped with the date that the secret is created, to differentiate it from other TLS secrets applied to the automation controller instance.


1. Wait a few minutes for the changes to be applied.
1. Verify that new SSL/TLS certificate and key have been installed:


```
true | openssl s_client -showcerts -connect ${CONTROLLER_FQDN}:443
```




### 6.2.2. Changing the SSL/TLS certificate and key for automation hub on OpenShift Container Platform




The following procedure describes how to change the SSL/TLS certificate and key for automation hub running on OpenShift Container Platform.

**Procedure**

1. Copy the signed SSL/TLS certificate and key to a secure location.
1. Create a TLS secret within OpenShift:


```
oc create secret tls ${AUTOMATION_HUB_INSTANCE}-certs-$(date +%F) --cert=/path/to/ssl.crt --key=/path/to/ssl.key
```


1. Modify the automation hub custom resource to add `    route_tls_secret` and the name of the new secret to the spec section.


```
oc edit automationhub/${AUTOMATION_HUB_INSTANCE}
```


```
...    spec:      route_tls_secret: automation-hub-certs-2023-04-06    ...
```




The name of the TLS secret is arbitrary. In this example, it is timestamped with the date that the secret is created, to differentiate it from other TLS secrets applied to the automation hub instance.


1. Wait a few minutes for the changes to be applied.
1. Verify that new SSL/TLS certificate and key have been installed:


```
true | openssl s_client -showcerts -connect ${CONTROLLER_FQDN}:443
```




## 6.3. RPM-based installations




To renew or change SSL/TLS certificates for RPM-based installations, you can edit the inventory file and run the installation program. The installation program verifies that all Ansible Automation Platform components are working.

Alternatively, you can change the SSL/TLS certificates manually. This is quicker, but there is no automatic verification.

Red Hat recommends that you use the installation program to make changes to your Ansible Automation Platform deployment.

### 6.3.1. Renewing the self-signed SSL/TLS certificates




The following steps regenerate new SSL/TLS certificates for all Ansible Automation Platform components.

**Procedure**

1. Add `    aap_service_regen_cert=true` to the inventory file in the `    [all:vars]` section:


```
[all:vars]    aap_service_regen_cert=true
```


1. Run the installation program.


**Verification**

- Validate the CA file and certificate file on Event-Driven Ansible controller:


```
openssl verify -CAfile ansible-automation-platform-managed-ca-cert.crt /etc/ansible-automation-platform/eda/server.cert    openssl s_client -connect &lt;EDA_FQDN&gt;:443
```


- Validate the CA file and certificate file on platform gateway:


```
openssl verify -CAfile ansible-automation-platform-managed-ca-cert.crt /etc/ansible-automation-platform/gateway/gateway.cert    openssl s_client -connect &lt;GATEWAY_FQDN&gt;:443
```


- Validate the CA file and certificate file on automation hub:


```
openssl verify -CAfile ansible-automation-platform-managed-ca-cert.crt /etc/pulp/certs/pulp_webserver.crt    openssl s_client -connect &lt;HUB_FQDN&gt;:443
```


- Validate the CA file and certificate file on automation controller:


```
openssl verify -CAfile ansible-automation-platform-managed-ca-cert.crt /etc/tower/tower.cert    openssl s_client -connect &lt;CONTROLLER_FQDN&gt;:443
```




### 6.3.2. Changing SSL/TLS certificates and keys using the installation program




The following procedure describes how to change the SSL/TLS certificate and key in the inventory file.

**Prerequisites**

- The certificates must be in PEM format.
- If there is an intermediate certificate authority, you must append it to the server certificate.
- Use the correct order for the certificates: The server certificate comes first, followed by the intermediate certificate authority.


For further information, see the [ssl certificate section of the NGINX documentation](http://nginx.org/en/docs/http/ngx_http_ssl_module.html#ssl_certificate) .

**Procedure**

1. Copy the new SSL/TLS certificates and keys to a path relative to the Ansible Automation Platform installer.
1. Add the absolute paths of the SSL/TLS certificates and keys to the inventory file. Refer to [Inventory file variables](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/rpm_installation/appendix-inventory-files-vars) for guidance on setting these variables.


- Event-Driven Ansible controller: `        automationedacontroller_ssl_cert` , `        automationedacontroller_ssl_key` , `        custom_ca_cert`
- Platform gateway: `        automationgateway_ssl_cert` , `        automationgateway_ssl_key` , `        custom_ca_cert`
- Automation hub: `        automationhub_ssl_cert` , `        automationhub_ssl_key` , `        custom_ca_cert`
- Automation controller: `        web_server_ssl_cert` , `        web_server_ssl_key` , `        custom_ca_cert`

Note
The `        custom_ca_cert` must be the root certificate authority that signed the intermediate certificate authority. This file is installed in `        /etc/pki/ca-trust/source/anchors` .





1. Run the installation program.


### 6.3.3. Changing SSL/TLS certificates and keys manually




The following procedure describes how to change SSL/TLS certificates and keys manually for all Ansible Automation Platform components.

**Procedure**

1. Backup the current SSL/TLS certificate:


```
cp &lt;CERT_PATH&gt; &lt;CERT_PATH&gt;-$(date +%F)
```


1. Backup the current key files:


```
cp &lt;KEY_PATH&gt; &lt;KEY_PATH&gt;-$(date +%F)
```


1. Copy the new SSL/TLS certificate to the certificate path.
1. Copy the new key to the key path.
1. Restore the SELinux context:


```
restorecon -v &lt;CERT_PATH&gt; &lt;KEY_PATH&gt;
```


1. Set appropriate permissions for the certificate and key files:


```
chown &lt;OWNER&gt;:&lt;GROUP&gt; &lt;CERT_PATH&gt; &lt;KEY_PATH&gt;    chmod 0600 &lt;CERT_PATH&gt; &lt;KEY_PATH&gt;
```


1. Test the NGINX configuration:


```
nginx -t
```


1. Reload NGINX:


```
systemctl reload nginx.service
```


1. Verify that new SSL/TLS certificate and key have been installed:


```
true | openssl s_client -showcerts -connect &lt;COMPONENT_FQDN&gt;:443
```


<span id="idm140162029626896"></span>
**Table 6.2. SSL/TLS certificate and key file paths per service**

| Service | Certificate file path | Key file path | Owner:Group |
| --- | --- | --- | --- |
| Automation controller |  `/etc/tower/tower.cert` |  `/etc/tower/tower.key` |  `root:awx` |
| Automation hub |  `/etc/pulp/certs/pulp_webserver.crt` |  `/etc/pulp/certs/pulp_webserver.key` |  `root:pulp` |
| Event-Driven Ansible controller |  `/etc/ansible-automation-platform/eda/server.cert` |  `/etc/ansible-automation-platform/eda/server.key` |  `root:eda` |
| Platform gateway |  `/etc/ansible-automation-platform/gateway/gateway.cert` |  `/etc/ansible-automation-platform/gateway/gateway.key` |  `root:gateway` |








<span id="idm140162035190288"></span>
# Legal Notice

Copyright© Red Hat.
Except as otherwise noted below, the text of and illustrations in this documentation are licensed by Red Hat under the Creative Commons Attribution–Share Alike 3.0 Unported license . If you distribute this document or an adaptation of it, you must provide the URL for the original version.
Red Hat, as the licensor of this document, waives the right to enforce, and agrees not to assert, Section 4d of CC-BY-SA to the fullest extent permitted by applicable law.
Red Hat, the Red Hat logo, JBoss, Hibernate, and RHCE are trademarks or registered trademarks of Red Hat, LLC. or its subsidiaries in the United States and other countries.
Linux® is the registered trademark of Linus Torvalds in the United States and other countries.
XFS is a trademark or registered trademark of Hewlett Packard Enterprise Development LP or its subsidiaries in the United States and other countries.
TheOpenStack® Word Mark and OpenStack logo are trademarks or registered trademarks of the Linux Foundation, used under license.
All other trademarks are the property of their respective owners.





