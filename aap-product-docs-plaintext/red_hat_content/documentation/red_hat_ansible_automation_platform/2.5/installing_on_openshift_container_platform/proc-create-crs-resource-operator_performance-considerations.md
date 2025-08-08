# 10. Ansible Automation Platform Resource Operator
## 10.3. Connecting Resource Operator to platform gateway
### 10.3.1. Creating custom resources for Resource Operator




#### 10.3.1.1. Creating an AnsibleJob custom resource




An AnsibleJob custom resource launches a job in the automation controller instance specified in the Kubernetes secret (automation controller host URL, token). You can launch an automation job on automation controller by creating an AnsibleJob resource.

**Procedure**

1. Specify the connection secret and job template you want to launch.


```
apiVersion: tower.ansible.com/v1alpha1    kind: AnsibleJob    metadata:      generateName: demo-job-1 # generate a unique suffix per 'kubectl create'    spec:      connection_secret: controller-access      job_template_name: Demo Job Template
```


1. Configure features such as, inventory, extra variables, and time to live for the job.


```
spec:      connection_secret: controller-access      job_template_name: Demo Job Template      inventory: Demo Inventory                    # Inventory prompt on launch needs to be enabled      runner_image: quay.io/ansible/controller-resource-runner      runner_version: latest      job_ttl: 100      extra_vars:                                  # Extra variables prompt on launch needs to be enabled         test_var: test      job_tags: "provision,install,configuration"  # Specify tags to run      skip_tags: "configuration,restart"           # Skip tasks with a given tag
```

Note
You must enable prompt on launch for inventories and extra variables if you are configuring those. To enable **Prompt on launch** , within the automation controller UI: From theResources→Templatespage, select your template and select the **Prompt on launch** checkbox next to **Inventory** and **Variables** sections.




1. Launch a workflow job template with an AnsibleJob object by specifying the `    workflow_template_name` instead of `    job_template_name` :


```
apiVersion: tower.ansible.com/v1alpha1    kind: AnsibleJob    metadata:      generateName: demo-job-1 # generate a unique suffix per 'kubectl create'    spec:      connection_secret: controller-access      workflow_template_name: Demo Workflow Template
```




#### 10.3.1.2. Creating a JobTemplate custom resource




