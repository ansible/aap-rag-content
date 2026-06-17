+++
title = "Architecture - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/whats_new-assembly_edge_manager_architecture"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/whats_new-technology_preview/", "Technology Preview"]]
category = "What's new"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/whats_new-assembly_edge_manager_architecture/aem-page/whats_new-assembly_edge_manager_architecture.html"
last_crumb = "Architecture"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Architecture"
oversized = "false"
page_slug = "whats_new-assembly_edge_manager_architecture"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/whats_new-assembly_edge_manager_architecture"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/whats_new-assembly_edge_manager_architecture/toc/toc.json"
type = "aem-page"
+++

# Architecture

You can manage individual devices or an entire fleet by using the Red Hat Edge Manager. The Red Hat Edge Manager uses an agent-based architecture that allows for a scalable and robust device management, even with limited network conditions.

By deploying a Red Hat Edge Manager agent to a device, the agent autonomously manages and monitors the device while periodically communicating with the Red Hat Edge Manager service to check for new configurations and to report device status.

The Red Hat Edge Manager supports image-based operating systems. You can include the Red Hat Edge Manager agent and the agent configuration in the image that is distributed to the devices.

Image-based operating systems allow the agent to start a transactional update of the image and to roll back to the earlier version in case of an update error.

The Red Hat Edge Manager architecture has the following main features:

- Agent
- Service
- Image-based operating system
- API server
- Database
- Device
- Device fleet

## Agent and service

The Red Hat Edge Manager agent is a process running on each managed device that periodically communicates with the Red Hat Edge Manager service. The agent is responsible for the following tasks:

- Enrolling devices into the service
- Periodically checking with the service for changes in the device specification, such as changes to the operating system, configuration, and applications
- Applying any updates independently from the service
- Reporting status of the device and the applications


The Red Hat Edge Manager service is responsible for the following tasks:

- Authenticating and authorizing users and agents
- Enrolling devices
- Managing device inventory
- Reporting status from individual devices or fleets


The service also communicates with a database that stores the device inventory and the target device configuration. When communicating with the service, the agent polls the service for changes in the configuration. If the agent detects that the current configuration deviates from the target configuration, the agent attempts to apply the changes to the device.

When the agent receives a new target configuration from the service, the agent does the following tasks:

1. To avoid depending on network connectivity during the update, the agent downloads all required resources, such as the operating system image and application container images, over the network to disk.
2. The agent updates the operating system image by delegating to `bootc`.
3. The agent updates configuration files on the file system of the device by overlaying a set of files that the service sends to the device.
4. If necessary, the agent reboots into the new operating system. Otherwise, the agent signals system services and applications to reload the updated configuration.
5. The agent updates applications running on Podman.


If the update fails or the system does not return online after rebooting, the agent automatically rolls back to the earlier operating system image and configuration.

Note:

You can keep fleet definitions in Git. The Red Hat Edge Manager periodically syncs with the fleet definitions in the database.

## API server

The API server is a core part of the Red Hat Edge Manager service that gives users and agents an option to communicate with the service.

The API server exposes the following endpoints:

User-facing API endpoint
Users can connect to the user-facing API endpoint from the CLI or the web console. Users must authenticate on the platform gateway to obtain a JSON Web Token (JWT) to make HTTPS requests.

Agent-facing API endpoint
Agents connect to the agent-facing endpoint, which is mTLS-protected. The service authenticates devices by using the X.509 client certificates.

The Red Hat Edge Manager service also communicates with various external systems to authenticate and authorize users, get mTLS certificates signed, or query configuration for managed devices.
