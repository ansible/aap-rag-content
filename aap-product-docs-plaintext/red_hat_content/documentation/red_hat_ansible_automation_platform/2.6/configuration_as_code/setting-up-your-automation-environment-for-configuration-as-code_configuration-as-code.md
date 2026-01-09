# Chapter 1. Setting up your automation environment for Configuration as Code




Configuration as Code is a way of working where you define and manage the configuration of the Ansible Automation Platform itself using the version-controlled configuration files (such as YAML, or JSON), instead of clicking through the web UI.

As an Ansible content developer, you can use the Configuration as Code approach to apply settings on your automation controller to get the following benefits:

- Predictable job behavior
- Easier and faster scaling to new clusters
- Change history with diffs and rollback capability thanks to version control support
- Faster recovery after outages or migrations
- Reduced risk of errors because changes flow through CI/CD pipelines and pull requests, where peer reviews and automated testing are applied


**Prerequisites**

- You have a Git account.
- Your platform gateway instance is accessible.
- You built and registered your own execution environment. Alternatively, you have available the supported execution environment to run playbooks that use the `    ansible.platform` collection. For more information, see [Creating and using execution environments](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/creating_and_using_execution_environments/index) .


**Procedure**

1. Create a new Git repository.
1. On your local machine, encrypt your password for platform gateway:


```
$ ansible-vault encrypt_string '<span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">&lt;gateway_password&gt;</span></em></span>' --name 'aap_password'    New Vault password:<span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">&lt;vault_password&gt;</span></em></span>Confirm New Vault password:<span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">&lt;vault_password&gt;</span></em></span>Encryption successful    aap_password: !vault |              $ANSIBLE_VAULT;1.1;AES256              63633763653530343566363864333130656433613634333465363733326261336465333362623635              3061333439626238616332313663633431663962353735320a633732346232396165373931653039              64326462306162396366373565316631343033656230363038623237313036613166313331623533              3363636462646534330a616437646665393738386235306361653333313338656563346633396434              35346164656437326231326433323934643133353436323562373762616531326463
```

You encrypted the value of the `    aap_password` variable, which you will use in the next step.


1. Create the `    /my_ansible_project/vars/all.yml` file with variables for connecting to your Ansible Automation Platform and variables for creating Role-Based Access Control (RBAC) objects:


```
---    # Ansible Automation Platform related variables    aap_hostname: "&lt;GATEWAY&gt;"    aap_username: "&lt;GATEWAY_USER&gt;"    aap_password: !vault |              $ANSIBLE_VAULT;1.1;AES256              63633763653530343566363864333130656433613634333465363733326261336465333362623635              3061333439626238616332313663633431663962353735320a633732346232396165373931653039              64326462306162396366373565316631343033656230363038623237313036613166313331623533              3363636462646534330a616437646665393738386235306361653333313338656563346633396434              35346164656437326231326433323934643133353436323562373762616531326463    aap_validate_certs: false        # Details for creating organization, team, and user    org_name: "Demo-Organization"    team_name: "Demo-Team"    user_username: "Demo-User"    user_email: "demo.user@example.com"    user_password: "3ncrypt3d_P@$$word"        # Role names as they exist in your Ansible Automation Platform    role_for_team_in_org: "Organization Inventory Admin" # "Executor"    role_for_user_in_org: "Organization Auditor"    role_for_user_in_team: "Auditor" # if your platform supports team-scoped roles        # Custom role definition details    custom_role_name: "NetOps ReadOnly"    custom_role_description: "Read-only access to network objects"
```


1. Compose the `    /my_ansible_project/RBAC_settings.yml` playbook, which creates RBAC objects and assigns roles to those objects:


```
---    - name: Create RBAC objects and assign roles to them      hosts: localhost      gather_facts: false      vars_files:        - ./vars/all.yml      tasks:        - name: Ensure new organization exists          ansible.platform.organization:            name: "{{ org_name }}"            state: present            aap_hostname: "{{ aap_hostname }}"            aap_username: "{{ aap_username }}"            aap_password: "{{ aap_password }}"            aap_validate_certs: "{{ aap_validate_certs }}"            - name: Ensure new team exists in organization          ansible.platform.team:            name: "{{ team_name }}"            organization: "{{ org_name }}"            state: present            aap_hostname: "{{ aap_hostname }}"            aap_username: "{{ aap_username }}"            aap_password: "{{ aap_password }}"            aap_validate_certs: "{{ aap_validate_certs }}"            - name: Ensure new user exists          ansible.platform.user:            username: "{{ user_username }}"            email: "{{ user_email }}"            password: "{{ user_password }}"            state: present            aap_hostname: "{{ aap_hostname }}"            aap_username: "{{ aap_username }}"            aap_password: "{{ aap_password }}"            aap_validate_certs: "{{ aap_validate_certs }}"            - name: Ensure new custom role exists          ansible.platform.role_definition:            name: "{{ custom_role_name }}"            description: "{{ custom_role_description }}"            content_type: awx.inventory            permissions:              - awx.view_inventory              - awx.change_inventory            state: present            aap_hostname: "{{ aap_hostname }}"            aap_username: "{{ aap_username }}"            aap_password: "{{ aap_password }}"            aap_validate_certs: "{{ aap_validate_certs }}"            - name: Assign already existing role to team in organization          ansible.platform.role_team_assignment:            team: "{{ team_name }}"            assignment_objects:              - name: "{{ org_name }}"                type: "organizations"            role_definition: "{{ role_for_team_in_org }}"            state: present            aap_hostname: "{{ aap_hostname }}"            aap_username: "{{ aap_username }}"            aap_password: "{{ aap_password }}"            aap_validate_certs: "{{ aap_validate_certs }}"            - name: Assign already existing role to user in organization          ansible.platform.role_user_assignment:            user: "{{ user_username }}"            object_ids:              - "{{ org_name }}"            role_definition: "{{ role_for_user_in_org }}"            state: present            aap_hostname: "{{ aap_hostname }}"            aap_username: "{{ aap_username }}"            aap_password: "{{ aap_password }}"            aap_validate_certs: "{{ aap_validate_certs }}"
```

