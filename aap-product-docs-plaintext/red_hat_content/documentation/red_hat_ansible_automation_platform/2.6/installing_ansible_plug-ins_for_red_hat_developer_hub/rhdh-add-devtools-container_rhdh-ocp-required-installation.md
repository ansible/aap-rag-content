# 2. Installing the Ansible plug-ins with a Helm chart on OpenShift Container Platform
## 2.4. Required configuration
### 2.4.3. Adding the Ansible Developer Tools container




You must update the Helm chart configuration to add an extra container.

**Procedure**

1. Log in to the OpenShift UI.
1. Navigate toHelm→developer-hub→Actions→upgrade→Yaml viewto open the Helm chart.
1. Update the `    extraContainers` section in the YAML file.

Add the following code:


```
upstream:      backstage:        ...        extraContainers:          - command:              - adt              - server            image: &gt;-              registry.redhat.io/ansible-automation-platform-26/ansible-dev-tools-rhel9:latest            imagePullPolicy: IfNotPresent            name: ansible-devtools-server            ports:              - containerPort: 8000        ...
```

Note
The image pull policy is `    imagePullPolicy: IfNotPresent` . The image is pulled only if it does not already exist on the node. Update it to `    imagePullPolicy: Always` if you always want to use the latest image.




1. ClickUpgrade.


**Verification**

To verify that the container is running, check the container log:


![View container log](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Installing_Ansible_plug-ins_for_Red_Hat_Developer_Hub-en-US/images/6abd3ad41671a23156c96a0710df0fe8/rhdh-check-devtools-container.png)


