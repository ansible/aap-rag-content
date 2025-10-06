# 3. Configuring Ansible Automation Platform to use egress proxy
## 3.1. Overview




The egress proxy should be configured on the system and component level of Ansible Automation Platform, for all the RPM and containerized installation methods. For containerized installers, the system proxy configuration for podman on the nodes solves most of the problems with access through the proxy. For RPM installation, both system and component configurations are needed.

