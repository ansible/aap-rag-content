# 14. Troubleshooting the Red Hat Ansible Automation Platform Operator on OpenShift Container Platform
## 14.2. Viewing events in the OpenShift Container Platform

You can view events in the OpenShift Container Platform web console to monitor for errors and troubleshoot issues. This helps you quickly diagnose problems by examining the status of custom resources and their related events.

You can debug by first reviewing the status conditions of the Ansible Automation Platform custom resource (CR) and then checking any nested CRs for errors.

**Procedure**

1. Log in to the OpenShift Container Platform web console.
2. In the navigation menu, select Home → Events.
3. Select your project from the project list.
4. To view events for a specific resource, navigate to that resource’s page. Many resource pages, such as pods and deployments, have their own **Events** tab.
5. Select a resource to bring you to the **Pod Details** page.

**Verification**

Check the **Conditions** section on the **Pod details** page to confirm no errors are listed in the **Message** column.

