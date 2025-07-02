# 3. Installing Red Hat Ansible Automation Platform
## 3.2. Inventory file examples based on installation scenarios
### 3.2.1. Inventory file recommendations based on installation scenarios




Before selecting your installation method for Ansible Automation Platform, review the following recommendations. Familiarity with these recommendations will streamline the installation process.

- Provide a reachable IP address or fully qualified domain name (FQDN) for hosts to ensure users can sync and install content from automation hub from a different node.

The FQDN must not contain either the `    -` or the `    _` symbols, as it will not be processed correctly.

Do not use `    localhost` .


-  `    admin` is the default user ID for the initial log in to Ansible Automation Platform and cannot be changed in the inventory file.
- Use of special characters for `    pg_password` is limited. The `    !` , `    #` , `    0` and `    @` characters are supported. Use of other special characters can cause the setup to fail.
- Enter your Red Hat Registry Service Account credentials in `    registry_username` and `    registry_password` to link to the Red Hat container registry.
- The inventory file variables `    registry_username` and `    registry_password` are only required if a non-bundle installer is used.


#### 3.2.1.1. Single platform gateway and automation controller with an external (installer managed) database




Use this example to see what is minimally needed within the inventory file to deploy single instances of platform gateway and automation controller with an external (installer managed) database.

```
[automationcontroller]
controller.example.com

[automationgateway]
gateway.example.com

[database]
data.example.com

[all:vars]
admin_password='&lt;password&gt;'
redis_mode=standalone
pg_host='data.example.com'
pg_port=5432
pg_database='awx'
pg_username='awx'
pg_password='&lt;password&gt;'
pg_sslmode='prefer' # set to 'verify-full' for client-side enforced SSL

registry_url='registry.redhat.io'
registry_username='&lt;registry username&gt;'
registry_password='&lt;registry password&gt;'

# Automation Gateway configuration
automationgateway_admin_password=''

automationgateway_pg_host='data.example.com'
automationgateway_pg_port=5432

automationgateway_pg_database='automationgateway'
automationgateway_pg_username='automationgateway'
automationgateway_pg_password=''
automationgateway_pg_sslmode='prefer'

# The main automation gateway URL that clients will connect to (e.g. https://&lt;load balancer host&gt;).
# If not specified, the first node in the [automationgateway] group will be used when needed.
# automationgateway_main_url = ''

# Certificate and key to install in Automation Gateway
# automationgateway_ssl_cert=/path/to/automationgateway.cert
# automationgateway_ssl_key=/path/to/automationgateway.key

# SSL-related variables
# If set, this will install a custom CA certificate to the system trust store.
# custom_ca_cert=/path/to/ca.crt
# Certificate and key to install in nginx for the web UI and API
# web_server_ssl_cert=/path/to/tower.cert
# web_server_ssl_key=/path/to/tower.key
# Server-side SSL settings for PostgreSQL (when we are installing it).
# postgres_use_ssl=False
# postgres_ssl_cert=/path/to/pgsql.crt
# postgres_ssl_key=/path/to/pgsql.key
```

#### 3.2.1.2. Single platform gateway, automation controller, and automation hub with an external (installer managed) database




Use this example to populate the inventory file to deploy single instances of platform gateway, automation controller, and automation hub with an external (installer managed) database.

