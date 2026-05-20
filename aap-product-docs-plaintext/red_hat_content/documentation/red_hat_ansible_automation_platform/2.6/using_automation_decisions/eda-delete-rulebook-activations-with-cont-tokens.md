# 6. Red Hat Ansible Automation Platform credential
## 6.1. Replacing controller tokens in Red Hat Ansible Automation Platform 2.6
### 6.1.1. Deleting rulebook activations with controller tokens

Delete rulebook activations that rely on deprecated controller tokens. This mandatory step prevents conflicts before migrating to the new, required Red Hat Ansible Automation Platform credentials.

**Procedure**

1. Log in to the Ansible Automation Platform Dashboard.
2. From the top navigation panel, select Automation Decisions → Rulebook Activations.
3. Select the rulebook activations that have controller tokens.
4. Select the More Actions icon **⋮** next to the **Rulebook Activation enabled/disabled** toggle.
5. Select Delete rulebook activation.
6. In the window, select Yes, I confirm that I want to delete these X rulebook activations.
7. Select Delete rulebook activations.

