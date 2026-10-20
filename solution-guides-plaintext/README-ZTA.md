## Overview

Traditional network security relies on perimeter defenses, but modern threats require a "never trust, always verify" approach. Organizations spend hours manually coordinating identity, secrets, policy, and network controls across fragmented tools, leading to security gaps and operational overhead. This guide demonstrates how to build and operate a Zero Trust Architecture using Red Hat Ansible Automation Platform as the central orchestration layer, reducing manual security operations by 80% while improving compliance posture.

<h2 id="background"></h2>

## Background

**Zero Trust Architecture (ZTA)** is a security framework that eliminates implicit trust and continuously validates every user, device, and application attempting to access resources. Unlike traditional perimeter-based security that assumes internal network traffic is safe, Zero Trust assumes breach and enforces strict verification at every layer.

 <a target="_blank" href="https://www.redhat.com/en/topics/security/what-is-zero-trust">What is Zero Trust? -- redhat.com</a>

The core principles include:
- 🚫 **Never trust, always verify** — Every access request requires authentication and authorization
- 🔐 **Least privilege** — Grant minimum necessary permissions for the minimum necessary time
- ⚠️ **Assume breach** — Design systems to limit blast radius when (not if) compromise occurs
- 🔒 **Micro-segmentation** — Isolate workloads and control traffic flows at granular levels

Traditional approaches require teams to manually coordinate identity (LDAP/AD), secrets (credential vaults), policy engines (OPA/RBAC), network controls (firewalls/ACLs), and monitoring (SIEM) across siloed tools. This creates security gaps, configuration drift, and slow incident response.

### The Traditional Security Model vs. Zero Trust

| Approach | Trust Model | Credential Lifetime | Policy Enforcement | Incident Response |
|----------|------------|---------------------|-------------------|-------------------|
| **Traditional Perimeter** | Trust internal network traffic | Passwords last months/years | Manual reviews, change tickets | Human-driven, hours to days |
| **Zero Trust Architecture** | Verify every request | Credentials expire in minutes | Policy-as-code, enforced at platform level | Automated, seconds to minutes |

 <a target="_blank" href="https://csrc.nist.gov/publications/detail/sp/800-207/final">NIST SP 800-207: Zero Trust Architecture -- csrc.nist.gov</a>

<h2 id="solution"></h2>

## Solution

This solution demonstrates an end-to-end Zero Trust Architecture using Ansible Automation Platform to orchestrate identity, secrets, policy, and network controls.

**What makes up the solution?**

-  **Red Hat Ansible Automation Platform (AAP)** — Central orchestration layer and policy enforcement point <a target="_blank" href="https://www.redhat.com/en/technologies/management/ansible">[Link]</a>
-  **Red Hat Identity Management (IdM/FreeIPA)** — Identity provider, LDAP, Kerberos, CA, DNS <a target="_blank" href="https://www.redhat.com/en/technologies/linux-platforms/enterprise-linux">[Link]</a>
-  **HashiCorp Vault** — Secrets management, dynamic credentials, SSH certificate authority <a target="_blank" href="https://www.vaultproject.io/">[Link]</a>
-  **Open Policy Agent (OPA)** — Policy-based authorization with deny-by-default <a target="_blank" href="https://www.openpolicyagent.org/">[Link]</a>
-  **SPIFFE/SPIRE** — Workload identity and cryptographic attestation <a target="_blank" href="https://spiffe.io/">[Link]</a>
-  **Netbox** — Configuration management database (CMDB) as source of truth <a target="_blank" href="https://netbox.dev/">[Link]</a>
-  **Arista cEOS** — Network fabric with VLAN isolation and ACLs <a target="_blank" href="https://www.arista.com/">[Link]</a>
-  **Gitea** — Git server for GitOps workflows <a target="_blank" href="https://gitea.io/">[Link]</a>

### Who Benefits

| Persona | Challenge | What They Gain |
|---------|-----------|---------------|
|  **Security Architect** | Manually orchestrating identity, secrets, policy, and network controls across siloed tools | Reference architecture showing how AAP unifies Zero Trust components with automated policy enforcement |
|  **IT Operations / SRE** | Credential sprawl, standing access, and manual secret rotation create security risk and operational toil | Executable playbooks for dynamic credentials, short-lived certificates, and automated credential revocation that eliminate standing secrets |
|  **Compliance / Audit** | Proving continuous compliance requires manual evidence collection across disconnected systems | Unified audit trail capturing OPA policy decisions, Vault credential lifecycle, IdM authentication, and network changes with full traceability |
|  **Platform Engineer** | Network segmentation requires manual firewall rules and switch ACL changes prone to drift | Automated micro-segmentation with policy-driven VLAN management, firewall rules, and ACL enforcement validated against CMDB |

**Recommended Demos and Self-Paced Labs:**

