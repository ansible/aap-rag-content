# 2. Hardening Ansible Automation Platform
## 2.1. Planning considerations
### 2.1.3. Credential management planning for Ansible Automation Platform




Red Hat Ansible Automation Platform uses credentials to authenticate requests to jobs against machines, synchronize with inventory sources, and import project content from a version control system.

Automation controller manages three sets of secrets:

- User passwords for **local Ansible Automation Platform users** .
- Secrets for Ansible Automation Platform **operational use** (database password, message bus password, and so on).
- Secrets for **automation use** (SSH keys, cloud credentials, external password vault credentials, and so on).


Implementing a privileged access or credential management solution to protect credentials from compromise is a highly recommended practice. Organizations should audit the use of, and provide additional programmatic control over, access and privilege escalation.

You can further secure automation credentials by ensuring they are unique and stored only in automation controller. Services such as OpenSSH can be configured to allow credentials on connections only from specific addresses. Use different credentials for automation from those used by system administrators to log in to a server. Although direct access should be limited where possible, it can be used for disaster recovery or other ad hoc management purposes, allowing for easier auditing.

Different automation jobs might need to access a system at different levels. For example, you can have low-level system automation that applies patches and performs security baseline checking, while a higher-level piece of automation deploys applications. By using different keys or credentials for each piece of automation, the effect of any one key vulnerability is minimized. This also allows for easy baseline auditing.

#### 2.1.3.1. Ansible Automation Platform operational secrets




Ansible Automation Platform uses several secrets (passwords, keys, and so on) operationally. These secrets are stored unencrypted on the various Ansible Automation Platform servers, as each component service must read them at startup.

All files are protected by UNIX permissions, and restricted to the root user or the appropriate service account user. These files should be routinely monitored to ensure there has been no unauthorized access or modification.

##### 2.1.3.1.1. RPM-based installation secrets




The following table provides the location of these secrets for RPM-based installs of Ansible Automation Platform.


<span id="idm139994922965296"></span>
**Table 2.1. Ansible Automation Platform operational secrets**

|  **Automation controller secrets** |
| --- |
|  **File path** |  **Description** |
|  `/etc/tower/SECRET_KEY` | A secret key used for encrypting automation secrets in the database. If the `SECRET_KEY` changes or is unknown, no encrypted fields in the database will be accessible. |
|  `/etc/tower/tower.cert`

`/etc/tower/tower.key` | SSL/TLS certificate and key for the automation controller web service.

A self-signed `cert/key` is installed by default; you can provide a locally appropriate certificate and key.