```
[automationcontroller]
controller.example.com

[automationhub]
automationhub.example.com

[automationgateway]
gateway.example.com

[database]
data.example.com

[all:vars]
admin_password='&lt;password&gt;'
redis_mode=standalone
pg_host='data.example.com'
pg_port='5432'
pg_database='awx'
pg_username='awx'
pg_password='&lt;password&gt;'
pg_sslmode='prefer'  # set to 'verify-full' for client-side enforced SSL

registry_url='registry.redhat.io'
registry_username='&lt;registry username&gt;'
registry_password='&lt;registry password&gt;'

automationhub_admin_password= &lt;PASSWORD&gt;

automationhub_pg_host='data.example.com'
automationhub_pg_port=5432

automationhub_pg_database='automationhub'
automationhub_pg_username='automationhub'
automationhub_pg_password=&lt;PASSWORD&gt;
automationhub_pg_sslmode='prefer'

# The default install will deploy a TLS enabled Automation Hub.
# If for some reason this is not the behavior wanted one can
# disable TLS enabled deployment.
#
# automationhub_disable_https = False
# The default install will generate self-signed certificates for the Automation
# Hub service. If you are providing valid certificate via automationhub_ssl_cert
# and automationhub_ssl_key, one should toggle that value to True.
#
# automationhub_ssl_validate_certs = False
# SSL-related variables
# If set, this will install a custom CA certificate to the system trust store.
# custom_ca_cert=/path/to/ca.crt
# Certificate and key to install in Automation Hub node
# automationhub_ssl_cert=/path/to/automationhub.cert
# automationhub_ssl_key=/path/to/automationhub.key

# Automation Gateway configuration
automationgateway_admin_password=''

automationgateway_pg_host=''
automationgateway_pg_port=5432

automationgateway_pg_database='automationgateway'
automationgateway_pg_username='automationgateway'
automationgateway_pg_password=''
automationgateway_pg_sslmode='prefer'

# The main automation gateway URL that clients will connect to (e.g. https://&lt;load balancer host&gt;).
# If not specified, the first node in the [automationgateway] group will be used when needed.
# automationgateway_main_url = ''

# Certificate and key to install in Automation Gateway
# automationgateway_ssl_cert=/path/to/automationgateway.cert
# automationgateway_ssl_key=/path/to/automationgateway.key

# Certificate and key to install in nginx for the web UI and API
# web_server_ssl_cert=/path/to/tower.cert
# web_server_ssl_key=/path/to/tower.key
# Server-side SSL settings for PostgreSQL (when we are installing it).
# postgres_use_ssl=False
# postgres_ssl_cert=/path/to/pgsql.crt
# postgres_ssl_key=/path/to/pgsql.key
```

#### 3.2.1.3. Single platform gateway, automation controller, automation hub, and Event-Driven Ansible controller with an external (installer managed) database




Use this example to populate the inventory file to deploy single instances of platform gateway, automation controller, automation hub, and Event-Driven Ansible controller with an external (installer managed) database.

Important
- This scenario requires a minimum of automation controller 2.4 for successful deployment of Event-Driven Ansible controller.
- Event-Driven Ansible controller must be installed on a separate server and cannot be installed on the same host as automation hub and automation controller.
- When an Event-Driven Ansible rulebook is activated under standard conditions, it uses approximately 250 MB of memory. However, the actual memory consumption can vary significantly based on the complexity of the rules and the volume and size of the events processed. In scenarios where a large number of events are anticipated or the rulebook complexity is high, conduct a preliminary assessment of resource usage in a staging environment. This ensures that the maximum number of activations is based on the resource capacity. In the following example, the default `    automationedacontroller_max_running_activations` setting is 12, but can be adjusted according to fit capacity.




