# 11. Subscription management in Ansible Automation Platform and automation controller
## 11.3. Keeping your subscription in compliance
### 11.3.2. Viewing Hosts automated in the CLI




Automation controller provides a way to generate a CSV output of the host metric data and host metric summary through the _Command Line Interface_ (CLI). You can also soft delete hosts in bulk through the API.

#### 11.3.2.1. awx-manage utility




To collect and manage host metric data and related cluster information in Ansible Automation Platform, use the `awx-manage` utility.

**Procedure**

1. The `    awx-manage` utility supports the following options:


```
awx-manage host_metric --csv
```


1. This command produces host metric data in CSV format, a host metrics summary file, and a cluster info file.
1. To package all the files into a single tar file for distribution and sharing, use:


```
awx-manage host_metric --tarball
```


1. To specify the number of rows ( `    &lt;n&gt;` ) to output to each file:


```
awx-manage host_metric --tarball --rows_per_file &lt;n&gt;
```


1. Automation Analytics then receives and uses the JSON file.


**Additional resources**

-  [Usage reporting with metrics-utility](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/configuring_automation_execution/metrics-utility)


