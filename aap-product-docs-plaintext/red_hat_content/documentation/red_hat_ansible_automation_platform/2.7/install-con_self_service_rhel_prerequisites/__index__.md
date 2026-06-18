# Prerequisites for deploying Ansible automation portal on RHEL

Before you deploy an Ansible automation portal RHEL appliance, verify that your environment meets the system, network, and access requirements.

## System requirements

*Table 1. System requirements for Ansible automation portal RHEL appliances*

| Resource         | Minimum                                   | Recommended |
| ---------------- | ----------------------------------------- | ----------- |
| CPU              | 4 vCPU                                    | 6 vCPU      |
| Memory           | 16 GB                                     | 24 GB       |
| Disk space       | 40 GB                                     | 60 GB       |
| Architecture     | AMD64/x86\_64                             | --          |
| Operating system | RHEL 9.6 or later (included in appliance) | RHEL 9.7    |


The recommended values include headroom for the built-in database. For production deployments, use an external PostgreSQL database. The built-in database is suitable for evaluation and small environments.

## Network requirements

The following table lists the default ports used by the Ansible automation portal RHEL appliance. The HTTPS port is configurable after deployment.

*Table 2. Default ports for Ansible automation portal RHEL appliances*

| Direction | Port          | Protocol | Purpose                                                                                    |
| --------- | ------------- | -------- | ------------------------------------------------------------------------------------------ |
| Inbound   | 443 (default) | HTTPS    | User access to Ansible automation portal                                                   |
| Inbound   | 22            | SSH      | Administrator access to the appliance                                                      |
| Outbound  | 443           | HTTPS    | Communication with the Ansible Automation Platform instance                                |
| Outbound  | 443           | HTTPS    | Image pulls from `registry.redhat.io` (upgrades only, not required with a mirror registry) |


Port 5432 (PostgreSQL) is used internally between containers and is not exposed to the network.

## Required access

- An Ansible Automation Platform 2.5 or later instance with administrator privileges.
- An active Red Hat Ansible Automation Platform subscription.
- An active RHEL subscription (for the KVM host, if applicable).
- The pre-built QCOW2 or VMDK appliance image, available from the Red Hat Ansible Automation Platform downloads page.
- An SSH key pair for appliance access.

## Create an OAuth application in Ansible Automation Platform

Before deploying the appliance, create an OAuth 2.0 application in Ansible Automation Platform. The Ansible automation portal uses this application to authenticate users through Ansible Automation Platform.

1. Log in to Ansible Automation Platform as an administrator.
2. Navigate to **Access Management** > **OAuth Applications**.
3. Click **Create OAuth Application** and set the following values:
| Field                        | Value                                                                     |
| ---------------------------- | ------------------------------------------------------------------------- |
| **Name**                     | `automation-portal`                                                       |
| **Authorization grant type** | Authorization code                                                        |
| **Redirect URIs**            | `https://placeholder.example.com` (you will update this after deployment) |
| **Client type**              | Confidential                                                              |

4. Click **Save**.
5. Note the **Client ID** and **Client Secret** values. You need these for the cloud-init configuration.

## Generate an API token

Generate a personal access token for an Ansible Automation Platform administrator. The Ansible automation portal uses this token to synchronize job templates from Ansible Automation Platform.

1. Navigate to **Access Management** > **Users** and select your administrator account.
2. Click **Tokens** > **Create Token**.
3. Set the **Scope** to **Write**.
4. Click **Save** and note the token value. You need this for the cloud-init configuration.


Optional: If you want to import custom templates from private GitHub or GitLab repositories, create a personal access token for each service before you begin. You provide these tokens in the cloud-init configuration.

## Prepare the cloud-init configuration

The appliance uses cloud-init to apply your configuration at first boot. Cloud-init is a standard tool for automating the initial setup of virtual machines. It creates user accounts, injects SSH keys, and runs custom configuration scripts. The appliance extends cloud-init with custom fields for Ansible Automation Platform credentials and database settings.

Create a cloud-init user-data file with your SSH keys and Ansible Automation Platform credentials.

The following four Ansible Automation Platform fields are required. Without them, Ansible automation portal services do not start:

- `aap.host_url`
- `aap.token`
- `aap.oauth.client_id`
- `aap.oauth.client_secret`


SSH keys are required for access. The appliance has no default password.

All other fields are optional. The Ansible automation portal RHEL appliance auto-generates passwords for the default built-in database deployed during initial installation, backend secrets, and a user-accessible URL if you omit them.

Tip:

Keep quotation marks around SSH public keys in the cloud-init user-data file.

## Minimal cloud-init template

Replace the placeholder values in angle brackets. All other values auto-generate at first boot.

```yaml
#cloud-config

users:
- name: <username>
sudo: ALL=(ALL) NOPASSWD:ALL
ssh_authorized_keys:
- "<your-ssh-public-key>"

aap:
host_url: "https://<aap-host>"
token: "<aap-api-token>"
oauth:
client_id: "<oauth-client-id>"
client_secret: "<oauth-client-secret>"

database:
type: builtin
builtin:
password: "auto"
admin_password: "auto"
```

## Full cloud-init template

This template includes all supported fields. Replace values marked with angle brackets. Remove or leave optional sections as-is.

```yaml
#cloud-config

users:
- name: <username>
sudo: ALL=(ALL) NOPASSWD:ALL
ssh_authorized_keys:
- "<your-ssh-public-key>"

aap:
host_url: "https://<aap-host>"
token: "<aap-api-token>"
check_ssl: true
oauth:
client_id: "<oauth-client-id>"
client_secret: "<oauth-client-secret>"

database:
type: builtin
builtin:
password: "auto"
admin_password: "auto"

security:
backend_secret: "auto"

network:
port: 443
base_url: "https://portal.example.com"

integrations:
github:
url: "github.com"
token: "<github-personal-access-token>"
gitlab:
url: "gitlab.com"
token: "<gitlab-personal-access-token>"
```


- **`aap.check_ssl`** -- Set to `false` if your Ansible Automation Platform instance uses a self-signed certificate.
- **`network.base_url`** -- Set this when users access the Ansible automation portal RHEL appliance through a hostname, route, or load balancer. If omitted, the user-accessible URL is auto-detected from the VM IP address.
- **`network.port`** -- The HTTPS listen port. Default is `443`. If you are using the standard port 443, you do not need to specify the port. If you set a custom port, you must also open that port on any firewall and, for Red Hat OpenShift Virtualization deployments, update the Red Hat OpenShift Container Platform route to use the custom port.
- **`integrations`** -- Optional. Only required if you need to import custom templates from private GitHub or GitLab repositories. Public repository access does not require a token.

## External database cloud-init template

To connect to an existing PostgreSQL database instead of the built-in one, use the following `database` section:

```yaml
database:
type: external
external:
host: "<database-host>"
port: 5432
name: "portal_db"
user: "<database-user>"
password: "<database-password>"
ssl: true
```
The database user requires the `CREATEDB` privilege.

Save the cloud-init user-data file. You will use it during the platform-specific installation procedure.
