# 3. Getting started as an automation developer
## 3.2. Create automation content with playbooks
### 3.2.1. Create a playbook




A playbook contains one or more plays. A basic play contains the following parameters:

-  **Name** : a brief description of the overall function of the playbook, which assists in keeping it readable and organized for all users.
-  **Hosts** : identifies the target or targets for Ansible to run against.
-  **Become statements** : this optional statement can be set to `    true` or `    yes` to enable privilege escalation using a become plugin (such as `    sudo` , `    su` , `    pfexec` , `    doas` , `    pbrun` , `    dzdo` , `    ksu` ).
-  **Tasks** : this is the list of actions that get executed against each host in the play.


Here is an example of a play in a playbook. You can see the name of the play, the host, and the list of tasks included in the play.

```
- name: Set Up a Project and Job Template
hosts: host.name.ip
become: true

tasks:
- name: Create a Project
ansible.controller.project:
name: Job Template Test Project
state: present
scm_type: git
scm_url: https://github.com/ansible/ansible-tower-samples.git

- name: Create a Job Template
ansible.controller.job_template:
name: my-job-1
project: Job Template Test Project
inventory: Demo Inventory
playbook: hello_world.yml
job_type: run
state: present
```

For more detailed instructions on authoring playbooks, see [Developing automation content](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/developing_automation_content) , or consult our documentation on [Red Hat Ansible Lightspeed with IBM watsonx Code Assistant User Guide](https://docs.redhat.com/en/documentation/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant/2.x_latest/html/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant_user_guide) to learn how to generate a playbook with AI assistance.

