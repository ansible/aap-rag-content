# 3. Using Ansible Builder
## 3.6. Building the automation execution environment image




When you have created a definition file, you can proceed to build an automation execution environment image.

Note
When building an execution environment image, it must support the architecture that Ansible Automation Platform is deployed with.



**Prerequisites**

- You have created a definition file.


**Procedure**

1. To build an automation execution environment image, run the following from the command line:


```
$ ansible-builder build
```

By default, Ansible Builder looks for a definition file named `    execution-environment.yml` but a different file path can be specified as an argument with the `    -f` flag:

For example:


```
$ ansible-builder build -f<span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">definition-file-name</span></em></span>.yml
```

where _definition-file-name_ specifies the name of your definition file.