```
[automationcontroller]
controller.example.com

[automationhub]
automationhub.example.com

[automationedacontroller]
automationedacontroller.example.com

[automationgateway]
gateway.example.com

[database]
data.example.com

[all:vars]
admin_password='&lt;password&gt;'
redis_mode=standalone
pg_host='data.example.com'
pg_port='5432'
pg_database='awx'
pg_username='awx'
pg_password='&lt;password&gt;'
pg_sslmode='prefer'  # set to 'verify-full' for client-side enforced SSL

registry_url='registry.redhat.io'
registry_username='&lt;registry username&gt;'
registry_password='&lt;registry password&gt;'

# Automation hub configuration

automationhub_admin_password= &lt;PASSWORD&gt;

automationhub_pg_host='data.example.com'
automationhub_pg_port=5432

automationhub_pg_database='automationhub'
automationhub_pg_username='automationhub'
automationhub_pg_password=&lt;PASSWORD&gt;
automationhub_pg_sslmode='prefer'

# Automation Event-Driven Ansible controller configuration

automationedacontroller_admin_password='&lt;eda-password&gt;'

automationedacontroller_pg_host='data.example.com'
automationedacontroller_pg_port=5432

automationedacontroller_pg_database='automationedacontroller'
automationedacontroller_pg_username='automationedacontroller'
automationedacontroller_pg_password='&lt;password&gt;'

# Keystore file to install in SSO node
# sso_custom_keystore_file='/path/to/sso.jks'

# This install will deploy SSO with sso_use_https=True
# Keystore password is required for https enabled SSO
sso_keystore_password=''

# This install will deploy a TLS enabled Automation Hub.
# If for some reason this is not the behavior wanted one can
# disable TLS enabled deployment.
#
# automationhub_disable_https = False
# The default install will generate self-signed certificates for the Automation
# Hub service. If you are providing valid certificate via automationhub_ssl_cert
# and automationhub_ssl_key, one should toggle that value to True.
#
# automationhub_ssl_validate_certs = False
# SSL-related variables
# If set, this will install a custom CA certificate to the system trust store.
# custom_ca_cert=/path/to/ca.crt
# Certificate and key to install in Automation Hub node
# automationhub_ssl_cert=/path/to/automationhub.cert
# automationhub_ssl_key=/path/to/automationhub.key

# Automation Gateway configuration
automationgateway_admin_password=''

automationgateway_pg_host=''
automationgateway_pg_port=5432

automationgateway_pg_database='automationgateway'
automationgateway_pg_username='automationgateway'
automationgateway_pg_password=''
automationgateway_pg_sslmode='prefer'

# The main automation gateway URL that clients will connect to (e.g. https://&lt;load balancer host&gt;).
# If not specified, the first node in the [automationgateway] group will be used when needed.
# automationgateway_main_url = ''

# Certificate and key to install in Automation Gateway
# automationgateway_ssl_cert=/path/to/automationgateway.cert
# automationgateway_ssl_key=/path/to/automationgateway.key

# Certificate and key to install in nginx for the web UI and API
# web_server_ssl_cert=/path/to/tower.cert
# web_server_ssl_key=/path/to/tower.key
# Server-side SSL settings for PostgreSQL (when we are installing it).
# postgres_use_ssl=False
# postgres_ssl_cert=/path/to/pgsql.crt
# postgres_ssl_key=/path/to/pgsql.key

# Boolean flag used to verify Automation Controller's
# web certificates when making calls from Automation Event-Driven Ansible controller.
# automationedacontroller_controller_verify_ssl = true
#
# Certificate and key to install in Automation Event-Driven Ansible controller node
# automationedacontroller_ssl_cert=/path/to/automationeda.crt
# automationedacontroller_ssl_key=/path/to/automationeda.key
```

**Additional resources**

