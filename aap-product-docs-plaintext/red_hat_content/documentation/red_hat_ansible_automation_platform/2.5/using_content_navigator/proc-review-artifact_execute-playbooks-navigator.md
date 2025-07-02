# 6. Running Ansible playbooks with automation content navigator
## 6.2. Reviewing playbook results with an automation content navigator artifact file




Automation content navigator saves the results of the playbook run in a JSON artifact file. You can use this file to share the playbook results with someone else, save it for security or compliance reasons, or review and troubleshoot later. You only need the artifact file to review the playbook run. You do not need access to the playbook itself or inventory access.

**Prerequisites**

- A automation content navigator artifact JSON file from a playbook run.


**Procedure**

- Start automation content navigator with the artifact file.


```
$ ansible-navigator replay simple_playbook_artifact.json
```


1. Review the playbook results that match when the playbook ran.

![Playbook results](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_content_navigator-en-US/images/4f50de6511503aed4d7729dafafad134/navigator-artifact-replay.png)






You can now type the number next to the plays and tasks to step into each to review the results, as you would after executing the playbook.

**Additional resources**

-  [ansible-playbook](https://docs.ansible.com/ansible/latest/cli/ansible-playbook.html)
-  [Ansible playbooks](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_intro.html)


