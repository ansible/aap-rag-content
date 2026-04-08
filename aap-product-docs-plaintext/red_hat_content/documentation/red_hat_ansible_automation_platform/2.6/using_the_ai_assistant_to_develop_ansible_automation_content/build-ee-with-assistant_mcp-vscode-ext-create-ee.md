# 6. Create and validate an execution environment with the AI assistant
## 6.5. Build the execution environment with the AI assistant




After you have created and validated the definition file, prompt the assistant for the specific commands to build the execution environment image.

**Prerequisites**

- A container runtime like Podman is installed.
- The GitHub Copilot chat is active and your execution environment file is open.


**Procedure**

1. Prompt the assistant for build instructions. For example:


-  _How do I build this execution environment? What are the next steps?_

This prompts the AI assistant to generate an `        ansible-builder` command tailored to fit your file and tag.



1. Copy the build command that was generated and run it in your VS Code terminal. An example command might look like this:


```
ansible-builder build --file execution-environment.yml --context ./context --tag webserver-ee:1.0 -vvv.
```




# Chapter 7. Running playbooks with `ansible-navigator` using the AI assistant




Once you have built a suitable execution environment, prompt the AI assistant to generate the correct `ansible-navigator` command to execute your playbook in that particular environment.

## 7.1. Prerequisites




- The GitHub Copilot Extension is installed and active.
- Ansible VS Code extension is installed.
- The Ansible MCP server is enabled.
- Ansible development tools is installed through the AI assistant ( `    adt_check_env` ) or manually.
- An execution environment definition file is prepared and ready to use.


## 7.2. Run a playbook with ansible-navigator




Prompt the AI assistant for help with running playbooks.

**Procedure**

1. Prompt the assistant to generate a command that runs the playbook in your execution environment. For example:


-  _Give me the command to run this playbook in the execution environment <file name>_ .

The assistant then generates an appropriate `        ansible-navigator` command, ensuring the `        --execution-environment-image` flag points to your newly-built tag.

A generated command might look like the following:


```
ansible-navigator run playbook.yml --execution-environment-image webserver-ee:1.0 --mode stdout
```



1. Execute the command in the VS Code terminal to run your automation within the custom environment.



<span id="idm140481310097168"></span>
# Legal Notice

Copyright© Red Hat.
The text of and illustrations in this document are licensed by Red Hat under a Creative Commons Attribution–Share Alike 3.0 Unported license ("CC-BY-SA"). An explanation of CC-BY-SA is available at [http://creativecommons.org/licenses/by-sa/3.0/](http://creativecommons.org/licenses/by-sa/3.0/) . In accordance with CC-BY-SA, if you distribute this document or an adaptation of it, you must provide the URL for the original version.
Red Hat, as the licensor of this document, waives the right to enforce, and agrees not to assert, Section 4d of CC-BY-SA to the fullest extent permitted by applicable law.
Red Hat, Red Hat Enterprise Linux, the Shadowman logo, JBoss, OpenShift, Fedora, the Infinity logo, and RHCE are trademarks of Red Hat, Inc., registered in the United States and other countries.
Linux® is the registered trademark of Linus Torvalds in the United States and other countries.
Java® is a registered trademark of Oracle and/or its affiliates.
XFS® is a trademark of Silicon Graphics International Corp. or its subsidiaries in the United States and/or other countries.
MySQL® is a registered trademark of MySQL AB in the United States, the European Union and other countries.
Node.js® is an official trademark of Joyent. Red Hat Software Collections is not formally related to or endorsed by the official Joyent Node.js open source or commercial project.
TheOpenStack® Word Mark and OpenStack logo are either registered trademarks/service marks or trademarks/service marks of the OpenStack Foundation, in the United States and other countries and are used with the OpenStack Foundation's permission. We are not affiliated with, endorsed or sponsored by the OpenStack Foundation, or the OpenStack community.
All other trademarks are the property of their respective owners.





