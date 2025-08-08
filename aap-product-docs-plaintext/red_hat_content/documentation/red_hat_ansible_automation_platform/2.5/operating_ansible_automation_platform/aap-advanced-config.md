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

To customize settings in container-based installation deployments, you can use the `extra_settings` parameter to ensure that customizations persist through installer updates. For more information, see [Inventory file variables](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/containerized_installation/appendix-inventory-files-vars) in the Containerized installation guide.

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




The platform gateway utilizes the Dynaconf library for managing its application settings. Dynaconf follows a layered configuration approach, where settings are loaded from multiple sources in a defined order, with later sources overriding earlier ones. Ansible Automation Platform loads settings in the following sequence:

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

- For more information, see the [Red Hat privacy policy](https://www.redhat.com/en/about/privacy-policy) .


### 5.1.1. Controlling data collection from automation controller




You can control how automation controller collects data from theSettings→Automation Execution→Systemmenu.

**Procedure**

1. Log in to your automation controller.
1. From the navigation panel, selectSettings→Automation Execution→System.
1. Select **Gather data for Automation Analytics** to enable automation controller to gather data on automation and send it to Automation Analytics.


# Chapter 6. Renewing and changing the SSL certificate




If your current SSL certificate has expired or will expire soon, you can either renew or replace the SSL certificate used by Ansible Automation Platform.

You must renew the SSL certificate if you need to regenerate the SSL certificate with new information such as new hosts.

You must replace the SSL certificate if you want to use an SSL certificate signed by an internal certificate authority.

## 6.1. Renewing the self-signed SSL certificate




The following steps regenerate a new SSL certificate for both automation controller and automation hub.

**Procedure**

1. Add `    aap_service_regen_cert=true` to the inventory file in the `    [all:vars]` section:


```
[all:vars]    aap_service_regen_cert=true
```


1. Run the installer.


**Verification**

- Validate the CA file and `    server.crt` file on automation controller:


```
openssl verify -CAfile ansible-automation-platform-managed-ca-cert.crt /etc/tower/tower.cert    openssl s_client -connect &lt;AUTOMATION_HUB_URL&gt;:443
```


- Validate the CA file and `    server.crt` file on automation hub:


```
openssl verify -CAfile ansible-automation-platform-managed-ca-cert.crt /etc/pulp/certs/pulp_webserver.crt    openssl s_client -connect &lt;AUTOMATION_CONTROLLER_URL&gt;:443
```




## 6.2. Changing SSL certificates




To change the SSL certificate, you can edit the inventory file and run the installation program. The installation program verifies that all Ansible Automation Platform components are working. The installation program can take a long time to run.

Alternatively, you can change the SSL certificates manually. This is quicker, but there is no automatic verification.

Red Hat recommends that you use the installation program to make changes to your Ansible Automation Platform instance.

### 6.2.1. Prerequisites




- If there is an intermediate certificate authority, you must append it to the server certificate.
- Both automation controller and automation hub use NGINX so the server certificate must be in PEM format.
- Use the correct order for the certificates: The server certificate comes first, followed by the intermediate certificate authority.


For further information, see the [ssl certificate section of the NGINX documentation](http://nginx.org/en/docs/http/ngx_http_ssl_module.html#ssl_certificate) .

### 6.2.2. Changing the SSL certificate and key using the installer




The following procedure describes how to change the SSL certificate and key in the inventory file.

**Procedure**

1. Copy the new SSL certificates and keys to a path relative to the Ansible Automation Platform installer.
1. Add the absolute paths of the SSL certificates and keys to the inventory file. Refer to the [Automation controller variables](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/rpm_installation/appendix-inventory-files-vars#controller-variables) , [Automation hub variables](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/rpm_installation/appendix-inventory-files-vars#hub-variables) , and [Event-Driven Ansible controller variables](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/rpm_installation/appendix-inventory-files-vars#event-driven-ansible-variables) sections of [RPM installation](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/rpm_installation) for guidance on setting these variables.


- Automation controller: `        web_server_ssl_cert` , `        web_server_ssl_key` , `        custom_ca_cert`
- Automation hub: `        automationhub_ssl_cert` , `        automationhub_ssl_key` , `        custom_ca_cert`
- Event-Driven Ansible controller: `        automationedacontroller_ssl_cert` , `        automationedacontroller_ssl_key` , `        custom_ca_cert`

Note
The `    custom_ca_cert` must be the root certificate authority that signed the intermediate certificate authority. This file is installed in `    /etc/pki/ca-trust/source/anchors` .




1. Run the installation program.


#### 6.2.2.1. Changing the SSL certificate and key manually on automation controller




The following procedure describes how to change the SSL certificate and key manually on automation controller.

**Procedure**

1. Backup the current SSL certificate:


```
cp /etc/tower/tower.cert /etc/tower/tower.cert-$(date +%F)
```


1. Backup the current key files:


```
cp /etc/tower/tower.key /etc/tower/tower.key-$(date +%F)+
```


1. Copy the new SSL certificate to `    /etc/tower/tower.cert` .
1. Copy the new key to `    /etc/tower/tower.key` .
1. Restore the SELinux context:


```
restorecon -v /etc/tower/tower.cert /etc/tower/tower.key
```


1. Set appropriate permissions for the certificate and key files:


```
chown root:awx /etc/tower/tower.cert /etc/tower/tower.key    chmod 0600 /etc/tower/tower.cert /etc/tower/tower.key
```


1. Test the NGINX configuration:


```
nginx -t
```


1. Reload NGINX:


```
systemctl reload nginx.service
```


1. Verify that new SSL certificate and key have been installed:


```
true | openssl s_client -showcerts -connect ${CONTROLLER_FQDN}:443
```




#### 6.2.2.2. Changing the SSL certificate and key on automation controller on OpenShift Container Platform




The following procedure describes how to change the SSL certificate and key for automation controller running on OpenShift Container Platform.

**Procedure**

1. Copy the signed SSL certificate and key to a secure location.
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
1. Verify that new SSL certificate and key have been installed:


```
true | openssl s_client -showcerts -connect ${CONTROLLER_FQDN}:443
```




#### 6.2.2.3. Changing the SSL certificate and key for automation hub on OpenShift Container Platform




The following procedure describes how to change the SSL certificate and key for automation hub running on OpenShift Container Platform.

**Procedure**

1. Copy the signed SSL certificate and key to a secure location.
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
1. Verify that new SSL certificate and key have been installed:


```
true | openssl s_client -showcerts -connect ${CONTROLLER_FQDN}:443
```




#### 6.2.2.4. Changing the SSL certificate and key on Event-Driven Ansible controller




The following procedure describes how to change the SSL certificate and key manually on Event-Driven Ansible controller.

**Procedure**

1. Backup the current SSL certificate:


```
cp /etc/ansible-automation-platform/eda/server.cert /etc/ansible-automation-platform/eda/server.cert-$(date +%F)
```


1. Backup the current key files:


```
cp /etc/ansible-automation-platform/eda/server.key /etc/ansible-automation-platform/eda/server.key-$(date +%F)
```


1. Copy the new SSL certificate to `    /etc/ansible-automation-platform/eda/server.cert` .
1. Copy the new key to `    /etc/ansible-automation-platform/eda/server.key` .
1. Restore the SELinux context:


```
restorecon -v /etc/ansible-automation-platform/eda/server.cert /etc/ansible-automation-platform/eda/server.key
```


1. Set appropriate permissions for the certificate and key files:


```
chown root:eda /etc/ansible-automation-platform/eda/server.cert /etc/ansible-automation-platform/eda/server.key
```


```
chmod 0600 /etc/ansible-automation-platform/eda/server.cert /etc/ansible-automation-platform/eda/server.key
```


1. Test the NGINX configuration:


```
nginx -t
```


1. Reload NGINX:


```
systemctl reload nginx.service
```


1. Verify that new SSL certificate and key have been installed:


```
true | openssl s_client -showcerts -connect ${CONTROLLER_FQDN}:443
```




#### 6.2.2.5. Changing the SSL certificate and key manually on automation hub




The following procedure describes how to change the SSL certificate and key manually on automation hub.

**Procedure**

1. Backup the current SSL certificate:


```
cp /etc/pulp/certs/pulp_webserver.crt /etc/pulp/certs/pulp_webserver.crt-$(date +%F)
```


1. Backup the current key files:


```
cp /etc/pulp/certs/pulp_webserver.key /etc/pulp/certs/pulp_webserver.key-$(date +%F)
```


1. Copy the new SSL certificate to `    /etc/pulp/certs/pulp_webserver.crt` .
1. Copy the new key to `    /etc/pulp/certs/pulp_webserver.key` .
1. Restore the SELinux context:


```
restorecon -v /etc/pulp/certs/pulp_webserver.crt /etc/pulp/certs/pulp_webserver.key
```


1. Set appropriate permissions for the certificate and key files:


```
chown root:pulp /etc/pulp/certs/pulp_webserver.crt /etc/pulp/certs/pulp_webserver.key
```


```
chmod 0600 /etc/pulp/certs/pulp_webserver.crt /etc/pulp/certs/pulp_webserver.key
```


1. Test the NGINX configuration:


```
nginx -t
```


1. Reload NGINX:


```
systemctl reload nginx.service
```


1. Verify that new SSL certificate and key have been installed:


```
true | openssl s_client -showcerts -connect ${CONTROLLER_FQDN}:443
```





<span id="idm140184329121568"></span>
# Legal Notice

Copyright© 2025 Red Hat, Inc.
The text of and illustrations in this document are licensed by Red Hat under a Creative Commons Attribution–Share Alike 3.0 Unported license ("CC-BY-SA"). An explanation of CC-BY-SA is available at [http://creativecommons.org/licenses/by-sa/3.0/](http://creativecommons.org/licenses/by-sa/3.0/) . In accordance with CC-BY-SA, if you distribute this document or an adaptation of it, you must provide the URL for the original version.
Red Hat, as the licensor of this document, waives the right to enforce, and agrees not to assert, Section 4d of CC-BY-SA to the fullest extent permitted by applicable law.
Red Hat, Red Hat Enterprise Linux, the Shadowman logo, the Red Hat logo, JBoss, OpenShift, Fedora, the Infinity logo, and RHCE are trademarks of Red Hat, Inc., registered in the United States and other countries.
Linux® is the registered trademark of Linus Torvalds in the United States and other countries.
Java® is a registered trademark of Oracle and/or its affiliates.
XFS® is a trademark of Silicon Graphics International Corp. or its subsidiaries in the United States and/or other countries.
MySQL® is a registered trademark of MySQL AB in the United States, the European Union and other countries.
Node.js® is an official trademark of Joyent. Red Hat is not formally related to or endorsed by the official Joyent Node.js open source or commercial project.
TheOpenStack® Word Mark and OpenStack logo are either registered trademarks/service marks or trademarks/service marks of the OpenStack Foundation, in the United States and other countries and are used with the OpenStack Foundation's permission. We are not affiliated with, endorsed or sponsored by the OpenStack Foundation, or the OpenStack community.
All other trademarks are the property of their respective owners.





