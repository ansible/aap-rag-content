# 12. Usage reporting with metrics-utility
## 12.3. Modifying the run schedule
### 12.3.1. Modifying the run schedule on OpenShift Container Platform from the Ansible Automation Platform operator




To adjust the execution schedule of the `metrics-utility` within your Ansible Automation Platform deployment running on OpenShift Container Platform, use the following procedure:

**Procedure**

1. From the navigation panel, selectWorkloads→Deployments.
1. On the next screen, select **automation-controller-operator-controller-manager** .
1. Beneath the heading **Deployment Details** , click the down arrow button to change the number of pods to zero. This pauses the deployment so you can update the running schedule.
1. From the navigation panel, select **Installed Operators** .
1. From the list of installed operators, select Ansible Automation Platform.
1. On the next screen, select the automation controller tab.
1. From the list that appears, select your automation controller instance.
1. On the next screen, select the `    YAML` tab.
1. In the `    YAML` file, find the following parameters and enter a variable representing how often `    metrics-utility` should gather data and how often it should produce a report:

`    metrics_utility_cronjob_gather_schedule:`

`    metrics_utility_cronjob_report_schedule:`


1. ClickSave.
1. From the navigation menu, selectDeploymentsand then select **automation-controller-operator-controller-manager** .
1. Increase the number of pods to 1.
1. To verify that you have changed the `    metrics-utility` running schedule successfully, you can take one or both of the following steps:


1. Return to the `        YAML` file and ensure that the previously described parameters reflect the correct variables.
1. From the navigation menu, selectWorkloads→Cronjobsand ensure that your cronjobs show the updated schedule.



