# Troubleshoot failed event-driven automation triggers
## Fix rulebook activations stuck in a restart loop

Troubleshoot rulebook activations that restart repeatedly (indicating persistent errors) to diagnose and fix core issues preventing stable, continuous automation execution.

### Procedure

1.  Log in to Ansible Automation Platform.
2.  From the navigation panel, select Automation Decisions> (and then)Rulebook Activations.
3.  From the **Rulebook Activations** page, select the activation in your list that keeps restarting. The Details page is displayed.
4.  Click the **History** tab for more information and select the rulebook activation that keeps restarting. The Details tab is displayed and shows the output information.
5.  Check the **Restart policy** field for your activation. There are three selections available: **On failure** (restarts a rulebook activation when the container process fails), **Always** (always restarts regardless of success or failure with no more than 5 restarts), or **Never** (never restarts when the container process ends).

1.  Confirm that your rulebook activation Restart policy is set to **On failure**. This is an indication that an issue is causing it to fail.
2.  To possibly diagnose the problem, check the YAML code and the instance logs of the rulebook activation for errors.
3.  If you cannot find a solution with the restart policy values, proceed to the next steps related to the **Log level**.

6.  Check your log level for your activation.   1.  If your default log level is **Error**, go back to the **Rulebook Activation** page and recreate your activation following procedures in [Setting up rulebook a activation](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-assembly_eda_rulebook_activations#eda-set-up-rulebook-activation "Create a rulebook activation to link a rulebook to a decision environment and event sources, initiating the event-driven automation process.").
2.  Change the **Log level** to **Debug**.
3.  Run the activation again and navigate to the **History** tab from the activation details page.
4.  On the **History** page, click one of your recent activations and view the **Output**.

