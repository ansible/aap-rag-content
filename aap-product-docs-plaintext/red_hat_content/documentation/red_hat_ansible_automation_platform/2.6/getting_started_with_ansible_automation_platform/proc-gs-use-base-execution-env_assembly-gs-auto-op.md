# 4. Getting started as an automation operator
## 4.6. Build and use an execution environment
### 4.6.1. Using the base automation execution environment




Your subscription with Ansible Automation Platform gives you access to some base automation execution environments. You can use a base execution environment as a starting point for creating a customized execution environment.

Ansible Automation Platform includes the following default execution environments:

-  `    Minimal` - Includes the latest Ansible-core 2.15 release along with Ansible Runner, but does not include collections or other content
-  `    EE Supported` - Minimal, plus all Red Hat-supported collections and dependencies


Base images included with Ansible Automation Platform are hosted on the Red Hat Ecosystem Catalog (registry.redhat.io).

**Prerequisites**

- You have a valid Red Hat Ansible Automation Platform subscription.


**Procedure**

1. Log in to registry.redhat.io.


```
$ podman login registry.redhat.io
```


1. Pull the base images from the registry:


```
$podman pull registry.redhat.io/aap/&lt;image name&gt;
```

**Additional resources**

While these environments cover many automation use cases, you can also customize these containers for your specific needs. For more information about customizing your execution environment, see [Customizing an existing automation execution environment image](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/creating_and_using_execution_environments/assembly-publishing-exec-env#proc-customize-ee-image) in the Creating and using execution environments guide.