For more information about these inventory variables, see [Ansible automation hub variables](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/rpm_installation/appendix-inventory-files-vars#hub-variables) in the _Red Hat Ansible Automation Platform Installation Guide_ .


#### 3.2.1.4. High availability automation hub




Use the following examples to populate the inventory file to install a highly available automation hub. This inventory file includes a highly available automation hub with a clustered setup.

You can configure your HA deployment further to enable a [high availability deployment of automation hub on SELinux](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/rpm_installation/index#proc-install-ha-hub-selinux) .

**Specify database host IP**

- Specify the IP address for your database host, using the `    automation_pg_host` and `    automation_pg_port` inventory variables. For example:


```
automationhub_pg_host='192.0.2.10'
automationhub_pg_port=5432
```

- Also specify the IP address for your database host in the [database] section, using the value in the `    automationhub_pg_host` inventory variable:


```
[database]
192.0.2.10
```

**List all instances in a clustered setup**

- If installing a clustered setup, replace `    localhost ansible_connection=local` in the [automationhub] section with the hostname or IP of all instances. For example:


```
[automationhub]
automationhub1.testing.ansible.com ansible_user=cloud-user
automationhub2.testing.ansible.com ansible_user=cloud-user
automationhub3.testing.ansible.com ansible_user=cloud-user
```

**Next steps**

Check that the following directives are present in `/etc/pulp/settings.py` in each of the private automation hub servers:


```
USE_X_FORWARDED_PORT = True
USE_X_FORWARDED_HOST = True
```

Note
If `automationhub_main_url` is not specified, the first node in the [automationhub] group will be used as default.



#### 3.2.1.5. Enabling a high availability (HA) deployment of automation hub on SELinux




You can configure the inventory file to enable high availability deployment of automation hub on SELinux. You must create two mount points for `/var/lib/pulp` and `/var/lib/pulp/pulpcore_static` , and then assign the appropriate SELinux contexts to each.

Note
You must add the context for `/var/lib/pulp` pulpcore_static and run the Ansible Automation Platform installer before adding the context for `/var/lib/pulp` .



**Prerequisites**

- You have already configured a NFS export on your server.

Note
The NFS share is hosted on an external server and is not a part of high availability automation hub deployment.






**Procedure**

1. Create a mount point at `    /var/lib/pulp` :


```
$ mkdir /var/lib/pulp/
```


1. Open `    /etc/fstab` using a text editor, then add the following values:


```
srv_rhel8:/data /var/lib/pulp nfs defaults,_netdev,nosharecache,context="system_u:object_r:var_lib_t:s0" 0 0    srv_rhel8:/data/pulpcore_static /var/lib/pulp/pulpcore_static nfs defaults,_netdev,nosharecache,context="system_u:object_r:httpd_sys_content_rw_t:s0" 0 0
```


1. Run the reload systemd manager configuration command:


```
$ systemctl daemon-reload
```


1. Run the mount command for `    /var/lib/pulp` :


```
$ mount /var/lib/pulp
```


1. Create a mount point at `    /var/lib/pulp/pulpcore_static` :


```
$ mkdir /var/lib/pulp/pulpcore_static
```


1. Run the mount command:


```
$ mount -a
```


1. With the mount points set up, run the Ansible Automation Platform installer:


```
$ setup.sh -- -b --become-user root
```


1. After the installation is complete, unmount the `    /var/lib/pulp/` mount point.


**Next steps**

1.  [Apply the appropriate SELinux context](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/rpm_installation/index#proc-apply-selinux-context) .
1.  [Configure the pulpcore.serivce](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/rpm_installation/index#proc-configure-pulpcore-service) .


**Additional Resources**

- See the [SELinux Requirements on the Pulp Project documentation](https://docs.pulpproject.org/en/2.16/user-guide/scaling.html#selinux-requirements) for a list of SELinux contexts.
- See the [Filesystem Layout](https://docs.pulpproject.org/pulpcore/installation/hardware-requirements.html#filesystem-layout) for a full description of Pulp folders.


##### 3.2.1.5.1. Configuring pulpcore.service




After you have configured the inventory file, and applied the SELinux context, you now need to configure the pulp service.

**Procedure**

1. With the two mount points set up, shut down the Pulp service to configure `    pulpcore.service` :


```
$ systemctl stop pulpcore.service
```


1. Edit `    pulpcore.service` using `    systemctl` :


```
$ systemctl edit pulpcore.service
```


1. Add the following entry to `    pulpcore.service` to ensure that automation hub services starts only after starting the network and mounting the remote mount points:


```
[Unit]    After=network.target var-lib-pulp.mount
```


1. Enable `    remote-fs.target` :


```
$ systemctl enable remote-fs.target
```


1. Reboot the system:


```
$ systemctl reboot
```




**Troubleshooting**

A bug in the pulpcore SELinux policies can cause the token authentication public/private keys in `etc/pulp/certs/` to not have the proper SELinux labels, causing the pulp process to fail. When this occurs, run the following command to temporarily attach the proper labels:


```
$ chcon system_u:object_r:pulpcore_etc_t:s0 /etc/pulp/certs/token_{private,public}_key.pem
```

Repeat this command to reattach the proper SELinux labels whenever you relabel your system.

##### 3.2.1.5.2. Applying the SELinux context




After you have configured the inventory file, you must now apply the context to enable the high availability (HA) deployment of automation hub on SELinux.

**Procedure**

1. Shut down the Pulp service:


```
$ systemctl stop pulpcore.service
```


1. Unmount `    /var/lib/pulp/pulpcore_static` :


```
$ umount /var/lib/pulp/pulpcore_static
```


1. Unmount `    /var/lib/pulp/` :


```
$ umount /var/lib/pulp/
```


1. Open `    /etc/fstab` using a text editor, then replace the existing value for `    /var/lib/pulp` with the following:


```
srv_rhel8:/data /var/lib/pulp nfs defaults,_netdev,nosharecache,context="system_u:object_r:pulpcore_var_lib_t:s0" 0 0
```


1. Run the mount command:


```
$ mount -a
```




#### 3.2.1.6. Configuring content signing on private automation hub




To successfully sign and publish Ansible Certified Content Collections, you must configure private automation hub for signing.

**Prerequisites**

- Your GnuPG key pairs have been securely set up and managed by your organization.
- Your public-private key pair has proper access for configuring content signing on private automation hub.


**Procedure**

1. Create a signing script that accepts only a filename.

Note
This script acts as the signing service and must generate an ascii-armored detached `    gpg` signature for that file using the key specified through the `    PULP_SIGNING_KEY_FINGERPRINT` environment variable.



The script prints out a JSON structure with the following format.


```
{"file": "filename", "signature": "filename.asc"}
```

All the file names are relative paths inside the current working directory. The file name must remain the same for the detached signature.

**Example:**

The following script produces signatures for content:



```
#!/usr/bin/env bash        FILE_PATH=$1    SIGNATURE_PATH="$1.asc"        ADMIN_ID="$PULP_SIGNING_KEY_FINGERPRINT"    PASSWORD="password"        # Create a detached signature    gpg --quiet --batch --pinentry-mode loopback --yes --passphrase \       $PASSWORD --homedir ~/.gnupg/ --detach-sign --default-key $ADMIN_ID \       --armor --output $SIGNATURE_PATH $FILE_PATH        # Check the exit status    STATUS=$?    if [ $STATUS -eq 0 ]; then       echo {\"file\": \"$FILE_PATH\", \"signature\": \"$SIGNATURE_PATH\"}    else       exit $STATUS    fi
```

After you deploy a private automation hub with signing enabled to your Ansible Automation Platform cluster, new UI additions are displayed in collections.


1. Review the Ansible Automation Platform installer inventory file for options that begin with `    automationhub_*` .


```
[all:vars]    .    .    .    automationhub_create_default_collection_signing_service = True    automationhub_auto_sign_collections = True    automationhub_require_content_approval = True    automationhub_collection_signing_service_key = /abs/path/to/galaxy_signing_service.gpg    automationhub_collection_signing_service_script = /abs/path/to/collection_signing.sh
```

The two new keys ( **automationhub_auto_sign_collections** and **automationhub_require_content_approval** ) indicate that the collections must be signed and approved after they are uploaded to private automation hub.




#### 3.2.1.7. Adding a safe plugin variable to Event-Driven Ansible controller




When using `redhat.insights_eda` or similar plugins to run rulebook activations in Event-Driven Ansible controller, you must add a safe plugin variable to a directory in Ansible Automation Platform. This ensures connection between Event-Driven Ansible controller and the source plugin, and displays port mappings correctly.

**Procedure**

1. Create a directory for the safe plugin variable: `    mkdir -p ./group_vars/automationedacontroller`
1. Create a file within that directory for your new setting (for example, `    touch ./group_vars/automationedacontroller/custom.yml` )
1. Add the variable `    automationedacontroller_additional_settings` to extend the default `    settings.yaml` template for Event-Driven Ansible controller and add the `    SAFE_PLUGINS` field with a list of plugins to enable. For example:


```
automationedacontroller_additional_settings:       SAFE_PLUGINS:         - ansible.eda.webhook         - ansible.eda.alertmanager
```

Note
You can also extend the `    automationedacontroller_additional_settings` variable beyond `    SAFE_PLUGINS` in the Django configuration file `    /etc/ansible-automation-platform/eda/settings.yaml` .






