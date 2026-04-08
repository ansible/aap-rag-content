# 6. Deploying Red Hat Ansible Lightspeed on containerized Ansible Automation Platform
## 6.3. Changing your LLM model




To change the LLM model for your containerized Ansible Automation Platform deployment of Ansible Lightspeed intelligent assistant, you must edit the inventory file with the specific details of your new LLM provider and then rerun the install playbook.

**Procedure**

1. Edit the inventory file to update the following Ansible Lightspeed intelligent assistant variables with the specific details of your required LLM provider:


-  `        lightspeed_chatbot_model_url`
-  `        lightspeed_chatbot_model_api_key`
-  `        lightspeed_chatbot_model_id`
-  `        lightspeed_chatbot_default_provider`

1. Rerun the `    install` playbook to [install the containerized Ansible Automation Platform](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/containerized_installation/index#installing-containerized-aap) .


**Additional resources**

-  [Appendix: Red Hat Ansible Lightspeed Inventory file variables](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/containerized_installation/index#lightspeed-variables)


