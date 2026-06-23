# Configure the metrics-utility to run at specific times
## Modify the run schedule on OpenShift Container Platform from the Ansible Automation Platform operator

To adjust the execution schedule of the `metrics-utility` within your Ansible Automation Platform deployment running on OpenShift Container Platform, use the following procedure.

### Procedure

1.  From the navigation panel, select Workloads> (and then)Deployments.
2.  On the next screen, select **automation-controller-operator-controller-manager**.
3.  Beneath the heading **Deployment Details**, click the down arrow button to change the number of pods to zero. This pauses the deployment so you can update the running schedule.
4.  From the navigation panel, select **Installed Operators**.
5.  From the list of installed operators, select Ansible Automation Platform.
6.  On the next screen, select the automation controller tab.
7.  From the list displayed, select your automation controller instance.
8.  On the next screen, select the `YAML` tab.
9.  In the `YAML` file, find the following parameters and enter a variable representing how often `metrics-utility` should gather data and how often it should produce a report:
`metrics_utility_cronjob_gather_schedule:`

`metrics_utility_cronjob_report_schedule:`

10.  Click Save.
11.  From the navigation menu, select Deployments and then select **automation-controller-operator-controller-manager**.
12.  Increase the number of pods to 1.
13.  To verify that you have changed the `metrics-utility` running schedule successfully, you can take one or both of the following steps:
1.  Return to the `YAML` file and ensure that the previously described parameters reflect the correct variables.
2.  From the navigation menu, select Workloads> (and then)Cronjobs and ensure that your cronjobs show the updated schedule.
