# 11. Subscription management in Ansible Automation Platform and automation controller
## 11.3. Keeping your subscription in compliance
### 11.3.2. Viewing Hosts automated in the CLI




Automation controller provides a way to generate a CSV output of the host metric data and host metric summary through the _Command Line Interface_ (CLI). You can also soft delete hosts in bulk through the API.

#### 11.3.2.1. awx-manage utility




The `awx-manage` utility supports the following options:

```
awx-manage host_metric --csv
```

This command produces host metric data, a host metrics summary file, and a cluster info file. To package all the files into a single tarball for distribution and sharing use:

```
awx-manage host_metric --tarball
```

To specify the number of rows ( `&lt;n&gt;` ) to output to each file:

```
awx-manage host_metric --tarball --rows_per_file &lt;n&gt;
```

Automation Analytics receives and uses the JSON file.

For more information on using `metrics-utility` CLI, see [Configuring automation execution](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/configuring_automation_execution) /assembly-controller-metrics[Usage reporting with metrics-utility]

