# 10. Patch releases
## 10.7. Ansible Automation Platform patch release May 28, 2025
### 10.7.2. Features




#### 10.7.2.1. Ansible Automation Platform




- Ansible Automation Platform now supports service account-based authentication for integration with services available through the Hybrid Cloud Console, including automation analytics, Insights for Ansible Automation Platform, and subscription management. See this [Knowledgebase article](https://access.redhat.com/articles/7112649) for more information on the required changes.
- Replaced basic authenticate with service account authentication for Ansible Automation Platform subscription management.(AAP-44643)
- Updated the subscription wizard to accommodate fetching subscription information using service account credentials.(AAP-37077)
- Adds `    ansible_base.lib.utils.address.classify_address` providing common recognition and parsing of machine addressing (hostname, IPv4 and IPv6) with and without an appended `    :&lt;port&gt;` .(AAP-45287)


