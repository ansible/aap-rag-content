---
title: "Module: mycompany.infrastructure.configure_network"
url: "https://github.com/ansible/aap-rag-content/blob/main/byok/ansible-collection-docs/modules/configure_network.md"
---
# Module: mycompany.infrastructure.configure_network

**Short description:** Configure VPC networks, subnets, and security groups
**Collection:** mycompany.infrastructure
**Version added:** 1.0.0

---

## Synopsis

- Creates or updates a Virtual Private Cloud (VPC) network configuration, including subnets, route tables, internet gateways, and security groups.
- Supports AWS VPC, Azure Virtual Network (VNet), and GCP VPC networks.
- When `state=present` and the network already exists (identified by `name` and `project`), mutable attributes are updated in-place.
- All subnet and security group operations are idempotent.

---

## Requirements

The following must be installed on the host executing this module:

- python >= 3.9
- boto3 >= 1.26 *(for `provider=aws`)*
- azure-mgmt-network >= 23.0 *(for `provider=azure`)*
- google-cloud-compute >= 1.14 *(for `provider=gcp`)*
- netaddr >= 0.8

---

## Parameters

| Parameter | Type | Required | Default | Choices | Description |
|---|---|---|---|---|---|
| `name` | string | yes | | | Name of the VPC or virtual network resource. |
| `provider` | string | yes | | `aws`, `azure`, `gcp` | Cloud provider. |
| `cidr_block` | string | no | | | Primary IPv4 CIDR block for the VPC (e.g. `10.0.0.0/16`). Required when creating a new network. Cannot be changed after creation. |
| `subnets` | list of dicts | no | | | List of subnet definitions. Each dict contains: `name` (required), `cidr` (required), `az` (optional), `public` (boolean, default `false`). |
| `security_groups` | list of dicts | no | | | List of security group definitions. Each dict contains: `name` (required), `description`, `inbound_rules`, `outbound_rules`. Rules have `protocol`, `from_port`, `to_port`, `source` (CIDR or SG name). |
| `enable_dns_hostnames` | boolean | no | `true` | `true`, `false` | Enable DNS hostnames for instances launched into the VPC. |
| `internet_gateway` | boolean | no | `false` | `true`, `false` | Attach an internet gateway to the VPC. Required for public subnets to be reachable from the internet. |
| `state` | string | no | `present` | `present`, `absent` | Desired state of the network resources. |
| `region` | string | no | | | Cloud region. Env var: `MYCOMPANY_REGION`. |
| `tags` | dictionary | no | `{}` | | Key/value tags applied to the VPC and all resources it contains. |

---

## Attributes

| Attribute | Support | Description |
|---|---|---|
| check_mode | full | Reports what would change without making changes. |
| diff_mode | full | Shows before/after for all changed resources. |
| platform | all | No target-host OS dependencies. |

---

## Notes

- The `netaddr` Python library is required on the control node to validate CIDR notation and compute subnet overlaps before making API calls.
- Deleting a VPC (`state=absent`) will fail if any dependent resources (EC2 instances, RDS instances, load balancers) still exist inside it. Terminate or migrate those resources first.
- Security group rules referencing other security groups by name are resolved at apply time. If the referenced group does not exist, the task will fail.
- On GCP, security groups correspond to firewall rules applied at the network level.

---

## See Also

- [create_server](create_server.md) — Create servers inside the VPC configured by this module.
- [infrastructure filters](../filter/infrastructure_filters.md) — Use the `to_cidr` filter to convert IP/prefix notation to CIDR.

---

## Examples

```yaml
# Create a production VPC on AWS with public and private subnets
- name: Configure production VPC
  mycompany.infrastructure.configure_network:
    name: myapp-prod-vpc
    provider: aws
    region: us-east-1
    cidr_block: "10.0.0.0/16"
    internet_gateway: true
    enable_dns_hostnames: true
    subnets:
      - name: public-us-east-1a
        cidr: "10.0.1.0/24"
        az: us-east-1a
        public: true
      - name: public-us-east-1b
        cidr: "10.0.2.0/24"
        az: us-east-1b
        public: true
      - name: private-us-east-1a
        cidr: "10.0.10.0/24"
        az: us-east-1a
        public: false
      - name: private-us-east-1b
        cidr: "10.0.11.0/24"
        az: us-east-1b
        public: false
    security_groups:
      - name: web-sg
        description: Allow HTTP/HTTPS from internet
        inbound_rules:
          - protocol: tcp
            from_port: 80
            to_port: 80
            source: "0.0.0.0/0"
          - protocol: tcp
            from_port: 443
            to_port: 443
            source: "0.0.0.0/0"
        outbound_rules:
          - protocol: "-1"
            from_port: 0
            to_port: 0
            source: "0.0.0.0/0"
      - name: db-sg
        description: Allow Postgres from app tier only
        inbound_rules:
          - protocol: tcp
            from_port: 5432
            to_port: 5432
            source: web-sg
    tags:
      environment: production
      team: platform
    state: present
  register: vpc_result

# Delete a staging network
- name: Remove staging VPC
  mycompany.infrastructure.configure_network:
    name: myapp-staging-vpc
    provider: aws
    region: us-east-1
    state: absent
```

---

## Return Values

| Key | Description | Returned | Type |
|---|---|---|---|
| `network` | Details of the VPC or virtual network. | when `state=present` | dict |
| `network.vpc_id` | Provider-assigned VPC ID. | always | string — e.g. `"vpc-0a1b2c3d4e5f6a7b8"` |
| `network.name` | VPC name. | always | string |
| `network.cidr_block` | Primary CIDR block of the VPC. | always | string — e.g. `"10.0.0.0/16"` |
| `network.subnets` | List of subnet dicts with `subnet_id`, `name`, `cidr`, `az`, `public`. | always | list |
| `network.security_groups` | List of security group dicts with `sg_id`, `name`, `inbound_rules`, `outbound_rules`. | always | list |
| `changed` | Whether any changes were made. | always | bool |

---

## Authors

- Alice Nguyen (@alice-n) — alice.nguyen@mycompany.example