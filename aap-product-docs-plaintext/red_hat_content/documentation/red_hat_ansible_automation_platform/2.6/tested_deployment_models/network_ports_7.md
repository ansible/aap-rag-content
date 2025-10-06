# 5. Automation mesh nodes
## 5.2. Network ports




Automation mesh uses several ports to communicate with its services. These ports must be open and available for incoming connections to the Red Hat Ansible Automation Platform server for it to work. Ensure that these ports are available and are not blocked by the server firewall.


<span id="idm140627609344960"></span>
**Table 5.1. Network ports and protocols**

| Port number | Protocol | Service | Source | Destination |
| --- | --- | --- | --- | --- |
| 80/443 | HTTP/HTTPS | Receptor | Execution node | OpenShift Container Platform mesh ingress |
| 80/443 | HTTP/HTTPS | Receptor | Hop node | OpenShift Container Platform mesh ingress |
| 27199 | TCP | Receptor | OpenShift Container Platform cluster | Execution node |
| 27199 | TCP | Receptor | OpenShift Container Platform cluster | Hop node |




# Appendix A. Additional resources for tested deployment models




This appendix provides a reference for the additional resources relevant to the tested deployment models outlined in Tested deployment models.

- For additional information about each of the tested topologies described in this document, see the [test-topologies GitHub repo](https://github.com/ansible/test-topologies/) .
- For questions around IBM cloud specific configurations or issues, see [IBM support](https://www.ibm.com/mysupport) .



<span id="idm140627614450448"></span>
# Legal Notice

Copyright© 2025 Red Hat, Inc.
The text of and illustrations in this document are licensed by Red Hat under a Creative Commons Attribution–Share Alike 3.0 Unported license ("CC-BY-SA"). An explanation of CC-BY-SA is available at [http://creativecommons.org/licenses/by-sa/3.0/](http://creativecommons.org/licenses/by-sa/3.0/) . In accordance with CC-BY-SA, if you distribute this document or an adaptation of it, you must provide the URL for the original version.
Red Hat, as the licensor of this document, waives the right to enforce, and agrees not to assert, Section 4d of CC-BY-SA to the fullest extent permitted by applicable law.
Red Hat, Red Hat Enterprise Linux, the Shadowman logo, the Red Hat logo, JBoss, OpenShift, Fedora, the Infinity logo, and RHCE are trademarks of Red Hat, Inc., registered in the United States and other countries.
Linux® is the registered trademark of Linus Torvalds in the United States and other countries.
Java® is a registered trademark of Oracle and/or its affiliates.
XFS® is a trademark of Silicon Graphics International Corp. or its subsidiaries in the United States and/or other countries.
MySQL® is a registered trademark of MySQL AB in the United States, the European Union and other countries.
Node.js® is an official trademark of Joyent. Red Hat is not formally related to or endorsed by the official Joyent Node.js open source or commercial project.
TheOpenStack® Word Mark and OpenStack logo are either registered trademarks/service marks or trademarks/service marks of the OpenStack Foundation, in the United States and other countries and are used with the OpenStack Foundation's permission. We are not affiliated with, endorsed or sponsored by the OpenStack Foundation, or the OpenStack community.
All other trademarks are the property of their respective owners.





