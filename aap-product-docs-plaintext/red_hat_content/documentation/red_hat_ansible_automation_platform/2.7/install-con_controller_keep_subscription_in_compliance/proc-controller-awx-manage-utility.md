# Keep subscriptions for managed hosts in compliance
## awx-manage utility

To collect and manage host metric data and related cluster information in Ansible Automation Platform, use the `awx-manage` utility.

### Procedure

1.  The `awx-manage` utility supports the following options:


```
awx-manage host_metric --csv
```

2.  This command produces host metric data in CSV format, a host metrics summary file, and a cluster info file.
3.  To package all the files into a single tar file for distribution and sharing, use:


```
awx-manage host_metric --tarball
```

4.  To specify the number of rows (`<n>`) to output to each file:


```
awx-manage host_metric --tarball --rows_per_file <n>
```

5.  Automation Analytics then receives and uses the JSON file.

