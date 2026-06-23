# Configure the `metrics-utility` to run at specific times

You can configure `metrics-utility` to run at specified times and intervals. Run frequency is expressed in cronjobs. For more information on the cron utility, see [How to schedule jobs using the Linux `Cron` utility](https://www.redhat.com/sysadmin/linux-cron-command).

## About this task

To modify the run schedule on Red Hat Enterprise Linux and on OpenShift Container Platform, use one of the following procedures:

## Procedure

1.  From the command line, run:
`crontab -e`

2.  After the code editor has opened, update the `gather` and `build` parameters using cron syntax as shown below:
`*/2 * * * * metrics-utility gather_automation_controller_billing_data --ship --until=10m`

`*/5 * * * * metrics-utility build_report`

3.  Save and close the file.

