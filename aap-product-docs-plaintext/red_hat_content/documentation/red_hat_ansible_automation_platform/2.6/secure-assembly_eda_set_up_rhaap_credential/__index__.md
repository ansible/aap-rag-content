# Replace legacy automation controller tokens

When Event-Driven Ansible controller is deployed on Ansible Automation Platform, you can create a Red Hat Ansible Automation Platform credential to connect to automation controller through the use of an automation controller URL and a username and password.

After it has been created, you can attach the Red Hat Ansible Automation Platform credential to a rulebook and use it to run rulebook activations. These credentials provide a simple way to configure communication between automation controller and Event-Driven Ansible controller, enabling your rulebook activations to launch job templates.

Note:

If you previously used controller tokens to connect automation controller and Event-Driven Ansible controller, these tokens are now deprecated. To delete deprecated controller tokens and the rulebook activations associated with them, complete the following procedures starting with replacing controller tokens before proceeding with setting up a Red Hat Ansible Automation Platform credential.

## Replace deprecated controller tokens

To use Event-Driven Ansible controller, you must replace legacy controller tokens configured in your environment with Red Hat Ansible Automation Platform credentials because controller tokens have been deprecated.

## Delete rulebook activations with controller tokens

Delete rulebook activations that rely on deprecated controller tokens. This mandatory step prevents conflicts before migrating to the new, required Red Hat Ansible Automation Platform credentials.

### Procedure

1.  Log in to the Ansible Automation Platform Dashboard.
2.  From the top navigation panel, select Automation Decisions> (and then)Rulebook Activations.
3.  Select the rulebook activations that have controller tokens.
4.  Select the More Actions icon **⋮** next to the **Rulebook Activation enabled/disabled** toggle.
5.  Select Delete rulebook activation.
6.  In the window, select Yes, I confirm that I want to delete these X rulebook activations.
7.  Select Delete rulebook activations.

## Delete controller tokens

Before configuring the new Red Hat Ansible Automation Platform credentials, delete all existing controller tokens, which are now deprecated and will conflict with the new Red Hat Ansible Automation Platform credentials.

### Before you begin

- You have deleted all rulebook activations that use controller tokens.

### Procedure

1.  Log in to the Ansible Automation Platform Dashboard.
2.  From the top navigation panel, select your profile.
3.  Click **User details**.
4.  Select the **Tokens** tab.
5.  Delete all of your previous controller tokens.

### What to do next

After deleting the controller tokens and rulebook activations, proceed with[Replace legacy automation controller tokens](/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-assembly_eda_set_up_rhaap_credential#eda-set-up-rhaap-credential-type "When Event-Driven Ansible controller is deployed on Ansible Automation Platform, you can create a Red Hat Ansible Automation Platform credential to connect to automation controller through the use of an automation controller URL and a username and password.").
