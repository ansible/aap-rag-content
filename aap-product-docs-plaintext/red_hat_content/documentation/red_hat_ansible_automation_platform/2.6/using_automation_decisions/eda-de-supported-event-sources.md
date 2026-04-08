# 5. Decision environments
## 5.2. Supported event sources and filters




The capabilities of your decision environment are largely defined by the event sources and filters included in your container image. Event sources serve as the foundation for Event-Driven Ansible controller, determining where your rulebooks receive incoming signals.

Selecting compatible sources is critical for successful deployment, as availability can vary—some sources are exclusive to the web-based Event-Driven Ansible controller, while others are optimized for the `ansible-rulebook` command-line interface (CLI).

When building your decision environments, the `de-minimal` image provides a curated set of supported plugins designed to ensure stability and compatibility. However, as the ecosystem evolves, plugin namespaces have been updated to reflect their specific collection origins (for example, migrating from `ansible.eda` to specific cloud collections). To ensure your rulebooks remain functional, verify that your definitions align with the latest plugin naming conventions.

The following table lists the supported plugins in the `de-minimal` image, including their plugin type and any associated deprecated names:


<span id="idm139919144655472"></span>
**Table 5.1. Supported event sources and filters**

| Plugin name | Event filter | Deprecated name |
| --- | --- | --- |
|  ** `eda.builtin.dashes_to_underscores` ** | Event filter |  `ansible.eda.dashes_to_underscores` |
|  ** `eda.builtin.event_splitter` ** | Event filter |  |
|  ** `eda.builtin.generic` ** | Event source |  `ansible.eda.generic` |
|  ** `eda.builtin.insert_hosts_to_meta` ** | Event filter |  `ansible.eda.insert_hosts_to_meta` |
|  ** `eda.builtin.insert_meta_info` ** | Event filter |  |
|  ** `eda.builtin.json_filter` ** | Event filter |  `ansible.eda.json_filter` |
|  ** `eda.builtin.normalize_keys` ** | Event filter |  `ansible.eda.normalize_keys` |
|  ** `eda.builtin.pg_listener` ** | Event source |  `ansible.eda.pg_listener` |
|  ** `eda.builtin.range` ** | Event source |  `ansible.eda.range` |
|  ** `eda.builtin.webhook` ** | Event source |  `ansible.eda.webhook` |




The following event sources have been made available in dedicated collections. The original `ansible.eda` names are currently supported as deprecated plugins in `de-minimal` , but you must transition to the new `de-supported` versions to ensure long-term compatibility and overall improvements:


<span id="idm139919146355776"></span>
**Table 5.2. `de-supported` event sources**

| Event source (in `de-supported`) | Deprecated name (in `de-minimal`) |
| --- | --- |
|  ** `amazon.aws.aws_cloudtrail` ** |  `ansible.eda.aws_cloudtrail` |
|  ** `amazon.aws.aws_sqs_queue` ** |  `ansible.eda.aws_sqs_queue` |
|  ** `azure.azcollection.azure_service_bus` ** |  `ansible.eda.azure_service_bus` |




In addition, the `de-minimal` image currently provides event sources that are not supported, and will be removed in a future release:

-  `    ansible.eda.file`
-  `    ansible.eda.file_watch`
-  `    ansible.eda.journald`
-  `    ansible.eda.tick`
-  `    ansible.eda.url_check`


