# 12. Usage reporting with metrics-utility
## 12.3. Modifying the run schedule




You can configure `metrics-utility` to run at specified times and intervals. Run frequency is expressed in cronjobs. For more information on the cron utility, see [How to schedule jobs using the Linux ‘Cron’ utility](https://www.redhat.com/sysadmin/linux-cron-command) .

To modify the run schedule on Red Hat Enterprise Linux and on OpenShift Container Platform, use one of the following procedures:

**Procedure**

1. From the command line, run:

`    crontab -e`


1. After the code editor has opened, update the `    gather` and `    build` parameters using cron syntax as shown below:

`    */2 * * * * metrics-utility gather_automation_controller_billing_data --ship --until=10m`

`    */5 * * * * metrics-utility build_report`


1. Save and close the file.


