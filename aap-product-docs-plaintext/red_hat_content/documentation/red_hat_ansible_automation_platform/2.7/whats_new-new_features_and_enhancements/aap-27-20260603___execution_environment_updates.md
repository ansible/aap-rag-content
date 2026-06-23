# New features and enhancements
## Execution environment updates

- Ee-minimal
* Removed `ansible-lint`. If your infrastructure depends on
* , migrate to the Ansible Automation Platform Development Tools container.
* Removed :latest: convention for ee-minimal images. Users now need to identify the specific image and version to download.
- Ee-supported
* Removed `ansible-lint`. If your infrastructure depends on `ansible-lint`, migrate to the Ansible Automation Platform Development Tools container.
* Added microsoft.mecm and microsoft.hyperv collections.
* Updated existing collections to the most recent compatible versions.
* Removed the cloud.common, cloud.terraform, redhat.csp_download , redhat.rhv, and trendmicro.deepsec collections.
* Removed the junipernetworks-junos collection. Use the juniper.device collection instead.