Many values in this playbook are provided in the form of variables, such as object names, their details, Ansible Automation Platform credentials. You can easily reuse the variables throughout files in your Ansible project, which will also simplify the creation and maintenance of the project and reduce the number of errors.

Refer to the `    all.yml` file to see the expanded values of those variables. For details about the module parameters, default values, and further examples how to use the modules, see the resources on Automation hub for the [ansible.platform](https://console.redhat.com/ansible/automation-hub/repo/published/ansible/platform/content/?showing=module) collection.


1. Push the variables and the playbook to your Git repository so that the automation controller can later read in the correct data.


```
git add .    git commit -m "Provide variables and RBAC_settings.yml playbook resources for Ansible Automation Platform project"    git push origin _&lt;relevant_branch_name&gt;_
```


1. Using the platform gateway UI, create a new project with the following values:


- Name: Platform collection testing
- Description: Automation resources to test the CaC capability of RBAC modules from the `        ansible.platform` collection
- Execution Environment: `        ee-supported`
- Organization: Default
- Source Control Type: Git
- Source Control URL: https://my_git_url/my_git_repository/my_ansible_project

![Create project](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Configuration_as_Code-en-US/images/5748f7c24f85d7f55807e6b9c4debd50/cac-create-project.png)




1. Create a credential for your Ansible Vault password of your encrypted `    aap_password` variable:


- Name: aap_password_vault
- Description: Holds vault password for decrypting the value of the `        aap_password` variable
- Credential type: Vault
- Vault Password: _<vault_password>_

![Create Credential](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Configuration_as_Code-en-US/images/087082ec7aadccb2a4713003d6412c9f/cac-create-vault-credential.png)




1. Create a job template with the following values:


- Name: RBAC_settings
- Description: Create organization, team, user, and custom role RBAC objects. Assign a pre-existing role to the created team and assign a pre-existing role to the created user.
- Job type: Run
- Inventory: Demo Inventory
- Project: Platform collection testing
- Playbook: `        RBAC_settings.yml`
- Execution Environment: `        ee-supported`
- Credentials: aap_password_vault | Vault

![Create job template](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Configuration_as_Code-en-US/images/0ce76cb6c2e2157ff520a177c217e8f7/cac-create-job-template.png)




1. Launch the `    RBAC_settings` job template. After the template job successfully finishes, the output should be similar to the following:


```
Vault password:    [WARNING]: Collection ansible.platform does not support Ansible version 2.15.13        PLAY [Create organization] *****************************************************        TASK [Ensure new organization exists] ******************************************    changed: [localhost]        PLAY [Create team] *************************************************************        TASK [Ensure new team exists in organization] **********************************    changed: [localhost]        PLAY [Create user] *************************************************************        TASK [Ensure new user exists] **************************************************    changed: [localhost]        PLAY [Create custom role] ******************************************************        TASK [Ensure new custom role exists] *******************************************    changed: [localhost]        PLAY [Team gets role] **********************************************************        TASK [Assign already existing role to team in organization] ********************    changed: [localhost]        PLAY [User gets role] **********************************************************        TASK [Assign already existing role to user in organization] ********************    changed: [localhost]        PLAY RECAP *********************************************************************    localhost: ok=6 changed=6 unreachable=0 failed=0 skipped=0 rescued=0 ignored=0
```

The output message shows that you ran the job template against 1 target (your localhost). At the same time, you created:


- An organization.
- A team that exists within the created organization. The team was assigned some pre-existing role.
- A user that exists within the created organization. The user was assigned some pre-existing role.
- A custom role.



**Verification**

- In the navigation panel, check that you see your created organization:

![Organization exists](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Configuration_as_Code-en-US/images/8d0f1f6e3c7376a01d4e5b74368a632c/cac-organization-exists.png)



- Check that you see your created team, which belongs to the organization and is assigned the correct pre-existing role:

![Team with assigned role exists](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Configuration_as_Code-en-US/images/c151fa4bafb1a71a8319b31a62eabbab/cac-team-exists.png)



- Check that you see your created user, which belongs to the organization and is assigned the correct pre-existing role:

![User with assigned role exists](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Configuration_as_Code-en-US/images/455f76ff2d59aa6aa2897d0494697bf8/cac-user-exists.png)



- Check that you see your created custom role, which was assigned the permissions as specified in your `    RBAC_settings.yml` playbook:

![Custom role with assigned permissions exists](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Configuration_as_Code-en-US/images/eefc394ea9113533fda20b7c42ca81bb/cac-custom-role-exists.png)






<span id="idm140439814095696"></span>