-  [Zero Trust Workshop (GitHub)](https://github.com/nmartins0611/zta-workshop-aap) -- Complete hands-on lab with all five use cases
-  [Ansible Automation Platform Product Tour](https://www.redhat.com/en/technologies/management/ansible/try-it) -- Interactive platform walkthrough

**Source Code:**

-  [nmartins0611/zta-workshop-aap](https://github.com/nmartins0611/zta-workshop-aap) -- Playbooks, policies, and configuration for all use cases

<h2 id="prerequisites"></h2>

## Prerequisites

### Ansible Automation Platform

- **Ansible Automation Platform 2.6+** — Required for Policy as Code features
- **AAP Policy as Code (OPA Gateway)** — Platform-level policy enforcement

### Featured Ansible Content Collections

| Collection | Type | Purpose |
|-----------|------|---------|
| <a target="_blank" href="https://console.redhat.com/ansible/automation-hub/repo/published/ansible/posix/">ansible.posix</a> | Certified | Firewall management, mount, selinux, sysctl |
| <a target="_blank" href="https://console.redhat.com/ansible/automation-hub/repo/published/community/general/">community.general</a> | Validated | OPA queries, system configuration |
| <a target="_blank" href="https://console.redhat.com/ansible/automation-hub/repo/published/community/hashi_vault/">community.hashi_vault</a> | Validated | Vault integration, secrets lookups, SSH CA |
| <a target="_blank" href="https://console.redhat.com/ansible/automation-hub/repo/published/netbox/netbox/">netbox.netbox</a> | Validated | CMDB inventory source, DCIM operations |
| <a target="_blank" href="https://console.redhat.com/ansible/automation-hub/repo/published/arista/eos/">arista.eos</a> | Certified | Arista cEOS switch configuration, VLAN management |
| <a target="_blank" href="https://console.redhat.com/ansible/automation-hub/repo/published/ansible/controller/">ansible.controller</a> | Certified | Automation Controller configuration as code |

### External Systems

| System | Required | Purpose | Examples |
|--------|----------|---------|----------|
| Identity Provider | Yes | LDAP/Kerberos authentication and authorization | Red Hat IdM (FreeIPA), Active Directory |
| Secrets Manager | Yes | Dynamic credentials and SSH certificate authority | HashiCorp Vault, CyberArk |
| Policy Engine | Yes | Deny-by-default authorization decisions | Open Policy Agent (OPA) |
| CMDB | Yes | Infrastructure source of truth | Netbox, ServiceNow CMDB |
| SIEM / Log Analytics | Optional | Bypass detection and audit correlation in defense-in-depth scenarios | Splunk, Elastic Stack, IBM QRadar, Wazuh |
| Network Infrastructure | Yes | Micro-segmentation and traffic control | Arista cEOS, Cisco, Juniper |
| Workload Identity | Optional but recommended | Cryptographic workload attestation | SPIFFE/SPIRE |
| Git Server | Optional | GitOps workflow triggers | Gitea, GitHub, GitLab |

### Infrastructure Requirements

- **RHEL 9.x** hosts for all components
- **Podman** for containerized services (SPIRE, OPA, application containers)
- **Network:** Management network (192.168.1.0/24) plus internal Podman networks for application tiers
- **DNS:** All hostnames must resolve via IdM DNS (zta.lab domain)
- **Certificate Trust:** All hosts enrolled in IdM domain for CA trust

### Operational Impact

| Use Case | Impact Level | Reversibility |
|---------|--------------|---------------|
| Use Case 1 (Verification) | **None** | N/A (read-only checks) |
| Use Case 2 (Credential Management) | **Medium** | Reversible (credentials auto-expire) |
| Use Case 3 (Policy Enforcement) | **High** | Configuration changes require testing |
| Use Case 4 (Network Operations) | **High** | Network changes, test in non-production first |
| Use Case 5 (Access Control) | **High** | Requires break-glass access path |

**Warning:** Use Cases 3, 4, and 5 make configuration changes to SSH, network, and access controls. Test in a non-production environment first and ensure break-glass access is validated before applying to production systems.

---

## Zero Trust Architecture Workflow

The solution implements defense-in-depth with multiple policy enforcement rings.

### Key Workflow Patterns

**Pattern 1: Policy-Gated Operations**
Every operation passes through AAP's OPA gateway before execution. Template name patterns map to required IdM groups, enforced at platform level with no bypass possible.

**Pattern 2: Just-In-Time Credentials**
No standing access. Credentials are generated on-demand from Vault, used once, and automatically revoked after TTL expiration.

**Pattern 3: Workload Identity Verification**
SPIFFE/SPIRE provides cryptographic proof that the automation platform is legitimate, preventing rogue scripts from impersonating AAP.

**Pattern 4: Defense-in-Depth Lockdown**
Four independent layers (firewall, HBAC, Vault policy, SIEM monitoring) must all be bypassed to compromise a host, with break-glass recovery tested and validated.

<h2 id="use-cases"></h2>

## Use Cases

<h3 id="use-case-1"></h3>

### Use Case 1: Infrastructure Integration and Service Verification

**Operational Impact:** None (read-only verification)

**Business Value:** Reduce integration time by 70% through automated verification of identity, secrets, policy, and infrastructure components.

**What This Use Case Demonstrates:**

This use case establishes the foundation by verifying that Ansible Automation Platform can successfully integrate with all Zero Trust components. All credentials are pre-configured via automation, and you verify the integrations work correctly.

#### Key Integration Points

1. **Vault Lookups:** AAP credentials use external secret lookups instead of stored passwords
2. **IdM LDAP:** Users authenticate to AAP with IdM credentials, group membership determines permissions
3. **Netbox Inventory:** Infrastructure hosts are sourced from CMDB, not static files
4. **OPA Policy Gateway:** AAP checks policy before launching any job template
5. **Vault SSH CA:** Ephemeral SSH certificates replace static keys

#### Featured Playbook: `verify-zta-services.yml`

```yaml
- name: Verify All ZTA Services
  hosts: zta_services
  tasks:
    - name: Check IdM status
      ansible.builtin.command: ipactl status
      register: idm_status
      failed_when: "'RUNNING' not in idm_status.stdout"

    - name: Check Vault health
      ansible.builtin.uri:
        url: "http://{{ vault_host }}:8200/v1/sys/health"
        method: GET
      register: vault_health
      failed_when: vault_health.json.sealed | bool

    - name: Check OPA policies loaded
      ansible.builtin.uri:
        url: "http://{{ opa_host }}:8181/v1/policies"
        method: GET
      register: opa_policies
      failed_when: "'aap.gateway' not in opa_policies.json.result"

    - name: Display verification results
      ansible.builtin.debug:
        msg:
          - "IdM: {{ 'RUNNING' if 'RUNNING' in idm_status.stdout else 'FAILED' }}"
          - "Vault: {{ 'UNSEALED' if not vault_health.json.sealed else 'SEALED' }}"
          - "OPA: {{ 'LOADED' if 'aap.gateway' in opa_policies.json.result else 'MISSING' }}"
```

#### Validation Steps

**Test Vault Dynamic Credentials:**

```bash
# Generate a dynamic PostgreSQL user with 5-minute TTL
vault read database/creds/ztaapp-short-lived

# Observe credentials are unique each time
# Username format: v-root-ztaapp-s-<random>
# After 5 minutes, user is automatically revoked
```

**Test Vault SSH Signed Certificates:**

```bash
# Generate ephemeral keypair
ssh-keygen -t rsa -b 2048 -f /tmp/ephemeral -N '' -q

# Sign with Vault CA
vault write -field=signed_key ssh/sign/ssh-signer \
  public_key=@/tmp/ephemeral.pub valid_principals=rhel > /tmp/ephemeral-cert.pub

# Inspect certificate
ssh-keygen -L -f /tmp/ephemeral-cert.pub
# Shows: TTL, valid principals, serial number

# SSH using signed certificate (not password)
ssh -i /tmp/ephemeral -o CertificateFile=/tmp/ephemeral-cert.pub \
  -p 2023 rhel@192.168.1.11
```

**Test OPA Policy Decisions:**

```bash
# Query OPA for a patching decision
curl -s http://central.zta.lab:8181/v1/data/zta/patch_access/decision \
  -d '{
    "input": {
      "user": "ztauser",
      "user_groups": ["patch-admins"],
      "host": "app.zta.lab",
      "action": "apply_patch"
    }
  }' | python3 -m json.tool

# Expected result: {"allow": true, "reason": "user in patch-admins"}
```

> **Tip:** IdM LDAP Configuration
>
> On AAP 2.6, configure IdM LDAP authentication via **Access Management → Authentication Methods**. Use **GroupOfNamesType** with `name_attr: cn` for FreeIPA group lookups. See the workshop Section 1.2 for detailed UI configuration steps including authentication mapping rules for team assignment.

---

<h3 id="use-case-2"></h3>

### Use Case 2: Just-In-Time Credential Management

**Operational Impact:** Medium (creates database users, deploys application)

**Business Value:** Eliminate standing database credentials, reducing credential compromise risk by 95% through 5-minute TTL enforcement.

**What This Use Case Demonstrates:**

Deploy applications using dynamic database credentials from Vault with automatic expiration. The deployment is protected by OPA policy — only users in the `app-deployers` group can proceed. Demonstrates deny-by-default authorization and just-in-time credential issuance.

**Credential Lifecycle Timeline:**

| Time | Event | Component | Result |
|------|-------|-----------|--------|
| T+0s | User launches "Deploy Application" | AAP Controller | OPA policy check initiated |
| T+1s | OPA evaluates user groups | Open Policy Agent | ✅ User in `app-deployers` → ALLOW |
| T+2s | Request dynamic DB credentials | HashiCorp Vault | Creates `v-root-ztaapp-s-abc123` with 300s TTL |
| T+3s | Deploy application with credentials | AAP Playbook | Application configured with ephemeral creds |
| T+4s | Application starts serving traffic | App Server | ✅ Healthy, connected to database |
| **T+300s** | Vault TTL expires | HashiCorp Vault | ⚠️ Automatic credential revocation |
| T+301s | Application loses database access | App Server | ❌ Connection errors logged |

#### Featured Playbook: `deploy-application.yml`

```yaml
- name: Deploy Application with Short-Lived Credentials
  hosts: localhost
  tasks:
    # Step 1: Query OPA for authorization
    - name: Check OPA database access policy
      ansible.builtin.uri:
        url: "http://{{ opa_host }}:8181/v1/data/zta/db_access/decision"
        method: POST
        body_format: json
        body:
          input:
            user: "{{ tower_user_name }}"
            user_groups: "{{ tower_user_groups }}"
            database: "ztaapp"
            action: "deploy"
      register: opa_decision
      failed_when: not opa_decision.json.result.allow

    # Step 2: Generate dynamic database credentials
    - name: Create Vault database credential
      community.hashi_vault.vault_read:
        url: "{{ vault_addr }}"
        path: database/creds/ztaapp-short-lived
      register: db_creds
      # Vault creates: username, password with 5-minute TTL

    # Step 3: Configure network ACL for micro-segmentation
    - name: Apply database access ACL
      arista.eos.eos_config:
        lines:
          - "10 permit tcp host 10.20.0.10 host 10.30.0.10 eq 5432"
          - "20 deny ip any host 10.30.0.10"
        parents: ip access-list ZTA-APP-TO-DB
      delegate_to: ceos2

    # Step 4: Deploy application with ephemeral credentials
    - name: Deploy application
      ansible.builtin.template:
        src: app-config.j2
        dest: /opt/ztaapp/.env
      vars:
        db_username: "{{ db_creds.data.username }}"
        db_password: "{{ db_creds.data.password }}"
      delegate_to: app
      notify: restart ztaapp
```

#### Deny-by-Default in Action

**Wrong user attempt (neteng — not in app-deployers):**

```
OPA Database Access Decision:
  User:       neteng
  Groups:     []
  Database:   ztaapp
  Decision:   DENIED
  Reason:     user 'neteng' is not authorized to request database credentials

ACCESS DENIED by OPA policy. Vault never contacted, no credentials issued.
```

**Correct user attempt (appdev — in app-deployers):**

```
OPA Database Access Decision:
  User:       appdev
  Groups:     ['app-deployers']
  Database:   ztaapp
  Decision:   ALLOWED

Dynamic database credentials created:
  Username: v-root-ztaapp-s-abc123def
  TTL:      300s
  Lease:    database/creds/ztaapp-short-lived/xyz

Application deployed successfully:
  URL:     http://app.zta.lab:8081
  Health:  ok
  DB User: v-root-ztaapp-s-abc123def (expires in 5 minutes)
```

#### Observing Credential Expiry

After 5 minutes, the Vault-generated database user is automatically revoked:

```bash
# Before expiry
ssh -p 2022 rhel@central.zta.lab "sudo -u postgres psql -c '\du'"
# Shows: v-root-ztaapp-s-abc123def

# After 5 minutes
ssh -p 2022 rhel@central.zta.lab "sudo -u postgres psql -c '\du'"
# User is gone — Vault revoked it

# Application loses database access
curl http://app.zta.lab:8081/health
# Returns: unhealthy (database connection lost)
```

> **ZTA Principle:** Credentials are ephemeral. Without rotation, access is automatically removed. This limits the window of opportunity for compromised credentials and eliminates standing access.

---

<h3 id="use-case-3"></h3>

### Use Case 3: Platform-Level Policy Enforcement

**Operational Impact:** High (applies SSH hardening, password policy, audit rules)

**Business Value:** Enforce separation of duties and reduce unauthorized change risk through platform-level policy gates that cannot be bypassed.

**What This Use Case Demonstrates:**

AAP **Policy as Code** enforces authorization at the platform level — before any playbook runs. The `aap.gateway` OPA policy evaluates every launch request and blocks unauthorized users from even starting a job. Demonstrates separation of duties and platform-level enforcement with no bypass possible.

#### Gateway Policy Rules

| Template Name Contains | Required AAP Team | IdM Group |
|------------------------|-------------------|-----------|
| "Patch" | Infrastructure or Security | team-infrastructure, team-security |
| "VLAN" or "Network" | Infrastructure | team-infrastructure |
| "Deploy", "Application" | Applications or DevOps | team-applications, team-devops |

#### The Security Patch

The `apply-security-patch.yml` playbook deploys:
1. **Login banner** — Legal warning on `/etc/issue` and `/etc/motd`
2. **SSH hardening** — Disable root login, max 3 auth attempts, no password authentication for root
3. **Password policy** — 12-character minimum with complexity requirements
4. **Audit logging** — Monitor authentication events, identity file changes, sudoers modifications

#### Featured Playbook Excerpt: `apply-security-patch.yml`

```yaml
- name: Apply Security Hardening Patch
  hosts: "{{ target_host }}"
  become: true
  tasks:
    - name: Deploy security login banner
      ansible.builtin.copy:
        content: |
          ****************************************************************************
          WARNING: Unauthorized access to this system is forbidden and will be
          prosecuted by law. By accessing this system, you agree that your actions
          may be monitored if unauthorized usage is suspected.
          ****************************************************************************
        dest: "{{ item }}"
        mode: '0644'
      loop:
        - /etc/issue
        - /etc/motd

    - name: Apply SSH hardening
      ansible.builtin.lineinfile:
        path: /etc/ssh/sshd_config
        regexp: "{{ item.regexp }}"
        line: "{{ item.line }}"
      loop:
        - { regexp: '^PermitRootLogin', line: 'PermitRootLogin no' }
        - { regexp: '^MaxAuthTries', line: 'MaxAuthTries 3' }
        - { regexp: '^PermitEmptyPasswords', line: 'PermitEmptyPasswords no' }
      notify: restart sshd

    - name: Deploy password policy
      ansible.builtin.copy:
        content: |
          minlen = 12
          dcredit = -1
          ucredit = -1
          lcredit = -1
          ocredit = -1
        dest: /etc/security/pwquality.conf.d/zta-policy.conf
        mode: '0644'

    - name: Configure audit rules for ZTA
      ansible.builtin.copy:
        content: |
          -w /var/log/lastlog -p wa -k zta-auth
          -w /var/run/faillock/ -p wa -k zta-auth
          -w /etc/ssh/sshd_config -p wa -k zta-sshd
          -w /etc/sudoers -p wa -k zta-sudoers
        dest: /etc/audit/rules.d/zta.rules
        mode: '0640'
      notify: reload auditd
```

#### Platform Gate in Action

**Scenario 1: Wrong user (neteng — not in Infrastructure or Security team)**

1. User `neteng` clicks "Launch" on **Apply Security Patch** template
2. AAP sends request to OPA `v1/data/aap/gateway/decision`
3. OPA evaluates:
   ```
   Template: "Apply Security Patch"  → contains "Patch"
   Required: Infrastructure or Security team
   User:     neteng → teams: []
   Result:   DENIED
   ```
4. AAP blocks the launch — job never starts, no SSH connection, no changes
5. User sees: "Denied by policy — you are not authorized to launch this template"

**Scenario 2: Correct user (ztauser — in Infrastructure team)**

1. User `ztauser` clicks "Launch" on **Apply Security Patch**
2. OPA evaluates:
   ```
   User: ztauser → teams: ['Infrastructure']
   Result: ALLOWED
   ```
3. Playbook executes, patch is applied:
   ```
   Security Patch Applied

   Host:      app.zta.lab
   Patch:     ZTA-SEC-2026-001

   Applied:
     ✓ Security login banner (/etc/issue + /etc/motd)
     ✓ SSH hardening (no root, max 3 auth tries)
     ✓ Password policy (12 char min, complexity)
     ✓ Audit logging (auth, identity, sudoers)
   ```

#### Verification

```bash
# SSH to patched host — see banner immediately
ssh -p 2023 rhel@central.zta.lab

# Verify SSH hardening
sudo sshd -T | grep -E 'permitrootlogin|maxauthtries'
# Expected: permitrootlogin no, maxauthtries 3

# Verify password policy
cat /etc/security/pwquality.conf.d/zta-policy.conf

# Verify audit rules
sudo auditctl -l | grep zta
# Expected: watches on /var/log/lastlog, /etc/ssh/sshd_config, /etc/sudoers
```

> **Separation of Duties:** The `appdev` user (Applications team) cannot launch patching templates. The `ztauser` (Infrastructure team) cannot launch application deployment templates. Each team's access is scoped by OPA policy, enforced at the platform level.

---

<h3 id="use-case-4"></h3>

### Use Case 4: Workload Identity Verification for Network Operations

**Operational Impact:** High (creates VLANs, modifies network ACLs)

**Business Value:** Prevent rogue automation and insider threats through cryptographic workload verification that proves the automation platform is legitimate.

**What This Use Case Demonstrates:**

Defense-in-depth for network automation with **two OPA policy rings**: the outer ring (AAP gateway) checks if the user can launch the template, and the inner ring (in-playbook) validates SPIFFE workload identity, user group, VLAN range, and action. Demonstrates workload identity verification and runtime parameter validation.

#### SPIFFE/SPIRE Workload Identity

[SPIFFE](https://spiffe.io/) (Secure Production Identity Framework For Everyone) provides cryptographic identities to workloads:

- **SPIRE Server** runs on `central` — trust root
- **SPIRE Agents** run on `control` (AAP), `db`, `vault` — issue SVIDs to local workloads
- **X.509 SVID** (SPIFFE Verifiable Identity Document) — short-lived certificate with workload identity
- **Trust domain:** `zta.lab` (matches IdM domain)

The AAP network automation workload receives identity:
```
spiffe://zta.lab/workload/network-automation
```

#### Featured Playbook: `configure-vlan.yml`

```yaml
- name: Verify SPIFFE Workload Identity
  hosts: automation
  tasks:
    - name: Fetch SVID from local SPIRE Agent
      ansible.builtin.command:
        cmd: /opt/spire/bin/spire-agent api fetch x509 -socketPath /run/spire/sockets/agent.sock
      register: spiffe_svid

    - name: Parse SPIFFE ID from SVID
      ansible.builtin.set_fact:
        spiffe_id: "{{ spiffe_svid.stdout | regex_search('SPIFFE ID:\\s+(.+)', '\\1') | first }}"

    - name: Display workload identity
      ansible.builtin.debug:
        msg: "Workload verified: {{ spiffe_id }}"
      failed_when: spiffe_id != "spiffe://zta.lab/workload/network-automation"

- name: OPA Policy Decision (Inner Ring)
  hosts: zta_services
  tasks:
    - name: Query OPA network policy
      ansible.builtin.uri:
        url: "http://{{ opa_host }}:8181/v1/data/zta/network/decision"
        method: POST
        body_format: json
        body:
          input:
            user: "{{ tower_user_name }}"
            user_groups: "{{ tower_user_groups }}"
            spiffe_id: "{{ hostvars['control']['spiffe_id'] }}"
            action: "create_vlan"
            vlan_id: "{{ new_vlan_id | int }}"
      register: opa_decision

    - name: Display policy decision
      ansible.builtin.debug:
        msg:
          - "Workload verified: {{ opa_decision.json.result.conditions.workload_verified }}"
          - "User authorized: {{ opa_decision.json.result.conditions.user_authorized }}"
          - "Valid VLAN: {{ opa_decision.json.result.conditions.valid_vlan }}"
          - "Action permitted: {{ opa_decision.json.result.conditions.action_permitted }}"
      failed_when: not opa_decision.json.result.allow

- name: Create VLAN on Arista Fabric
  hosts: network
  tasks:
    - name: Configure VLAN
      arista.eos.eos_vlans:
        config:
          - vlan_id: "{{ new_vlan_id }}"
            name: "{{ new_vlan_name }}"
        state: merged

- name: Update Netbox CMDB
  hosts: zta_services
  tasks:
    - name: Create VLAN in Netbox
      netbox.netbox.netbox_vlan:
        netbox_url: "{{ netbox_url }}"
        netbox_token: "{{ netbox_token }}"
        data:
          vid: "{{ new_vlan_id }}"
          name: "{{ new_vlan_name }}"
          description: "Created by {{ tower_user_name }} via {{ spiffe_id }}"
        state: present
```

#### Policy Enforcement Scenarios

**Scenario 1: Wrong user (neteng — not in network-admins)**

```
SPIFFE Workload Identity Verification
  SPIFFE ID: spiffe://zta.lab/workload/network-automation
  Status:    VERIFIED ✓

OPA Network Policy Decision
  User:      neteng
  Action:    create_vlan
  VLAN ID:   200
  Result:    DENIED

  Conditions:
    Workload verified:      PASS  (legitimate AAP workload)
    User in network-admins: FAIL  (neteng not authorized)
    Valid VLAN ID:          PASS  (200 is in range 100-999)
    Action permitted:       PASS  (create_vlan is allowed)

DENIED: user 'neteng' is not a member of network-admins group
```

The SPIFFE check passes (the platform is legitimate) but the **user** is not authorized. Arista switches are never touched.

**Scenario 2: Correct user, invalid VLAN (netadmin with VLAN 5000)**

```
OPA Network Policy Decision
  User:      netadmin
  Action:    create_vlan
  VLAN ID:   5000
  Result:    DENIED

  Conditions:
    Workload verified:      PASS
    User in network-admins: PASS
    Valid VLAN ID:          FAIL  (5000 outside range 100-999)
    Action permitted:       PASS

DENIED: VLAN ID 5000 is outside the permitted range (100-999)
```

**Scenario 3: Correct user, valid VLAN (netadmin with VLAN 200)**

```
SPIFFE Workload Identity Verification
  SPIFFE ID: spiffe://zta.lab/workload/network-automation
  Status:    VERIFIED ✓

OPA Network Policy Decision
  Result:    ALLOWED
  All conditions: PASS

VLAN 200 (DMZ) created on ceos1, ceos2, ceos3

VLAN Configuration Complete
  VLAN 200 (DMZ)
  Switches:   ceos1, ceos2, ceos3 (Arista cEOS fabric)
  Netbox:     Created with audit trail
  User:       netadmin
  Workload:   spiffe://zta.lab/workload/network-automation
```

Verify on switches:
```bash
ssh -p 2001 admin@central.zta.lab "show vlan brief"
# VLAN 200 appears on all switches
```

Verify in Netbox:
```bash
curl -H "Authorization: Token $NETBOX_TOKEN" \
  http://netbox.zta.lab:8880/api/ipam/vlans/?vid=200 | python3 -m json.tool
# Description includes: "Created by netadmin via spiffe://zta.lab/workload/network-automation"
```

> **Why verify workload identity?** A compromised script running outside AAP could impersonate a network admin user. SPIFFE cryptographically proves the *platform* is legitimate, not just the user.

---

<h3 id="use-case-5"></h3>

### Use Case 5: Defense-in-Depth Access Control

**Operational Impact:** High (restricts SSH access, requires break-glass testing)

**Business Value:** Reduce attack surface through layered access controls while maintaining operational recovery paths for incident management.

**What This Use Case Demonstrates:**

Apply defense-in-depth SSH lockdown with four independent layers, then recover from a misconfiguration that locks AAP out of managed hosts. Demonstrates layered security and the critical importance of tested break-glass access paths.

#### Layer 1: Firewall Lockdown

**Featured Task:**

```yaml
- name: Allow SSH only from AAP controller and break-glass host
  ansible.posix.firewalld:
    rich_rule: "rule family='ipv4' source address='{{ item }}' service name='ssh' accept"
    permanent: true
    state: enabled
  loop:
    - 192.168.1.10  # AAP controller
    - 192.168.1.11  # central (break-glass)
  notify: reload firewalld

- name: Block all other SSH
  ansible.posix.firewalld:
    service: ssh
    permanent: true
    state: disabled
  notify: reload firewalld
```

**Test:**
```bash
# From workstation (blocked)
ssh ztauser@app.zta.lab
# Connection refused (firewall blocks before authentication)

# From AAP controller (allowed)
ssh rhel@control.zta.lab
ssh rhel@app.zta.lab
# Connection succeeds
```

#### Layer 2: IdM HBAC Lockdown

IdM Host-Based Access Control rules determine which users can access which hosts for which services.

**HBAC Rules Created:**

| Rule Name | Users | Hosts | Services |
|-----------|-------|-------|----------|
| `allow_aap_automation` | `aap-service` | All managed hosts | `sshd` |
| `allow_breakglass` | `breakglass-admins` group | `central` only | `sshd` |

**Test with `ipa hbactest`:**

```bash
kinit admin

# Test unauthorized user
ipa hbactest --user=neteng --host=app.zta.lab --service=sshd
# Access denied (no matching rule)

# Test AAP service account
ipa hbactest --user=aap-service --host=app.zta.lab --service=sshd
# Access granted (matched rule: allow_aap_automation)

# Test break-glass admin
ipa hbactest --user=ztauser --host=central.zta.lab --service=sshd
# Access granted (matched rule: allow_breakglass)

ipa hbactest --user=ztauser --host=app.zta.lab --service=sshd
# Access denied (breakglass only allowed to central)
```

#### The Lockout Scenario

The instructor runs a playbook that accidentally removes the AAP service account from the HBAC rule. **Every AAP job now fails:**

```
UNREACHABLE! => {"msg": "Failed to connect to the host via ssh:
Permission denied (publickey,gssapi-keyex,gssapi-with-mic)"}
```

AAP cannot manage any hosts. The platform is locked out.

#### Break-Glass Recovery

**Step 1: Access via break-glass path**
```bash
ssh ztauser@central.zta.lab
# Works — ztauser is in breakglass-admins, central is allowed
```

**Step 2: Authenticate to IdM**
```bash
kinit admin
```

**Step 3: Diagnose the HBAC problem**
```bash
# Test AAP service account access
ipa hbactest --user=aap-service --host=app.zta.lab --service=sshd
# Access denied — confirms HBAC is the problem

# Check the HBAC rule
ipa hbacrule-show allow_aap_automation --all
# Notice: aap-service is missing from memberuser
```

**Step 4: Fix the HBAC rule**
```bash
ipa hbacrule-add-user allow_aap_automation --users=aap-service

# Verify fix
ipa hbactest --user=aap-service --host=app.zta.lab --service=sshd
# Access granted (matched rule: allow_aap_automation)
```

**Step 5: Return to AAP and re-run the job**

The job now succeeds. AAP can manage hosts again.

#### Layer 3: Vault Policy Lockdown

After lockdown, human operators can inspect secrets but cannot sign SSH certificates or generate dynamic credentials. Only AAP's AppRole can perform those operations.

**Human operator attempt:**
```bash
export VAULT_ADDR=http://vault.zta.lab:8200
vault login -method=userpass username=admin password=ansible123!

# Try to sign SSH certificate (DENIED)
vault write ssh/sign/ssh-signer public_key=@/tmp/test-key.pub
# Error: permission denied

# Read KV secret (ALLOWED — troubleshooting is permitted)
vault kv get secret/network/arista
# Success — human-readonly policy allows reads
```

**AAP AppRole (ALLOWED):**
```yaml
- name: AAP signs SSH certificate using AppRole
  community.hashi_vault.vault_write:
    url: "{{ vault_addr }}"
    auth_method: approle
    role_id: "{{ approle_role_id }}"
    secret_id: "{{ approle_secret_id }}"
    path: ssh/sign/ssh-signer
    data:
      public_key: "{{ ssh_public_key }}"
  register: signed_cert
```

#### Layer 4: Splunk Bypass Detection

Even when SSH is successfully blocked, attempts are logged and monitored.

**Splunk saved searches:**
1. **SSH Bypass — Login from Non-AAP Source:** Successful SSH from untrusted IP
2. **SSH Bypass — Repeated HBAC Denials:** Repeated HBAC-denied logins = reconnaissance

**Detection query:**
```
index=zta_syslog sourcetype=syslog sshd "Permission denied" OR "not allowed"
| stats count by src_ip, user
| where count >= 3
```

**Test:**
```bash
# Attempt SSH as unauthorized user (denied by HBAC)
ssh neteng@app.zta.lab
# Permission denied

# Check Splunk
# Activity → Triggered Alerts → "ZTA: SSH Bypass — Repeated HBAC Denials"
```

> **Defense in Depth:** Even if one layer fails, others still protect. If the firewall rule is accidentally removed, HBAC still denies unauthorized users. If HBAC is misconfigured, Vault policy prevents certificate signing. If all three fail, Splunk detects the bypass and alerts.

---

<h2 id="validation"></h2>

## Validation

The solution is validated through executable tests at each stage. A fully functional Zero Trust Architecture must pass all validation criteria.

> **Validation Philosophy: Trust but Verify**
>
> Zero Trust extends beyond user access -- it applies to the automation itself. Each use case includes concrete validation commands that prove the integration works correctly. These tests can be run in CI/CD pipelines, scheduled as AAP job templates, or executed manually during implementation.

### Comprehensive Validation Test Suite

**Use Case 1: ZTA Components Integration**

```bash
# Verify Vault unsealed and healthy
curl -s http://vault.zta.lab:8200/v1/sys/health | python3 -m json.tool
# Expected: {"sealed": false, "initialized": true}

# Verify OPA policies loaded
curl -s http://central.zta.lab:8181/v1/policies | python3 -m json.tool | grep -E 'aap.gateway|db_access|network'
# Expected: All three policies present

# Verify IdM running
ssh rhel@central.zta.lab "sudo ipactl status"
# Expected: All services RUNNING

# Verify Netbox inventory sync
# In AAP: Inventories → ZTA Lab Inventory → Sources → NetBox CMDB → Sync
# Expected: Green status, 10+ hosts

# Verify dynamic credentials
vault read database/creds/ztaapp-short-lived
# Expected: Unique username/password, 300s TTL

# Verify SSH certificate signing
ssh-keygen -t rsa -f /tmp/test -N '' -q
vault write -field=signed_key ssh/sign/ssh-signer public_key=@/tmp/test.pub > /tmp/test-cert.pub
ssh-keygen -L -f /tmp/test-cert.pub
# Expected: Shows certificate with TTL, valid principals
```

**Use Case 2: Just-In-Time Credential Management**

```bash
# Test OPA deny-by-default (wrong user)
curl -s http://central.zta.lab:8181/v1/data/zta/db_access/decision \
  -d '{"input": {"user": "neteng", "user_groups": [], "database": "ztaapp"}}' \
  | python3 -m json.tool
# Expected: {"result": {"allow": false}}

# Test OPA allow (correct user)
curl -s http://central.zta.lab:8181/v1/data/zta/db_access/decision \
  -d '{"input": {"user": "appdev", "user_groups": ["app-deployers"], "database": "ztaapp"}}' \
  | python3 -m json.tool
# Expected: {"result": {"allow": true}}

# Verify application health
curl http://app.zta.lab:8081/health
# Expected: {"status": "healthy", "database": "connected"}

# Verify dynamic DB user exists
ssh -p 2022 rhel@central.zta.lab "sudo -u postgres psql -c '\du'" | grep v-root
# Expected: Shows v-root-ztaapp-s-<random>

# Wait 5 minutes and verify credential expiry
sleep 300
ssh -p 2022 rhel@central.zta.lab "sudo -u postgres psql -c '\du'" | grep v-root
# Expected: No results (user auto-revoked)

curl http://app.zta.lab:8081/health
# Expected: unhealthy or connection error (lost DB access)
```

**Use Case 3: Platform-Level Policy Enforcement**

```bash
# Verify AAP Policy as Code enabled
curl -sk -u "admin:ansible123!" \
  "https://control.zta.lab/api/controller/v2/settings/opa/" | python3 -m json.tool
# Expected: OPA_ENABLED: true, OPA_PRE_ACTION_ENABLED: true

# Test gateway policy enforcement (manual query)
curl -s http://central.zta.lab:8181/v1/data/aap/gateway/decision \
  -d '{
    "input": {
      "user": {"username": "neteng", "teams": []},
      "template_name": "Apply Security Patch",
      "action": "launch"
    }
  }' | python3 -m json.tool
# Expected: {"result": {"allow": false}}

# Verify patch applied
ssh -p 2023 rhel@central.zta.lab
# Expected: Security banner displayed immediately

ssh -p 2023 rhel@central.zta.lab "sudo sshd -T | grep -E 'permitrootlogin|maxauthtries'"
# Expected: permitrootlogin no, maxauthtries 3

ssh -p 2023 rhel@central.zta.lab "cat /etc/security/pwquality.conf.d/zta-policy.conf"
# Expected: minlen = 12, complexity rules present

ssh -p 2023 rhel@central.zta.lab "sudo auditctl -l | grep zta"
# Expected: Audit rules for auth, sshd_config, sudoers
```

**Use Case 4: Workload Identity Verification for Network Operations**

```bash
# Verify SPIRE Agent running
ssh rhel@control.zta.lab "sudo systemctl status spire-agent"
# Expected: active (running)

# Fetch SVID
ssh rhel@control.zta.lab "sudo /opt/spire/bin/spire-agent api fetch x509 \
  -socketPath /run/spire/sockets/agent.sock"
# Expected: SPIFFE ID: spiffe://zta.lab/workload/network-automation

# Test network policy with SPIFFE verification
curl -s http://central.zta.lab:8181/v1/data/zta/network/decision \
  -d '{
    "input": {
      "user": "netadmin",
      "user_groups": ["network-admins"],
      "spiffe_id": "spiffe://zta.lab/workload/network-automation",
      "action": "create_vlan",
      "vlan_id": 200
    }
  }' | python3 -m json.tool
# Expected: {"result": {"allow": true}}

# Test wrong SPIFFE ID
curl -s http://central.zta.lab:8181/v1/data/zta/network/decision \
  -d '{
    "input": {
      "user": "netadmin",
      "user_groups": ["network-admins"],
      "spiffe_id": "spiffe://evil.com/rogue",
      "action": "create_vlan",
      "vlan_id": 200
    }
  }' | python3 -m json.tool
# Expected: {"result": {"allow": false}}

# Verify VLAN created on Arista
ssh -p 2001 admin@central.zta.lab "show vlan brief" | grep 200
# Expected: VLAN 200 with configured name

# Verify Netbox CMDB updated
curl -H "Authorization: Token $NETBOX_TOKEN" \
  "http://netbox.zta.lab:8880/api/ipam/vlans/?vid=200" | python3 -m json.tool
# Expected: VLAN 200 with description including SPIFFE ID
```

**Use Case 5: Defense-in-Depth Access Control**

```bash
# Layer 1: Firewall test
# From workstation (blocked source)
timeout 5 ssh ztauser@app.zta.lab
# Expected: Connection refused or timeout

# From AAP controller (allowed source)
ssh rhel@control.zta.lab "ssh rhel@app.zta.lab echo success"
# Expected: success

# Layer 2: HBAC test
ssh rhel@central.zta.lab
kinit admin
ipa hbactest --user=neteng --host=app.zta.lab --service=sshd
# Expected: Access denied

ipa hbactest --user=aap-service --host=app.zta.lab --service=sshd
# Expected: Access granted

# Layer 3: Vault policy test
vault login -method=userpass username=admin password=ansible123!
vault write ssh/sign/ssh-signer public_key=@/tmp/test.pub
# Expected: Error: permission denied

vault kv get secret/network/arista
# Expected: Success (read-only allowed)

# Layer 4: SIEM bypass detection
# Attempt SSH as unauthorized user
ssh neteng@app.zta.lab
# Denied by HBAC

# Check SIEM for denial events (query example varies by platform)
# Splunk example:
curl -u admin:ansible123! -k \
  'https://central.zta.lab:8089/services/search/jobs/export' \
  --data-urlencode 'search=index=zta_syslog sshd "Permission denied" user=neteng | head 1' \
  --data-urlencode 'output_mode=json'
# Expected: Denial event logged

# Break-glass recovery test
# Simulate lockout
ansible-playbook section6/playbooks/break-hbac.yml

# AAP job should fail
# From AAP: Launch any template
# Expected: UNREACHABLE (Permission denied)

# Recover via break-glass
ssh ztauser@central.zta.lab
kinit admin
ipa hbacrule-add-user allow_aap_automation --users=aap-service

# Verify fix
ipa hbactest --user=aap-service --host=app.zta.lab --service=sshd
# Expected: Access granted

# AAP job should succeed
# From AAP: Re-launch template
# Expected: Success
```

### Troubleshooting

<details>
<summary><strong>Common Failure Scenarios and Resolutions</strong></summary>

| Symptom | Likely Cause | Diagnostic Command | Fix |
|---------|-------------|-------------------|-----|
| 🔴 Vault dynamic credentials fail with 403 | Policy path mismatch | `vault list database/roles` | Verify policy path matches exact role name |
| 🔴 AAP jobs fail with "Permission denied" | HBAC rule missing aap-service user | `ipa hbactest --user=aap-service --host=<target> --service=sshd` | Add user with `ipa hbacrule-add-user` |
| 🔴 Application shows "unhealthy" after deployment | Database credentials expired | `vault read database/creds/ztaapp-short-lived` | Check TTL, run credential rotation playbook |
| 🔴 SPIFFE verification fails | SPIRE Agent not running | `sudo systemctl status spire-agent` | Start agent: `sudo systemctl start spire-agent` |
| 🔴 Netbox inventory sync fails | API token invalid or expired | `curl -H "Authorization: Token $TOKEN" http://netbox:8880/api/` | Regenerate token in Netbox UI, update AAP credential |
| 🔴 OPA policy returns 404 | Policy not loaded | `curl http://central.zta.lab:8181/v1/policies` | Re-run `setup/configure-opa-base.yml` |
| 🔴 SIEM not receiving logs | Log forwarder misconfigured | Check log shipper status and config | Verify rsyslog/Filebeat/Fluentd configuration |
| 🔴 Arista VLAN creation fails | ACL blocks management traffic | `ping <switch-ip>` from AAP controller | Verify management VLAN allows AAP → switch communication |
| 🔴 SELinux denials on container operations | File context incorrect | `sudo ausearch -m avc -ts recent \| audit2why` | Apply context: `sudo chcon -R -t container_file_t <path>` |

</details>

<h2 id="maturity-path"></h2>

## Maturity Path

Organizations can adopt Zero Trust incrementally, starting with foundational integrations and progressing to fully automated defense.

| Maturity Level | Description | What Gets Automated | Approval Required |
|----------------|-------------|---------------------|-------------------|
| **Crawl** | Read-only integrations and manual workflows | • Vault credential lookups (read-only)<br>• OPA policy queries (advisory mode)<br>• Netbox inventory source<br>• IdM LDAP authentication<br>• Manual validation of each operation | Yes — every operation requires human approval via AAP job launch |
| **Walk** | Automated operations with policy gates | • Dynamic credential generation (short TTL)<br>• Platform-level policy enforcement (AAP Policy as Code)<br>• Automated network changes (VLAN creation)<br>• Policy-gated patching<br>• Credential rotation on schedule | Conditional — policy allows/denies based on user + context, no per-operation approval |
| **Run** | Fully automated defense and self-healing | • Automated break-glass recovery<br>• Self-healing configuration drift detection<br>• Continuous compliance reporting<br>• SIEM-to-EDA incident response (see complementary guides) | No -- automation responds within seconds based on policy, human notified after action |

### Implementation Phases

**Phase 1: Foundation (Crawl — 2-4 weeks)**

Focus: Establish trust anchors and verify integrations work correctly.

- Deploy IdM, Vault, OPA, Netbox, SPIRE in non-production
- Integrate AAP with IdM LDAP for authentication
- Configure Netbox as inventory source
- Test Vault lookups for credentials (read-only, no auto-generation yet)
- Load OPA policies in advisory mode (log decisions, don't enforce)
- Validate break-glass access paths

Success criteria:
- All services healthy and integrated
- Users can authenticate via IdM
- Inventory syncs from Netbox
- OPA policy queries return expected results
- Break-glass path tested and documented

**Phase 2: Policy Enforcement (Walk — 4-8 weeks)**

Focus: Enforce policy-driven access and automate operations with gates.

- Enable AAP Policy as Code (OPA gateway enforcement)
- Deploy dynamic credentials for databases and SSH
- Implement SPIFFE workload identity verification
- Automate network VLAN creation with policy gates
- Apply security patches with platform-level authorization
- Configure credential rotation schedules

Success criteria:
- Policy denials prevent unauthorized operations
- Credentials expire automatically after TTL
- Network changes require both user and workload identity
- Separation of duties enforced (network admins ≠ patch admins ≠ app deployers)
- Audit trail captures user + workload + policy decision

**Phase 3: Automated Response (Run -- 2-4 weeks)**

Focus: Extend automation into self-healing operations and continuous compliance.

- Implement configuration drift detection and remediation
- Add self-healing for common failure scenarios
- Validate break-glass recovery under load
- Integrate SIEM-to-EDA incident response using the complementary guides below

Success criteria:
- Configuration drift auto-remediated
- Break-glass recovery tested and documented
- All security events logged with full context
- Incident response workflows documented for follow-on SIEM/EDA guide

### Measuring Success

| Metric | Baseline (Manual) | Target (Automated) | Measurement Method |
|--------|-------------------|--------------------|--------------------|
| **Credential rotation time** | 2-4 hours (manual rotation across systems) | < 5 minutes (automated, short-lived) | Vault audit log: time between credential creation and revocation |
| **Policy compliance audit** | 2-5 days (manual evidence collection) | < 1 hour (automated report generation) | OPA decisions + Vault lifecycle + IdM auth events |
| **Unauthorized access attempts** | Detected post-mortem (if at all) | Detected and blocked in real-time | Denied operations vs. allowed operations in audit logs |
| **Configuration drift detection** | Weekly manual checks | Continuous, auto-remediated within 15 minutes | AAP job logs: drift detection frequency and remediation time |
| **Mean time to recovery (MTTR)** | 4-8 hours (manual diagnosis and fix) | < 30 minutes (automated diagnosis via break-glass playbooks) | AAP job history: time from failure detection to service restoration |

<h2 id="summary"></h2>

## Summary

This guide demonstrated five use cases for implementing Zero Trust Architecture with Ansible Automation Platform as the central orchestration layer:

1. 🔍 **Infrastructure Integration** — Automated verification of identity, secrets, policy, and CMDB components
2. 🔑 **Just-In-Time Credentials** — Dynamic database credentials with automatic expiration (5-minute TTL)
3. 🛡️ **Platform-Level Policy Enforcement** — AAP Policy as Code blocks unauthorized launches with no bypass possible
4. 🔐 **Workload Identity Verification** — SPIFFE/SPIRE cryptographically proves automation platform legitimacy
5. 🔒 **Defense-in-Depth Access Control** — Four independent layers with tested break-glass recovery

**Measured Business Impact:**

- ✅ **80% reduction** in manual security operations through automation
- ✅ **95% reduction** in credential compromise risk through short-lived credentials
- ✅ **Continuous compliance** through unified audit trails across all components

Organizations implementing this architecture eliminate standing credentials, enforce deny-by-default policies at multiple layers, and automate the coordination of identity, secrets, policy, and network controls -- transforming Zero Trust from a conceptual framework into an operational reality.

---

<h2 id="related-guides"></h2>

## Related Guides

### Prerequisite Guides

-  [AI Infrastructure Automation with Ansible](README-IA.md) — Deploy and configure AI inference endpoints used in advanced AIOps integrations
-  [Network Device Backup and Configuration Management](https://github.com/network-automation/backup-config) — Foundation for network automation workflows

### Complementary Guides

-  [AIOps Automation with Ansible — Splunk ITSI Integration](README-AIOps-Splunk-ITSI.md) — Extend SIEM integration with AI-driven anomaly detection and automated remediation
-  [Event-Driven Ansible with ServiceNow](README-AIOps-ServiceNow.md) — Add ITSM ticket enrichment and bi-directional sync to ZTA workflows
-  [Intelligent Assistant with RHAIIS](README-Intelligent-Assistant-RHAIIS.md) — Natural language interface for querying ZTA policy decisions and audit trails

### Advanced Expansions

-  <a target="_blank" href="https://spiffe.io/docs/latest/spire/using/">Kubernetes Multi-Cluster Security with SPIFFE</a> — Extend workload identity to containerized applications
-  <a target="_blank" href="https://developer.hashicorp.com/vault/docs/enterprise/namespaces">HashiCorp Vault Enterprise Namespaces</a> — Multi-tenant secrets management for large-scale deployments
-  <a target="_blank" href="https://www.openpolicyagent.org/docs/latest/policy-language/">Open Policy Agent — Advanced Rego Patterns</a> — Custom policy authoring and testing

---

**Sources and Further Reading:**

-  <a target="_blank" href="https://csrc.nist.gov/publications/detail/sp/800-207/final">NIST SP 800-207: Zero Trust Architecture</a>
-  <a target="_blank" href="https://www.redhat.com/en/technologies/management/ansible">Red Hat Ansible Automation Platform</a>
-  <a target="_blank" href="https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html/installing_identity_management/">Red Hat Identity Management (IdM)</a>
-  <a target="_blank" href="https://www.vaultproject.io/">HashiCorp Vault</a>
-  <a target="_blank" href="https://www.openpolicyagent.org/">Open Policy Agent</a>
-  <a target="_blank" href="https://spiffe.io/">SPIFFE/SPIRE</a>
-  <a target="_blank" href="https://netbox.dev/">Netbox</a>
-  <a target="_blank" href="https://www.arista.com/en/products/software-controlled-container-networking">Arista cEOS</a>

---

## Next Steps

| | |
|---|---|
| <a target="_blank" href="https://www.redhat.com/en/technologies/management/ansible/trial"><strong>Try Ansible Automation Platform</strong></a> | Start a free 60-day trial and build your first Zero Trust automation workflows |
| <a target="_blank" href="https://github.com/nmartins0611/zta-workshop-aap"><strong>ZTA Workshop Source Code</strong></a> | Complete playbooks, OPA policies, and configuration for all five use cases |
| <a target="_blank" href="https://www.redhat.com/en/services/consulting"><strong>Red Hat Consulting</strong></a> | Work with Red Hat experts to design and deploy Zero Trust Architecture at scale |
| <a target="_blank" href="https://www.redhat.com/en/services/training-and-certification"><strong>Training and Certification</strong></a> | Build team skills with hands-on security automation courses |

---

<span class="guide-closing-logo-set">


</span>
