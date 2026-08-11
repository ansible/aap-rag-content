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

| Direction | Port          | Protocol | Purpose                                                                                   |
| --------- | ------------- | -------- | ----------------------------------------------------------------------------------------- |
| Inbound   | 443 (default) | HTTPS    | User access to Ansible automation portal                                                  |
| Inbound   | 22            | SSH      | Administrator access to the appliance                                                     |
| Outbound  | 443           | HTTPS    | Communication with the Ansible Automation Platform instance                               |
| Outbound  | 443           | HTTPS    | Image pulls from`registry.redhat.io` (upgrades only, not required with a mirror registry) |

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
| Field                        | Value                                                                         |
| ---------------------------- | ----------------------------------------------------------------------------- |
| **Name**                     | A descriptive name for your OAuth application, for example`automation-portal` |
| **Authorization grant type** | Authorization code                                                            |
| **Redirect URIs**            | `https://placeholder.example.com` (you will update this after deployment)     |
| **Client type**              | Confidential                                                                  |

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

The appliance uses cloud-init to apply your configuration at first boot. Cloud-init creates user accounts, injects SSH keys, and runs custom configuration scripts. The appliance extends cloud-init with custom fields for Ansible Automation Platform credentials.

Create two files before you install the appliance:

- `user-data` -- SSH access and Ansible Automation Platform registration
- `meta-data` -- instance identity for cloud-init

The following four Ansible Automation Platform fields are required in `user-data`. Without them, Ansible automation portal services do not start:

- `aap.host_url`
- `aap.token`
- `aap.oauth.client_id`
- `aap.oauth.client_secret`

SSH keys are required for access. The appliance has no default password.

The Ansible automation portal RHEL appliance auto-generates passwords for the built-in database, backend secrets, and user-accessible URL when you omit those fields.

Tip:

Keep quotation marks around SSH public keys in the `user-data` file.

## Create the user-data file

Replace the placeholder values in angle brackets.

```yaml
#cloud-config
users:
- name: admin
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
```

- Set `aap.check_ssl` to `false` if your Ansible Automation Platform instance uses a self-signed certificate.
- To enable execution environment builder at first boot, add an `integrations` section to `user-data`. See the Cloud-init reference and Understand execution environment builder topics in the related links below.

## Create the meta-data file

Create a file named `meta-data` in the same directory as `user-data`:

```yaml
instance-id: portal-01
local-hostname: portal
```

- Set `instance-id` to a unique value for each deployment.
- Set `local-hostname` to the hostname for the appliance.
- To reapply cloud-init configuration on an existing virtual machine, change `instance-id` to a new unique value (for example, increment `portal-01` to `portal-02`) before redeploying. See the Cloud-init reference topic in the related links below for optional fields and re-run behavior.

## Validate configuration files

After you create `user-data` and `meta-data`, validate syntax before you continue to an install guide.

**Option A -- Python:**

```terminal
$ python3 -c "import yaml; yaml.safe_load(open('user-data')); print('Valid YAML')"
$ python3 -c "import yaml; yaml.safe_load(open('meta-data')); print('Valid YAML')"
```

**Option B -- yamllint:**

```terminal
$ yamllint user-data
$ yamllint meta-data
```

Expected: `Valid YAML` (Python) or no errors (yamllint). Fix invalid YAML before you build an ISO or encode files for delivery.

For **Install Ansible automation portal on Red Hat OpenShift Virtualization**, validate `user-data` only.

## Next steps

Save `user-data` and `meta-data`. Continue in the install guide for your platform. See the related links below for the three platform install guides.

Each install guide includes steps to deliver configuration to the virtual machine.

If you deploy without configuration, redeploy the virtual machine with cloud-init from this page and your platform install guide. Do not configure the appliance manually after boot.
