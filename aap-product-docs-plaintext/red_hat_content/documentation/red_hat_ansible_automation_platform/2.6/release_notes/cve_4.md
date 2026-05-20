# 9. Patch releases
## 9.4. Ansible Automation Platform patch release January 21, 2026
### 9.4.1. CVE

With this update, the following CVEs have been addressed:

- [CVE-2025-69223](https://access.redhat.com/security/cve/cve-2025-69223) `automation-controller`: AIOHTTP’s HTTP Parser auto_decompress feature is vulnerable to zip bomb.(AAP-61927)
- [CVE-2025-69223](https://access.redhat.com/security/cve/cve-2025-69223) `ansible-automation-platform-26/controller-rhel9`: AIOHTTP’s HTTP Parser auto_decompress feature is vulnerable to zip bomb.(AAP-61915)
- [CVE-2025-4565](https://access.redhat.com/security/cve/cve-2025-4565) `python3.11-protobuf`: Unbounded recursion in Python Protobuf.(AAP-60498)
- [CVE-2025-66031](https://access.redhat.com/security/cve/cve-2025-66031) `ansible-ai-connect-service`: `node-forge` ASN.1 Unbounded Recursion.(AAP-59983)
- [CVE-2025-66416](https://access.redhat.com/security/cve/cve-2025-66416) `ansible-automation-platform-26/mcp-tools-rhel9`: DNS Rebinding Protection Disabled by Default in Model Context Protocol PythonSDK.(AAP-59952)
- [CVE-2025-64459](https://access.redhat.com/security/cve/cve-2025-64459) `ansible-automation-platform-26/hub-rhel9`: Django SQL injection.(AAP-58111)
- [CVE-2025-53643](https://access.redhat.com/security/cve/cve-2025-53643) `automation-controller`: AIOHTTP HTTP Request/Response Smuggling.(AAP-54877)
- [CVE-2025-61729](https://access.redhat.com/security/cve/cve-2025-61729) `ansible-automation-platform-26/receptor-rhel9`: Excessive resource consumption when printing error string for host certificate validation in `crypto/x509`.(AAP-61230)
- [CVE-2025-64460](https://access.redhat.com/security/cve/cve-2025-64460) `python3.11-django`: `Django`: Algorithmic complexity in XML deserializer leads to denial of service.(AAP-61780)
- [CVE-2025-64460](https://access.redhat.com/security/cve/cve-2025-64460) `automation-controller`: `Django`: Algorithmic complexity in XML Deserializer leads to denial of service.(AAP-60961)
- [CVE-2026-21441](https://access.redhat.com/security/cve/cve-2026-21441) `ansible-automation-platform-26/lightspeed-rhel9`: `urllib3` vulnerable to decompression-bomb safeguard bypass when following HTTP redirects (streaming API).(AAP-62341)
- [CVE-2025-66471](https://access.redhat.com/security/cve/cve-2025-66471) `python3.11-urllib3`: `urllib3` streaming API improperly handles highly compressed data.(AAP-62290)
- [CVE-2025-66471](https://access.redhat.com/security/cve/cve-2025-66471) `python3.11-urllib3`: `urllib3` Streaming API improperly handles highly compressed data.(AAP-62290)
- [CVE-2025-66471](https://access.redhat.com/security/cve/cve-2025-66471) `automation-controller`: `urllib3` Streaming API improperly handles highly compressed data.(AAP-62090)
- [CVE-2025-66471](https://access.redhat.com/security/cve/cve-2025-66471) `ansible-automation-platform-26/controller-rhel9`: `urllib3` Streaming API improperly handles highly compressed data.(AAP-62068)
- [CVE-2025-66471](https://access.redhat.com/security/cve/cve-2025-66471) `ansible-automation-platform-25/lightspeed-rhel8`: `urllib3`: Streaming API improperly handles highly compressed data.(AAP-62030)
- [CVE-2025-66471](https://access.redhat.com/security/cve/cve-2025-66471) `ansible-automation-platform-26/mcp-tools-rhel9`: `urllib3` Streaming API improperly handles highly compressed data.(AAP-62085)
- [CVE-2025-66471](https://access.redhat.com/security/cve/cve-2025-66471) `ansible-automation-platform-26/lightspeed-rhel9-operator`: `urllib3` Streaming API improperly handles highly compressed data.(AAP-62084)
- [CVE-2025-66471](https://access.redhat.com/security/cve/cve-2025-66471) `ansible-automation-platform-26/lightspeed-rhel9`: `urllib3` Streaming API improperly handles highly compressed data.(AAP-62083)
- [CVE-2025-66471](https://access.redhat.com/security/cve/cve-2025-66471) `ansible-automation-platform-26/lightspeed-chatbot-rhel9`: `urllib3` Streaming API improperly handles highly compressed data.(AAP-62082)
- [CVE-2025-66471](https://access.redhat.com/security/cve/cve-2025-66471) `ansible-automation-platform-26/controller-rhel9-operator`: `urllib3` Streaming API improperly handles highly compressed data.(AAP-62069)
- [CVE-2025-61729](https://access.redhat.com/security/cve/cve-2025-61729) `receptor`: Excessive resource consumption when printing error string for host certificate validation in `crypto/x509`.(AAP-61235)
- [CVE-2025-62706](https://access.redhat.com/security/cve/cve-2025-62706) `ansible-automation-platform-26/lightspeed-chatbot-rhel9`: `Authlib`: JWE `zip=DEF` decompression bomb enables DoS.(AAP-60596)
- [CVE-2025-66471](https://access.redhat.com/security/cve/cve-2025-66471) ``ansible-automation-platform-26/gateway-rhel9: `urllib3`` Streaming API improperly handles highly compressed data.(AAP-62077)
- [CVE-2025-66471](https://access.redhat.com/security/cve/cve-2025-66471) `ansible-automation-platform-26/eda-controller-rhel9`: `urllib3` Streaming API improperly handles highly compressed data.(AAP-62072)
- [CVE-2025-66471](https://access.redhat.com/security/cve/cve-2025-66471) `ansible-automation-platform-26/de-supported-rhel9`: `urllib3` Streaming API improperly handles highly compressed data.(AAP-62071)
- [CVE-2025-66471](https://access.redhat.com/security/cve/cve-2025-66471) `ansible-automation-platform-26/de-minimal-rhel9`: `urllib3` Streaming API improperly handles highly compressed data.(AAP-62070)
- [CVE-2026-21441](https://access.redhat.com/security/cve/cve-2026-21441) `ansible-automation-platform-26/gateway-rhel9`: `urllib3` vulnerable to decompression-bomb safeguard bypass when following HTTP redirects (streaming API).(AAP-62446)
- [CVE-2026-21441](https://access.redhat.com/security/cve/cve-2026-21441) `ansible-automation-platform-26/eda-controller-rhel9`: `urllib3` vulnerable to decompression-bomb safeguard bypass when following HTTP redirects (streaming API).(AAP-62443)
- [CVE-2026-21441](https://access.redhat.com/security/cve/cve-2026-21441) `ansible-automation-platform-26/de-minimal-rhel9`: `urllib3` vulnerable to decompression-bomb safeguard bypass when following HTTP redirects (streaming API).(AAP-62383)
- [CVE-2025-69223](https://access.redhat.com/security/cve/cve-2025-69223) `ansible-automation-platform-26/de-supported-rhel9`: AIOHTTP’s HTTP Parser `auto_decompress` feature is vulnerable to zip bomb.(AAP-61917)
- [CVE-2025-69223](https://access.redhat.com/security/cve/cve-2025-69223) `ansible-automation-platform-26/de-minimal-rhel9`: AIOHTTP’s HTTP Parser `auto_decompress` feature is vulnerable to zip bomb.(AAP-61916)

