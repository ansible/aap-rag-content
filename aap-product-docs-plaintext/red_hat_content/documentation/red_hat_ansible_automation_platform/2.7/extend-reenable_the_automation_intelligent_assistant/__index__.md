# Re-enable the automation intelligent assistant

After you resolve the issue that caused you to disable the automation intelligent assistant, you can re-enable it.

For an operator-based deployment:

- Set `disabled` to `false` in the Ansible Automation Platform custom resource YAML, and click **Save**. The operator recreates the AnsibleLightspeed custom resource and the Lightspeed pods restart automatically.

For containerized installations:

- Restore the Lightspeed chatbot variables in the inventory file, re-enable and start the systemd services, and re-run the installer:

```
sudo systemctl enable ansible-lightspeed.service
ansible-lightspeed-chatbot.service
sudo systemctl start ansible-lightspeed.service
ansible-lightspeed-chatbot.service ansible-playbook -i inventory ansible.containerized_installer.install
```
