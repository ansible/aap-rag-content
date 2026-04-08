# 5. Automation mesh nodes
## 5.2. Network ports




Automation mesh uses several ports to communicate with its services. These ports must be open and available for Red Hat Ansible Automation Platform to work. Ensure that these ports are available and are not blocked by a firewall.


<span id="idm140264419049808"></span>
**Table 5.1. Network ports and protocols**

| Port number | Protocol | Service | Source | Destination |
| --- | --- | --- | --- | --- |
| 80/443 | HTTP/HTTPS | Receptor | Execution node | OpenShift Container Platform mesh ingress |
| 80/443 | HTTP/HTTPS | Receptor | Hop node | OpenShift Container Platform mesh ingress |
| 27199 | TCP | Receptor | OpenShift Container Platform cluster | Execution node |
| 27199 | TCP | Receptor | OpenShift Container Platform cluster | Hop node |




# Appendix A. Additional resources for tested deployment models




Additional resources provide information and support for the tested deployment models outlined in Tested deployment models.

- For additional information about each of the tested topologies, see the [test-topologies GitHub repo](https://github.com/ansible/test-topologies/) .
- For questions around IBM cloud specific configurations or issues, see [IBM support](https://www.ibm.com/mysupport) .



<span id="idm140264418378896"></span>
# Legal Notice

Copyright© Red Hat.
Except as otherwise noted below, the text of and illustrations in this documentation are licensed by Red Hat under the Creative Commons Attribution–Share Alike 3.0 Unported license . If you distribute this document or an adaptation of it, you must provide the URL for the original version.
Red Hat, as the licensor of this document, waives the right to enforce, and agrees not to assert, Section 4d of CC-BY-SA to the fullest extent permitted by applicable law.
Red Hat, the Red Hat logo, JBoss, Hibernate, and RHCE are trademarks or registered trademarks of Red Hat, LLC. or its subsidiaries in the United States and other countries.
Linux® is the registered trademark of Linus Torvalds in the United States and other countries.
XFS is a trademark or registered trademark of Hewlett Packard Enterprise Development LP or its subsidiaries in the United States and other countries.
TheOpenStack® Word Mark and OpenStack logo are trademarks or registered trademarks of the Linux Foundation, used under license.
All other trademarks are the property of their respective owners.





