# 3. Getting started as an automation developer
## 3.8. Build and use an execution environment
### 3.8.1. Using the base automation execution environment




Ansible Automation Platform provides access to some base automation execution environments. You can use a base execution environment as a starting point for creating a customized execution environment.

Ansible Automation Platform includes the following execution environments:

-  `    Minimal` - Includes the latest Ansible-core 2.15 release along with Ansible Runner, but does not include collections or other content
-  `    EE Supported` - Minimal, plus all Red Hat-supported collections and dependencies


Base images included with Ansible Automation Platform are hosted on the Red Hat Ecosystem Catalog ( `registry.redhat.io` ).

**Prerequisites**

- You have a valid Red Hat Ansible Automation Platform subscription.


**Procedure**

1. Log in to `    registry.redhat.io` .


```
$ podman login registry.redhat.io
```


1. Pull the base images from the registry:


```
$ podman pull registry.redhat.io/aap/&lt;image name&gt;
```

**Additional resources**

-  [Customizing an existing automation execution environment image](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/creating_and_using_execution_environments/assembly-publishing-exec-env#proc-customize-ee-image)


#### 3.8.1.1. About Ansible Builder




You also have the option of creating an entirely new execution environment with Ansible Builder, also referred to as execution environment builder. Ansible Builder is a command line tool you can use to create an execution environment for Ansible.

To build your own execution environment, you must:

- Download Ansible Builder
- Create a definition file that defines your execution environment
- Create an execution environment image based on the definition file


For more information about building an execution environment, see [Creating and using execution environments](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/creating_and_using_execution_environments) .

