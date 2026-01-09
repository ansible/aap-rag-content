# 13. Ansible Automation Platform Resource Operator
## 13.5. Create custom resources for Resource Operator
### 13.5.1. Creating an AnsibleJob custom resource




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




