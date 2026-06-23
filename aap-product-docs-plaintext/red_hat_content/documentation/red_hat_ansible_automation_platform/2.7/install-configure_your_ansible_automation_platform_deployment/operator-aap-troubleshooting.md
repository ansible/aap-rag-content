# Configure your Ansible Automation Platform deployment
## Review platform gateway FAQs

Manage your Ansible Automation Platform deployment and troubleshoot common issues with these frequently asked questions. Learn about resource management, logging, and error recovery for your components.

If I delete my Ansible Automation Platform deployment will I still have access to automation controller?
No, automation controller, automation hub, and Event-Driven Ansible are nested within the deployment and are also deleted.

How must I manage parameters when adding or removing them in the Ansible Automation Platform custom resource (CR) hierarchy?
When *adding* parameters, you can add it to the Ansible Automation Platform custom resource (CR) only and those parameters will work their way down to the nested CRs.

When *removing* parameters, you have to remove them both from the Ansible Automation Platform CR *and* the nested CR, for example, the **Automation Controller** CR.

Something went wrong with my deployment but I’m not sure what, how can I find out?
You can follow along in the command line while the operator is reconciling, this can be helpful for debugging. Alternatively you can click into the deployment instance to see the status conditions being updated as the deployment goes on.

Is it still possible to view individual component logs?
When troubleshooting you should examine the **Ansible Automation Platform** instance for the main logs and then each individual component (**EDA**, **AutomationHub**, **AutomationController**) for more specific information.

Where can I view the condition of an instance?
To display status conditions click into the instance, and look under the **Details** or **Events** tab. Alternatively, to display the status conditions you can run the get command: `oc get automationcontroller <instance-name> -o jsonpath=Pipe "| jq"`

Can I track my migration in real time?
To help track the status of the migration or to understand why migration might have failed you can look at the migration logs as they are running. Use the logs command: `oc logs fresh-install-controller-migration-4.6.0-jwfm6 -f`

I have configured my SAML but authentication fails with this error: "Unable to complete social auth login" What can I do?
You must update your Ansible Automation Platform instance to include the `REDIRECT_IS_HTTPS` extra setting. See [Enabling single sign-on (SSO) for platform gateway on OpenShift Container Platform](/documentation/en-us/red_hat_ansible_automation_platform/2.7/install-configure_your_ansible_automation_platform_deployment#proc-operator-enable-https-redirect "HTTPS redirect for SAML, allows you to log in once and access all of the platform gateway without needing to reauthenticate.") for help with this.
