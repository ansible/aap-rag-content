# 8. Rulebook activations troubleshooting
## 8.3. Activation keeps restarting




Perform the following steps if your rulebook activation keeps restarting.

**Procedure**

1. Log in to Ansible Automation Platform.
1. From the navigation panel, selectAutomation Decisions→Rulebook Activations.
1. From the **Rulebook Activations** page, select the activation in your list that keeps restarting. The Details page is displayed.
1. Click the **History** tab for more information and select the rulebook activation that keeps restarting. The Details tab is displayed and shows the output information.
1. Check the **Restart policy** field for your activation.

There are three selections available: **On failure** (restarts a rulebook activation when the container process fails), **Always** (always restarts regardless of success or failure with no more than 5 restarts), or **Never** (never restarts when the container process ends).


1. Confirm that your rulebook activation Restart policy is set to **On failure** . This is an indication that an issue is causing it to fail.
1. To possibly diagnose the problem, check the YAML code and the instance logs of the rulebook activation for errors.
1. If you cannot find a solution with the restart policy values, proceed to the next steps related to the **Log level** .

1. Check your log level for your activation.


1. If your default log level is **Error** , go back to the **Rulebook Activation** page and recreate your activation following procedures in [Setting up rulebook a activation](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_decisions/eda-rulebook-activations#eda-set-up-rulebook-activation) .
1. Change the **Log level** to **Debug** .
1. Run the activation again and navigate to the **History** tab from the activation details page.
1. On the **History** page, click one of your recent activations and view the **Output** .



