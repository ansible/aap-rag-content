# Disable or remove the automation intelligent assistant

If the automation intelligent assistant produces responses that are harmful, inaccurate, or unacceptable for your environment, you can disable or remove it from your Ansible Automation Platform deployment.

As a platform administrator, you can disable the automation intelligent assistant to immediately stop it from responding to user queries. This procedure serves as the incident response mechanism for a malfunctioning AI assistant.

Choose the procedure that matches your deployment type:

- Operator-based deployments on OpenShift Container Platform: Disable the Lightspeed component in the operator custom resource.
- Containerized installations: Stop the chatbot services, remove the Lightspeed variables from the inventory file, and re-run the installer.
