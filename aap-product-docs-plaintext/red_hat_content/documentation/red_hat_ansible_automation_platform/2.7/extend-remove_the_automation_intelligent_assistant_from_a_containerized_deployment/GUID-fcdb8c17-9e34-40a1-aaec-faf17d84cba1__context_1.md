# Remove the automation intelligent assistant from a containerized deployment
## About this task

Note:

**Important**: To stop the chatbot as quickly as possible, complete step 1 first. Stopping the chatbot services immediately prevents the assistant from responding to user queries while you complete the remaining steps.

Note:

Re-running the installer with the chatbot configuration removed disconnects the chatbot from the platform gateway, but does not stop or remove the chatbot containers. The manual cleanup steps in this procedure are required.

## Procedure

1.  Stop the chatbot services on the host to immediately prevent the assistant from responding to queries:


```
sudo systemctl stop ansible-lightspeed-chatbot.service
sudo systemctl stop ansible-lightspeed.service
```

2.  Disable the chatbot services to prevent them from restarting on reboot:


```
sudo systemctl disable ansible-lightspeed-chatbot.service
sudo systemctl disable ansible-lightspeed.service
```

3.  Open the inventory file that you used to install Ansible Automation Platform.
4.  Remove or comment out all chatbot variables from the inventory file. These are the variables that begin with `lightspeed_chatbot_`:

- `lightspeed_chatbot_model_url`
- `lightspeed_chatbot_model_api_key`
- `lightspeed_chatbot_model_id`
- `lightspeed_chatbot_default_provider`
- `lightspeed_chatbot_model_extra_settings`
- `lightspeed_chatbot_agent_extra_settings`

5.  Remove or comment out the Ansible Lightspeed host entry from the `[ansiblelightspeed] `group, if no other Lightspeed components are in use. Leave the group header in the inventory file.
6.  Save the inventory file.
7.  Re-run the Ansible Automation Platform installer with the updated inventory file:


```
ansible-playbook -i inventory
ansible.containerized_installer.install
```

The installer reconfigures the platform gateway to remove the chatbot proxy routes. The chatbot API endpoints return a 503 error and the chat interface is no longer accessible to users.

8.  Remove the stopped chatbot containers from the host:


```
podman rm ansible-lightspeed-chatbot
podman rm ansible-lightspeed
```

