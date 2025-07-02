# Chapter 2. Red Hat Edge Manager architecture




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


Learn more from the following sections:

-  [Red Hat Edge Manager agent and service](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/managing_device_fleets_with_the_red_hat_edge_manager/index#edge-manager-agent-service)
-  [Red Hat Edge Manager API server](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/managing_device_fleets_with_the_red_hat_edge_manager/index#edge-manager-api-server)


