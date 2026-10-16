# Integrate with Red Hat Lightspeed for vulnerability management

Automation controller supports integration with Red Hat Lightspeed.

Note:

Red Hat Lightspeed (formerly Red Hat Insights) provides vulnerability scanning and patch management. This is separate from the Ansible Lightspeed coding assistant, which provides AI-powered code suggestions in IDEs. For information about the coding assistant, see Build automation content faster with the Ansible Lightspeed coding assistant in the Develop section.

When a host is registered with Red Hat Lightspeed, it is scanned continually for vulnerabilities and known configuration conflicts. Each problem identified can have an associated fix in the form of an Ansible Playbook.

Red Hat Lightspeed users create a maintenance plan to group the fixes and can create a playbook to mitigate the problems. Automation controller tracks the maintenance plan playbooks through a Red Hat Lightspeed project.

Authentication to Red Hat Lightspeed through Basic Authorization is backed by a special credential, which must first be established in automation controller.

To run a Red Hat Lightspeed maintenance plan, you need a Red Hat Lightspeed project and inventory.

