# 2. System requirements
## 2.5. Automation hub system requirements




With Automation hub you can discover and use new certified automation content from Red Hat Ansible and Certified Partners.

On Ansible automation hub, you can discover and manage Ansible Collections, which are supported automation content developed by Red Hat and its partners for use cases such as cloud automation, network automation, and security automation.

Note
Private automation hub

If you install private automation hub from an internal address with a certificate that only encompasses the external address, this can result in an installation that cannot be used as container registry without certificate issues.

To avoid this, use the `automationhub_main_url` inventory variable with a value such as https://pah.example.com linking to the private automation hub node in the installation inventory file.

This adds the external address to `/etc/pulp/settings.py` . This implies that you only want to use the external address.

For information about inventory file variables, see [Inventory file variables](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/rpm_installation/index#appendix-inventory-files-vars) .



