# 6. Network ports and protocols
## 6.3. Network ports and protocols firewalls




The following tables provide information about configuring firewalls for Red Hat Ansible Automation Platform components.

**Red Hat Lightspeed for Red Hat Ansible Automation Platform**

| URL | Required for |
| --- | --- |
|  [https://api.access.redhat.com:443](https://api.access.redhat.com) | General account services, subscriptions |
|  [https://cert-api.access.redhat.com:443](https://cert-api.access.redhat.com) | Insights data upload |
|  [https://cert.console.redhat.com:443](https://cert.console.redhat.com) | Inventory upload and Cloud Connector connection |
|  [https://console.redhat.com:443](https://console.redhat.com) | Access to Insights dashboard |


**Automation Hub**

| URL | Required for |
| --- | --- |
|  [https://console.redhat.com:443](https://console.redhat.com) | General account services, subscriptions |
|  [https://catalog.redhat.com:443](https://catalog.redhat.com) | Indexing execution environments |
|  [https://sso.redhat.com:443](https://sso.redhat.com) | TCP |
| https://automation-hub-prd.s3.amazonaws.com, https://automation-hub-prd.s3.us-east-2.amazonaws.com | Firewall access |
|  [https://galaxy.ansible.com:443](https://galaxy.ansible.com) | Ansible Community curated Ansible content |
| https://ansible-galaxy-ng.s3.dualstack.us-east-1.amazonaws.com | Dual Stack IPv6 endpoint for Community curated Ansible content repository |
|  [https://registry.redhat.io:443](https://registry.redhat.io) | Access to container images provided by Red Hat and partners |
|  [https://cert.console.redhat.com:443](https://cert.console.redhat.com) | Red Hat and partner curated Ansible Collections |


**Execution Environments (EE)**

| URL | Required for |
| --- | --- |
|  [https://registry.redhat.io:443](https://registry.redhat.io) | Access to container images provided by Red Hat and partners |
|  `cdn.quay.io:443` | Access to container images provided by Red Hat and partners |
|  `cdn01.quay.io:443` | Access to container images provided by Red Hat and partners |
|  `cdn02.quay.io:443` | Access to container images provided by Red Hat and partners |
|  `cdn03.quay.io:443` | Access to container images provided by Red Hat and partners |


Important
As of **April 1st, 2025** , `quay.io` is adding three additional endpoints. As a result, customers must adjust allow/block lists within their firewall systems lists to include the following endpoints:

-  `    cdn04.quay.io`
-  `    cdn05.quay.io`
-  `    cdn06.quay.io`


To avoid problems pulling container images, customers must allow outbound TCP connections (ports 80 and 443) to the following hostnames:

-  `    cdn.quay.io`
-  `    cdn01.quay.io`
-  `    cdn02.quay.io`
-  `    cdn03.quay.io`
-  `    cdn04.quay.io`
-  `    cdn05.quay.io`
-  `    cdn06.quay.io`


This change should be made to any firewall configuration that specifically enables outbound connections to `registry.redhat.io` or `registry.access.redhat.com` .

Use the hostnames instead of IP addresses when configuring firewall rules.

After making this change, you can continue to pull images from `registry.redhat.io` or `registry.access.redhat.com` . You do not require a `quay.io` login, or need to interact with the `quay.io` registry directly in any way to continue pulling Red Hat container images.

For more information, see [Firewall changes for container image pulls 2024/2025](https://access.redhat.com/articles/7084334) .



