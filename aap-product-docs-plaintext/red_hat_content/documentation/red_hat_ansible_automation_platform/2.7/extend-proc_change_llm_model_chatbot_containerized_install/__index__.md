# Change your LLM model

To change the LLM model for your containerized Ansible Automation Platform deployment of Ansible Lightspeed intelligent assistant, you must edit the inventory file with the specific details of your new LLM provider and then rerun the install playbook.

## Procedure

1.  Edit the inventory file to update the following Ansible Lightspeed intelligent assistant variables with the specific details of your required LLM provider:

-  `lightspeed_chatbot_model_url`
-  `lightspeed_chatbot_model_api_key`
-  `lightspeed_chatbot_model_id`
-  `lightspeed_chatbot_default_provider`

2.  Rerun the `install` playbook to [install the containerized Ansible Automation Platform](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-proc_installing_containerized_aap#installing-containerized-aap "Run the install playbook to install containerized Ansible Automation Platform after preparing the Red Hat Enterprise Linux host, downloading the installation program, and configuring the inventory file.").
