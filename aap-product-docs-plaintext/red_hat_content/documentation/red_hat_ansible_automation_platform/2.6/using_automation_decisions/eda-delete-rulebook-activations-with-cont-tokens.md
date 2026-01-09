# 6. Red Hat Ansible Automation Platform credential
## 6.1. Replacing controller tokens in Red Hat Ansible Automation Platform 2.6
### 6.1.1. Deleting rulebook activations with controller tokens




Delete rulebook activations that rely on deprecated controller tokens. This mandatory step prevents conflicts before migrating to the new, required Red Hat Ansible Automation Platform credentials.

**Procedure**

1. Log in to the Ansible Automation Platform Dashboard.
1. From the top navigation panel, selectAutomation Decisions→Rulebook Activations.
1. Select the rulebook activations that have controller tokens.
1. Select theMore Actionsicon **⋮** next to the **Rulebook Activation enabled/disabled** toggle.
1. SelectDelete rulebook activation.
1. In the window, selectYes, I confirm that I want to delete these X rulebook activations.
1. SelectDelete rulebook activations.


