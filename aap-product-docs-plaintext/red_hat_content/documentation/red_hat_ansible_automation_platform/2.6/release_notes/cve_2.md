# 9. Patch releases
## 9.2. Ansible Automation Platform patch release March 25, 2026
### 9.2.5. CVE

#### 9.2.5.1. Ansible Automation Platform UI

- [CVE-2026-29074](https://access.redhat.com/security/cve/cve-2026-29074) - SVGO denial of service via XML entity expansion in:


- `automation-platform-ui`. AAP-68529
- `gateway-rhel9` image. AAP-68526

- [CVE-2026-27904](https://access.redhat.com/security/cve/cve-2026-27904) - Minimatch denial of service via catastrophic backtracking in glob expressions in:


- `automation-platform-ui`. AAP-66695

- [CVE-2025-69873](https://access.redhat.com/security/cve/cve-2026-69873) - Regular expression denial of service (ReDoS) via `$data` references in:


- `automation-platform-ui` for Ansible Automation Platform 2.6. AAP-65713
- `gateway-rhel9` image. AAP-65711
- `lightspeed-rhel9`. AAP-66655

- [CVE-2026-25639](https://access.redhat.com/security/cve/cve-2026-25639) - Axios denial of service via `proto` handling in mergeConfig in:


- `automation-platform-ui`. AAP-65475
- `gateway-rhel9` image. AAP-65472
- `ansible-lightspeed-rhel9`. AAP-65473

#### 9.2.5.2. Automation gateway

- [CVE-2025-68121](https://access.redhat.com/security/cve/cve-2026-68121) - Unexpected session resumption in Go `crypto/tls` in:


- `automation-gateway-proxy` for Ansible Automation Platform 2.6. AAP-65695

- [CVE-2025-61726](https://access.redhat.com/security/cve/cve-2026-61726) - Memory exhaustion via query parameter parsing in Go `net/url` in:


- `automation-gateway-proxy` for Ansible Automation Platform 2.6. AAP-64902

#### 9.2.5.3. Red Hat Lightspeed / MCP / RAG

- [CVE-2026-30922](https://access.redhat.com/security/cve/cve-2026-30922) - pyasn1 denial of service via unbounded recursion in:


- `lightspeed-chatbot-rhel9` image for Ansible Automation Platform 2.6. AAP-69040

- [CVE-2026-28498](https://access.redhat.com/security/cve/cve-2026-28498) - Authlib authentication bypass via forged OpenID Connect ID tokens in:


- `lightspeed-chatbot-rhel9` image for Ansible Automation Platform 2.6. AAP-68686

- [CVE-2026-28802](https://access.redhat.com/security/cve/cve-2026-28802) - Authlib signature verification bypass allowing unauthorized access via malicious JWTs in:


- `lightspeed-chatbot-rhel9` image. AAP-67503

- [CVE-2026-25990](https://access.redhat.com/security/cve/cve-2026-25990) - Pillow out-of-bounds write via specially crafted PSD images in:


- `lightspeed-chatbot-rhel9`. AAP-65506
- `hub-rhel9`. AAP-65505

- [CVE-2026-26007](https://access.redhat.com/security/cve/cve-2026-26007) - cryptography subgroup attack due to missing subgroup validation for SECT curves in:


- `mcp-tools-rhel9`. AAP-65412
- `lightspeed-rhel9`. AAP-65411
- `lightspeed-chatbot-rhel9`. AAP-65410

- [CVE-2026-1615](https://access.redhat.com/security/cve/cve-2026-1615) - jsonpath arbitrary code execution via unsafe JSON Path evaluation in:


- `lightspeed-service-container`. AAP-65224

- [CVE-2025-69223](https://access.redhat.com/security/cve/cve-2026-69223) - AIOHTTP HTTP parser auto_decompress vulnerability exploitable with zip bombs in:


- `lightspeed-chatbot-rhel9`. AAP-61921

- [CVE-2026-30827](https://access.redhat.com/security/cve/cve-2026-30827) - express-rate-limit denial of service for IPv4 clients due to incorrect IPv6 subnet masking in:


- `mcp-server-rhel9`. AAP-67735

#### 9.2.5.4. Pillow / Image processing

- [CVE-2026-25990](https://access.redhat.com/security/cve/cve-2026-25990) - Out-of-bounds write via specially crafted PSD images in:


- `hub-rhel9`. AAP-65505