For more information, see [Installing with user-provided PKI certificates](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/hardening_and_compliance/hardening-aap#proc-install-user-pki_hardening-aap) . |
|  `/etc/tower/conf.d/postgres.py` | Contains the password used by automation controller to connect to the database, unless TLS authentication is used for the database connection. |
|  `/etc/tower/conf.d/channels.py` | Contains the secret used by automation controller for WebSocket broadcasts. |
|  `/etc/tower/conf.d/gateway.py` | Contains the key used by automation controller to sync state with the platform gateway. |
|  **Platform gateway secrets** |
|  **File path** |  **Description** |
|  `/etc/ansible-automation-platform/gateway/SECRET_KEY` | A secret key used for encrypting automation secrets in the database. If the `SECRET_KEY changes` or is unknown, the platform gateway cannot access the encrypted secrets in the database. |
|  `/etc/ansible-automation-platform/gateway/gateway.cert` | SSL/TLS certificate for the platform gateway web service.

A self-signed certificate is installed by default, although a user-provided certificate and key pair can be used.

For more information, see [Installing with user-provided PKI certificates](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/hardening_and_compliance/hardening-aap#proc-install-user-pki_hardening-aap) . |
|  `/etc/ansible-automation-platform/gateway/gateway.key` | SSL/TLS key for the platform gateway web service.

A self-signed certificate is installed by default, although a user-provided certificate and key pair can be used.

For more information, see [Installing with user-provided PKI certificates](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/hardening_and_compliance/hardening-aap#proc-install-user-pki_hardening-aap) . |
|  `/etc/ansible-automation-platform/gateway/cache.cert` | SSL/TLS certificate used for mutual TLS (mTLS) authentication with the Redis cache used by the platform gateway. |
|  `/etc/ansible-automation-platform/gateway/cache.key` | SSL/TLS key used for mutual TLS (mTLS) authentication with the Redis cache used by the platform gateway. |
|  `/etc/ansible-automation-platform/gateway/settings.py` | Contains the password used by the platform gateway to connect to the database, unless TLS authentication is used for the database connection. Also contains the password used to connect to the Redis cache used by the platform gateway. |
|  **Automation hub secrets** |
|  **File path** |  **Description** |
|  `/etc/pulp/settings.py` | Contains the password used by automation hub to connect to the database, unless TLS authentication is used for the database connection. Contains the Django secret key used by the automation hub web service. |
|  `/etc/pulp/certs/token_public_key.pem` | OpenSSL public key in PEM format for the automation hub EE token authentication. It is generated by default from the `token_private_key.pem` file. |
|  `/etc/pulp/certs/token_private_key.pem` | OpenSSL private key in PEM format for the automation hub EE token authentication. It is generated by default, although a user can provide their own private key with the `pulp_token_auth_key`` installation inventory variable. |
|  `/etc/pulp/certs/pulp_webserver.crt` | SSL/TLS certificate for the automation hub web service.

A self-signed certificate is installed by default, although a user-provided certificate and key pair can be used.

For more information, see [Installing with user-provided PKI certificates](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/hardening_and_compliance/hardening-aap#proc-install-user-pki_hardening-aap) . |
|  `/etc/pulp/certs/pulp_webserver.key` | SSL/TLS key for the automation hub web service.

A self-signed certificate is installed by default, although a user-provided certificate and key pair can be used.

For more information, see [Installing with user-provided PKI certificates](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/hardening_and_compliance/hardening-aap#proc-install-user-pki_hardening-aap) . |
|  `/etc/pulp/certs/database_fields.symmetric.key` | A key used for encrypting sensitive fields in the automation hub database table.

If the key changes or is unknown, automation hub cannot access the encrypted fields in the database. |
|  **Event-Driven Ansible secrets** |
|  **File path** |  **Description** |
|  `/etc/ansible-automation-platform/eda/SECRET_KEY` | A secret key used for encrypting fields in the Event-Driven Ansible controller database table.

If the SECRET_KEY changes or is unknown, the Event-Driven Ansible controller cannot access the encrypted fields in the database. |
|  `/etc/ansible-automation-platform/eda/settings.yaml` | Contains the password used by the Event-Driven Ansible gateway to connect to the database, unless TLS authentication is used for the database connection.

Contains the password used to connect to the Redis cache used by the Event-Driven Ansible controller.

Contains the key used by the Event-Driven Ansible controller to sync state with the platform gateway. |
|  `/etc/ansible-automation-platform/eda/server.cert` | SSL/TLS certificate for the Event-Driven Ansible controller web service.

A self-signed certificate is installed by default, although a user-provided certificate and key pair can be used.

For more information, see [Installing with user-provided PKI certificates](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/hardening_and_compliance/hardening-aap#proc-install-user-pki_hardening-aap) . |
|  `/etc/ansible-automation-platform/eda/server.key` | SSL/TLS key for the Event-Driven Ansible controller web service.

A self-signed certificate is installed by default, although a user-provided certificate and key pair can be used.

For more information, see [Installing with user-provided PKI certificates](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/hardening_and_compliance/hardening-aap#proc-install-user-pki_hardening-aap) . |
|  `/etc/ansible-automation-platform/eda/cache.cert` | SSL/TLS certificate used for mutual TLS (mTLS) authentication with the Redis cache used by the Event-Driven Ansible controller |
|  `/etc/ansible-automation-platform/eda/cache.key` | SSL/TLS key used for mutual TLS (mTLS) authentication with the Redis cache used by the Event-Driven Ansible controller |
|  `/etc/ansible-automation-platform/eda/websocket.cert` | SSL/TLS certificate for the Event-Driven Ansible controller WebSocket endpoint.

A self-signed certificate is installed by default, although a user-provided certificate and key pair can be used.

For more information, see [Installing with user-provided PKI certificates](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/hardening_and_compliance/hardening-aap#proc-install-user-pki_hardening-aap) . |
|  `/etc/ansible-automation-platform/eda/websocket.key` | SSL/TLS key for the Event-Driven Ansible controller WebSocket endpoint.

A self-signed certificate is installed by default, although a user-provided certificate and key pair can be used.

For more information, see [Installing with user-provided PKI certificates](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/hardening_and_compliance/hardening-aap#proc-install-user-pki_hardening-aap) . |
|  **Redis secrets** |
|  **File path** |  **Description** |
|  `/etc/ansible-automation-platform/ca/ansible-automation-platform-managed-ca-cert.crt` | SSL/TLS certificate for the internal self-signed certificate authority used by the installation program to generate the default self-signed certificates for each component service. |
|  `/etc/ansible-automation-platform/ca/ansible-automation-platform-managed-ca-cert.key` | SSL/TLS key for the internal self-signed certificate authority used by the installation program to generate the default self-signed certificates for each component service. |




Note
Some of these file locations reflect the previous product name of automation controller, formerly named Ansible Tower.



##### 2.1.3.1.2. Container-based installation secrets




The secrets listed for RPM-based installations are also used in container-based installations, but they are stored in a different manner. Container-based installations of Red Hat Ansible Automation Platform use Podman secrets to store operational secrets. These secrets can be listed using the `podman secret list` command.

By default, Podman stores data in the home directory of the user who installed and runs the containerized Red Hat Ansible Automation Platform services. Podman secrets are stored in the file `$HOME/.local/share/containers/storage/secrets/filedriver/secretsdata.json` as base64-encoded strings, so while they are not in plain text the values are only obfuscated.

The data stored in a Podman secret can be shown using the command `podman secret inspect --showsecret &lt;secret&gt;` .

This file should be routinely monitored to ensure there has been no unauthorized access or modification.

#### 2.1.3.2. Automation use secrets




Automation controller stores a variety of secrets in the database that are either used for automation or are a result of automation. Automation use secrets include:

- All secret fields of all credential types (passwords, secret keys, authentication tokens, secret cloud credentials).
- Secret tokens and passwords for external services defined in automation controller settings.
- “password” type survey field entries.


You can grant users and teams the ability to use these credentials without actually exposing the credential to the user. This means that if a user moves to a different team or leaves the organization, you do not have to re-key all of your systems.

Automation controller uses SSH (or the Windows equivalent) to connect to remote hosts. To pass the key from automation controller to SSH, the key must be decrypted before it can be written to a named pipe. Automation controller then uses that pipe to send the key to SSH (so that it is never written to disk). If passwords are used, automation controller handles those by responding directly to the password prompt and decrypting the password before writing it to the prompt.

As an administrator with superuser access, you can define a custom credential type in a standard format by using a YAML/JSON-like definition. This allows the assignment of new credential types to jobs and inventory updates. This, in turn, lets you to define a custom credential type that works in ways similar to existing credential types. For example, you can create a custom credential type that injects an API token for a third-party web service into an environment variable. Your playbook or custom inventory script can then consume this.

To encrypt secret fields, Ansible Automation Platform uses the _Advanced Encryption Standard_ (AES) in _Cipher Block Chaining_ (CBC) mode with a 256-bit key for encryption, _Public-Key cryptography Standard_ (PKCS7) padding, and _Hash-Based Message Authentication Code_ (HMAC) using SHA256 for authentication. The encryption and decryption processes derive the AES-256 bit encryption key from the `SECRET_KEY` , the field name of the model field, and the database-assigned auto-incremented record ID. Thus, if any attribute used in the key generation process changes, Ansible Automation Platform fails to correctly decrypt the secret. Ansible Automation Platform is designed such that the `SECRET_KEY` is never readable in playbooks Ansible Automation Platform launches. This means that these secrets are never readable by Ansible Automation Platform users, and no secret field values are ever made available through the Ansible Automation Platform REST API. If a secret value is used in a playbook, you must use `no_log` on the task so that it is not accidentally logged.

#### 2.1.3.3. Protecting sensitive data with no_log




If you save Ansible output to a log, you expose any secret data in your Ansible output, such as passwords and usernames. To keep sensitive values out of your logs, mark tasks that expose them with the `no_log: True` attribute.

However, the `no_log` attribute does not affect debugging output, so be careful not to debug playbooks in a production environment.

