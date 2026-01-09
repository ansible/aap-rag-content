# 3. Getting started as an automation developer
## 3.8. Build and use an execution environment




All automation in Red Hat Ansible Automation Platform runs on container images called automation execution environments.

Automation execution environments are consistent and shareable container images that serve as Ansible control nodes. Automation execution environments reduce the challenge of sharing Ansible content that has external dependencies.

If automation content is similar to a script that a developer has written, an automation execution environment is like a replica of that developer’s environment, thereby enabling you to reproduce and scale that automation content. In this way, execution environments make it easier for you to implement automation in a range of environments.

Automation execution environments contain:

- Ansible Core
- Ansible Runner
- Ansible Collections
- Python libraries
- System dependencies
- Custom user needs


You can either use the default base execution environment included in your Ansible Automation Platform subscription, or you can define and create an automation execution environment using Ansible Builder.

