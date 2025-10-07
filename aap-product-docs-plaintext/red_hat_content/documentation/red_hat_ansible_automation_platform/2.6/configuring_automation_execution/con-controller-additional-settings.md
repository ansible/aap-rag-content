# 2. Automation controller configuration
## 2.5. Additional settings for automation controller




There are additional advanced settings that can affect automation controller behavior that are not available in the automation controller UI.

For traditional virtual machine based deployments, these settings can be provided to automation controller by creating a file in `/etc/tower/conf.d/custom.py` . When settings are provided to automation controller through file-based settings, the settings file must be present on all control plane nodes. These include all of the hybrid or control type nodes in the `automationcontroller` group in the installer inventory.

For these settings to be effective, restart the service with `automation-controller-service` restart on each node with the settings file. If the settings provided in this file are also visible in the automation controller UI, then they are marked as "Read only" in the UI.

For container-based installations, use `controller_extra_settings` in the [Automation controller variables](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/containerized_installation/appendix-inventory-files-vars#controller-variables) . The containerized version does not support `custom.py` .

