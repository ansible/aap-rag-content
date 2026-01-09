# 10. Patch releases
## 10.1. Ansible Automation Platform patch release December 10, 2025
### 10.1.3. Ansible Automation Platform




#### 10.1.3.1. Bug Fixes




- Fixed an issue where the user could type the name of the playbook when creating a job template, to support playbooks that may exist in a branch of a project with branch override.(AAP-52566)
- Fixes using and condition with multiple attributes. Where previously the authentication map would skip the missing attributes, with this fix the map will be applied only if all attributes are present and the condition(s) are met.(AAP-53523)
- Fixes issue where subscription entitlement window displays again after Ansible Automation Platform had been entitled when running in a load-balanced environment with multiple controller web pods.(AAP-51618)
- Fixed an issue where the job template did not remain editable after the associated project was deleted.(AAP-58474)


