# 9. Patch releases
## 9.1. Ansible Automation Platform patch release May 4, 2026
### 9.1.4. CVE

#### 9.1.4.1. General

- CVE-2026-6266: Account hijacking and unauthorized access via unverified email linking. This affects the following components:


- `automation-controller` for Ansible Automation Platform 2.5 and 2.6.
- `automation-gateway` for Ansible Automation Platform 2.5 and 2.6.
- `python3.12-django-ansible-base` for Ansible Automation Platform 2.5 and 2.6.
- `ansible-automation-platform-26/controller-rhel9` for Ansible Automation Platform 2.6 only.
- `ansible-automation-platform-26/gateway-rhel9` for Ansible Automation Platform 2.6 only.

#### 9.1.4.2. Automation execution environments

- [CVE-2026-23490](https://access.redhat.com/security/cve/cve-2026-23490) - pyasn1: Denial of Service due to memory exhaustion from malformed RELATIVE-OID in:


- ansible-automation-platform-26/ee-supported-rhel9 for Ansible Automation Platform 2.6. AAP-72593

- [CVE-2026-27459](https://access.redhat.com/security/cve/cve-2026-27459) - pyOpenSSL: DTLS cookie callback buffer overflow in:


- ansible-automation-platform-26/ee-supported-rhel9 for Ansible Automation Platform 2.6. AAP-68956

- [CVE-2026-32274](https://access.redhat.com/security/cve/cve-2026-32274) - Black: Arbitrary file writes from unsanitized user input in cache file name in:


- ansible-automation-platform-26/ee-minimal-rhel9 for Ansible Automation Platform 2.6. AAP-68419

- [CVE-2026-32597](https://access.redhat.com/security/cve/cve-2026-32597) - PyJWT accepts unknown crit header extensions (RFC 7515 §4.1.11 MUST violation) in:


- ansible-automation-platform-26/ee-supported-rhel9 for Ansible Automation Platform 2.6. AAP-68399

#### 9.1.4.3. Automation controller

- [CVE-2025-14550](https://access.redhat.com/security/cve/cve-2026-14550) - Django: Denial of Service via crafted request with duplicate headers in:


- automation-controller for Ansible Automation Platform 2.6. AAP-64818

- [CVE-2025-69534](https://access.redhat.com/security/cve/cve-2026-69534) - markdown: Denial of Service via malformed HTML-like sequences in:


- automation-controller for Ansible Automation Platform 2.6. AAP-67446

- [CVE-2026-26007](https://access.redhat.com/security/cve/cve-2026-26007) - cryptography: Subgroup Attack due to missing subgroup validation for SECT curves in:


- automation-controller for Ansible Automation Platform 2.6. AAP-65413

- [CVE-2026-27459](https://access.redhat.com/security/cve/cve-2026-27459) - pyOpenSSL: DTLS cookie callback buffer overflow in:


- automation-controller for Ansible Automation Platform 2.6. AAP-68960

- [CVE-2026-32597](https://access.redhat.com/security/cve/cve-2026-32597) - PyJWT accepts unknown crit header extensions (RFC 7515 §4.1.11 MUST violation) in:


- automation-controller for Ansible Automation Platform 2.6. AAP-68405

#### 9.1.4.4. Automation hub

- [CVE-2026-27459](https://access.redhat.com/security/cve/cve-2026-27459) - pyOpenSSL: DTLS cookie callback buffer overflow in:


- ansible-automation-platform-26/hub-rhel9 for Ansible Automation Platform 2.6. AAP-68957

- [CVE-2026-32274](https://access.redhat.com/security/cve/cve-2026-32274) - Black: Arbitrary file writes from unsanitized user input in cache file name in:


- ansible-automation-platform-26/hub-rhel9 for Ansible Automation Platform 2.6. AAP-68421

- [CVE-2026-32597](https://access.redhat.com/security/cve/cve-2026-32597) - PyJWT accepts unknown crit header extensions (RFC 7515 §4.1.11 MUST violation) in:


- ansible-automation-platform-26/hub-rhel9 for Ansible Automation Platform 2.6. AAP-68401

#### 9.1.4.5. Platform gateway

- [CVE-2026-27459](https://access.redhat.com/security/cve/cve-2026-27459) - pyasn1: Denial of Service via unbounded recursion in ASN.1 decoding in:


- ansible-automation-platform-26/gateway-rhel9 for Ansible Automation Platform 2.6. AAP-69035

- [CVE-2026-27606](https://access.redhat.com/security/cve/cve-2026-27606) - Rollup: Remote Code Execution via Path Traversal Vulnerability in:


- ansible-automation-platform-26/gateway-rhel9 for Ansible Automation Platform 2.6. AAP-66536

- [CVE-2026-29074](https://access.redhat.com/security/cve/cve-2026-29074) - SVGO: Denial of Service via XML entity expansion in:


- automation-gateway for Ansible Automation Platform 2.6. AAP-68531

- [CVE-2026-32597](https://access.redhat.com/security/cve/cve-2026-32597) - PyJWT accepts unknown crit header extensions (RFC 7515 §4.1.11 MUST violation) in:


- ansible-automation-platform-26/gateway-rhel9 for Ansible Automation Platform 2.6. AAP-68400

- [CVE-2026-33154](https://access.redhat.com/security/cve/cve-2026-33154) - Dynaconf: Arbitrary code execution via Server-Side Template Injection in:


- ansible-automation-platform-26/gateway-rhel9 for Ansible Automation Platform 2.6. AAP-69466

#### 9.1.4.6. Ansible Automation Platform UI

- [CVE-2026-26996](https://access.redhat.com/security/cve/cve-2026-26996) - minimatch: Denial of Service via specially crafted glob patterns in:


- automation-platform-ui for Ansible Automation Platform 2.6. AAP-66292

- [CVE-2026-27606](https://access.redhat.com/security/cve/cve-2026-27606) - Rollup: Remote Code Execution via Path Traversal Vulnerability in:


- automation-platform-ui for Ansible Automation Platform 2.6. AAP-66535

#### 9.1.4.7. Event-Driven Ansible

- [CVE-2026-24049](https://access.redhat.com/security/cve/cve-2026-24049) - wheel: Privilege escalation or arbitrary code execution via malicious wheel file unpacking in:


- ansible-automation-platform-26/eda-controller-rhel9-operator for Ansible Automation Platform 2.6. AAP-63863

- [CVE-2026-26007](https://access.redhat.com/security/cve/cve-2026-26007) - cryptography: Subgroup Attack due to missing subgroup validation for SECT curves in:


- ansible-automation-platform-26/eda-controller-rhel9 for Ansible Automation Platform 2.6. AAP-65406

- [CVE-2026-27459](https://access.redhat.com/security/cve/cve-2026-27459) - pyOpenSSL: DTLS cookie callback buffer overflow in:


- ansible-automation-platform-26/eda-controller-rhel9 for Ansible Automation Platform 2.6. AAP-68954

- [CVE-2026-30922](https://access.redhat.com/security/cve/cve-2026-30922) - pyasn1: Denial of Service via unbounded recursion in:


- ansible-automation-platform-26/eda-controller-rhel9 for Ansible Automation Platform 2.6. AAP-69032

- [CVE-2026-32597](https://access.redhat.com/security/cve/cve-2026-32597) - PyJWT accepts unknown crit header extensions (RFC 7515 §4.1.11 MUST violation) in:


- ansible-automation-platform-26/eda-controller-rhel9 for Ansible Automation Platform 2.6. AAP-68398

- [CVE-2026-33154](https://access.redhat.com/security/cve/cve-2026-33154) - Dynaconf: Arbitrary code execution via Server-Side Template Injection in:


- ansible-automation-platform-26/eda-controller-rhel9 for Ansible Automation Platform 2.6. AAP-69465

#### 9.1.4.8. Red Hat Ansible Lightspeed

- [CVE-2025-69227](https://access.redhat.com/security/cve/cve-2025-69227) - aiohttp: Denial of Service via specially crafted POST request in:


- ansible-automation-platform/ansible-lightspeed-service-container(2.6) for Ansible Automation Platform 2.6. AAP-65586
- ansible-automation-platform/ansible-lightspeed-chatbot-container(2.6) for Ansible Automation Platform 2.6. AAP-65585

- [CVE-2025-69228](https://access.redhat.com/security/cve/cve-2025-69228) - aiohttp: Denial of Service via memory exhaustion from crafted POST request in:


- ansible-automation-platform-26/ansible-lightspeed-service-container(2.6) for Ansible Automation Platform 2.6. AAP-65629
- ansible-automation-platform/ansible-lightspeed-chatbot-container(2.6) for Ansible Automation Platform 2.6. AAP-65627

- [CVE-2026-0598](https://access.redhat.com/security/cve/cve-2026-0598) - Broken Object Level Authorization leading to cross-user AI conversation context injection in:


- ansible-automation-platform/ansible-wisdom-service for Ansible Automation Platform 2.6. AAP-64145

- [CVE-2026-26007](https://access.redhat.com/security/cve/cve-2026-26007) - cryptography: Subgroup Attack due to missing subgroup validation for SECT curves in:


- ansible-automation-platform-26/mcp-tools-rhel9 for Ansible Automation Platform 2.6. AAP-71204
- ansible-automation-platform-26/lightspeed-rhel9 for Ansible Automation Platform 2.6. AAP-71203
- ansible-automation-platform-26/lightspeed-chatbot-rhel9 for Ansible Automation Platform 2.6. AAP-71202

- [CVE-2026-27459](https://access.redhat.com/security/cve/cve-2026-27459) - pyOpenSSL: DTLS cookie callback buffer overflow in:


- ansible-automation-platform-26/lightspeed-rhel9 for Ansible Automation Platform 2.6. AAP-68958

- [CVE-2026-29074](https://access.redhat.com/security/cve/cve-2026-29074) - SVGO: Denial of Service via XML entity expansion in:


- ansible-automation-platform-26/lightspeed-rhel9 for Ansible Automation Platform 2.6. AAP-68528

- [CVE-2026-30922](https://access.redhat.com/security/cve/cve-2026-30922) - pyasn1: Denial of Service via unbounded recursion in:


- ansible-automation-platform-26/lightspeed-rhel9 for Ansible Automation Platform 2.6. AAP-69041

- [CVE-2026-31812](https://access.redhat.com/security/cve/cve-2026-31812) - quinn-proto: Denial of Service via crafted QUIC Initial packet in:


- ansible-automation-platform-26/lightspeed-chatbot-rhel9 for Ansible Automation Platform 2.6. AAP-68140

- [CVE-2026-32597](https://access.redhat.com/security/cve/cve-2026-32597) - PyJWT accepts unknown crit header extensions (RFC 7515 §4.1.11 MUST violation) in:


- ansible-automation-platform-26/mcp-tools-rhel9 for Ansible Automation Platform 2.6. AAP-68404
- ansible-automation-platform-26/lightspeed-rhel9 for Ansible Automation Platform 2.6. AAP-68403
- ansible-automation-platform-26/lightspeed-chatbot-rhel9 for Ansible Automation Platform 2.6. AAP-68402

- [CVE-2026-33154](https://access.redhat.com/security/cve/cve-2026-33154) - Dynaconf: Arbitrary code execution via Server-Side Template Injection in:


- ansible-automation-platform-26/lightspeed-rhel9 for Ansible Automation Platform 2.6. AAP-69468

- [CVE-2026-39373](https://access.redhat.com/security/cve/cve-2026-39373) - JWCrypto: Memory exhaustion via crafted compressed JWE tokens in:


- ansible-automation-platform-26/lightspeed-rhel9 for Ansible Automation Platform 2.6. AAP-71150

- [CVE-2026-4800](https://access.redhat.com/security/cve/cve-2026-4800) - lodash: Arbitrary code execution via untrusted input in template imports in:


- ansible-automation-platform-26/lightspeed-rhel9 for Ansible Automation Platform 2.6. AAP-70458

#### 9.1.4.9. Ansible Automation Platform security

- [CVE-2026-35029](https://access.redhat.com/security/cve/cve-2026-35029) - LiteLLM: Remote code execution and privilege escalation via unrestricted proxy configuration endpoint in:


- redhat-user-workloads/lightspeed-chatbot-rhel9 for Ansible Automation Platform 2.6. AAP-70909

- [CVE-2026-35030](https://access.redhat.com/security/cve/cve-2026-35030) - LiteLLM: Authentication bypass and privilege escalation via OIDC userinfo cache key collision in:


- redhat-user-workloads/lightspeed-chatbot-rhel9 for Ansible Automation Platform 2.6. AAP-70913

- [CVE-2026-4926](https://access.redhat.com/security/cve/cve-2026-4926) - path-to-regexp: Denial of Service via crafted regular expressions in:


- ansible-automation-platform-tech-preview/mcp-server-rhel9 for Ansible Automation Platform 2.6. AAP-70022

#### 9.1.4.10. Receptor

- [CVE-2026-25679](https://access.redhat.com/security/cve/cve-2026-25679) - Incorrect parsing of IPv6 host literals in net/url in:


- ansible-automation-platform-26/receptor-rhel9 for Ansible Automation Platform 2.6. AAP-68747
- receptor for Ansible Automation Platform 2.6. AAP-68731

- [CVE-2026-27137](https://access.redhat.com/security/cve/cve-2026-27137) - Incorrect enforcement of email constraints in crypto/x509 in:


- ansible-automation-platform-26/receptor-rhel9 for Ansible Automation Platform 2.6. AAP-68737