A job template is a definition and set of parameters for running an Ansible job. For more information see the [Job Templates](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#controller-job-templates) section of the _Using automation execution_ guide.

**Procedure**

- Create a job template on automation controller by creating a JobTemplate custom resource:


```
apiVersion: tower.ansible.com/v1alpha1    kind: JobTemplate    metadata:      name: jobtemplate-4    spec:      connection_secret: controller-access      job_template_name: ExampleJobTemplate4      job_template_project: Demo Project      job_template_playbook: hello_world.yml      job_template_inventory: Demo Inventory
```




#### 10.3.1.3. Creating an automation controller project custom resource




A Project is a logical collection of Ansible playbooks, represented in automation controller. For more information see the [Projects](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#controller-projects) section of the _Using automation execution_ guide.

**Procedure**

- Create a project on automation controller by creating an automation controller project custom resource:


```
apiVersion: tower.ansible.com/v1alpha1    kind: AnsibleProject    metadata:      name: git    spec:      repo: https://github.com/ansible/ansible-tower-samples      branch: main      name: ProjectDemo-git      scm_type: git      organization: Default      description: demoProject      connection_secret: controller-access      runner_pull_policy: IfNotPresent
```


<span id="proc-operator-create-controller-schedule_performance-considerations"></span>
= Creating an automation controller schedule custom resource





**Procedure**

- Create a schedule on automation controller by creating an automation controller schedule custom resource:


```
apiVersion: tower.ansible.com/v1alpha1    kind: AnsibleSchedule    metadata:      name: schedule    spec:      connection_secret: controller-access      runner_pull_policy: IfNotPresent      name: "Demo Schedule"      rrule: "DTSTART:20210101T000000Z RRULE:FREQ=DAILY;INTERVAL=1;COUNT=1"      unified_job_template: "Demo Job Template"
```


<span id="proc-operator-create-controller-workflow_performance-considerations"></span>
= Creating an automation controller workflow custom resource





Workflows enable you to configure a sequence of disparate job templates (or workflow templates) that may or may not share inventory, playbooks, or permissions. For more information see the [Workflows in automation controller](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#controller-workflows) section of the _Using automation execution_ guide.

**Procedure**

- Create a workflow on automation controller by creating a workflow custom resource:


```
apiVersion: tower.ansible.com/v1alpha1    kind: AnsibleWorkflow    metadata:      name: workflow    spec:      inventory: Demo Inventory      workflow_template_name: Demo Job Template      connection_secret: controller-access      runner_pull_policy: IfNotPresent
```


<span id="proc-operator-create-controller-workflow-template_performance-considerations"></span>
= Creating an automation controller workflow template custom resource





A workflow job template links together a sequence of disparate resources to track the full set of jobs that were part of the release process as a single unit. For more information see the [Workflow job templates](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#controller-workflow-job-templates) section of the _Using automation execution_ guide.

**Procedure**

- Create a workflow template on automation controller by creating a workflow template custom resource:


```
apiVersion: tower.ansible.com/v1alpha1    kind: WorkflowTemplate    metadata:      name: workflowtemplate-sample    spec:      connection_secret: controller-access      name: ExampleTowerWorkflow      description: Example Workflow Template      organization: Default      inventory: Demo Inventory      workflow_nodes:      - identifier: node101        unified_job_template:          name: Demo Job Template          inventory:            organization:              name: Default          type: job_template      - identifier: node102        unified_job_template:          name: Demo Job Template          inventory:            organization:              name: Default          type: job_template
```


<span id="proc-operator-create-controller-inventory_performance-considerations"></span>
= Creating an automation controller inventory custom resource





By using an inventory file, Ansible Automation Platform can manage a large number of hosts with a single command. Inventories also help you use Ansible Automation Platform more efficiently by reducing the number of command line options you have to specify. For more information see the [Inventories](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html-single/using_automation_execution/index#controller-inventories) section of the _Using automation execution_ guide.

**Procedure**

- Create an inventory on automation controller by creating an inventory custom resource:


```
metadata:      name: inventory-new    spec:      connection_secret: controller-access      description: my new inventory      name: newinventory      organization: Default      state: present      instance_groups:        - default      variables:        string: "string_value"        bool: true        number: 1        list:          - item1: true          - item2: "1"        object:          string: "string_value"          number: 2
```


<span id="proc-operator-create-controller-credential_performance-considerations"></span>
= Creating an automation controller credential custom resource





Credentials authenticate the automation controller user when launching jobs against machines, synchronizing with inventory sources, and importing project content from a version control system.

SSH and AWS are the most commonly used credentials. For a full list of supported credentials see the [Credential types](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/controller-credentials#ref-controller-credential-types) section of the _Using automation execution_ guide.

For help with defining values you can refer to the [OpenAPI (Swagger) file for Red Hat Ansible Automation Platform API](https://access.redhat.com/login?redirectTo=https%3A%2F%2Faccess.redhat.com%2Fsolutions%2F7050627) KCS article.

Tip
You can use `https://&lt;aap-instance&gt;/api/controller/v2/credential_types/` to view the list of credential types on your instance. To get the full list use the following `curl` command:

```
export AAP_TOKEN="your-oauth2-token"
export AAP_URL="https://your-aap-controller.example.com"

curl -s -H "Authorization: Bearer $AAP_TOKEN" "$AAP_URL/api/controller/v2/credential_types/" | jq -r '.results[].name'
```



**Procedure**

- Create an AWS or SSH credential on automation controller by creating a credential custom resource:


- SSH credential:


```
apiVersion: tower.ansible.com/v1alpha1        kind: AnsibleCredential        metadata:          name: ssh-cred        spec:          name: ssh-cred          organization: Default          connection_secret: controller-access          description: "SSH credential"          type: "Machine"          ssh_username: "cat"          ssh_secret: my-ssh-secret          runner_pull_policy: IfNotPresent
```


- AWS credential:


```
apiVersion: tower.ansible.com/v1alpha1        kind: AnsibleCredential        metadata:          name: aws-cred        spec:          name: aws-access          organization: Default          connection_secret: controller-access          description: "This is a test credential"          type: "Amazon Web Services"          username_secret: aws-secret          password_secret: aws-secret          runner_pull_policy: IfNotPresent
```





