# Troubleshoot your containerized deployment
## Gather logs from your containerized deployment

Use the `sos` utility to collect configuration and diagnostic data for Red Hat Technical Support. An `sos` report is the standard starting point for troubleshooting.

### About this task

You can collect an `sos` report for each host in your containerized Ansible Automation Platform deployment by running the `log_gathering` playbook with the appropriate parameters.

### Procedure

1.  Go to the Ansible Automation Platform installation directory.
2.  Run the `log_gathering` playbook. This playbook connects to each host in the inventory file, installs the `sos` tool, and generates the `sos` report.

```
$ ansible-playbook -i <path_to_inventory_file> ansible.containerized_installer.log_gathering
```

3.  To collect container-level logs, run the `sos` report directly on each host with the `aap_containerized` plugin enabled:


```
$ sudo sos report -e aap_containerized -k aap_containerized.username=*<username>*
```
where *<username>* is the service account or user running the containerized installation.

4.  Optional: To define additional parameters, specify them with the `-e` option. For example:


```
$ ansible-playbook -i <path_to_inventory_file> ansible.containerized_installer.log_gathering -e 'target_sos_directory=<path_to_files>' -e 'case_number=0000000' -e 'clean=true' -e 'upload=true' -s
```
1.  You can use the `-s` option to step through each task in the playbook and confirm its execution. This is optional but can be helpful for debugging.
2.  The following is a list of the parameters you can use with the `log_gathering` playbook:
*Table 1. Parameter reference*

| Parameter name              | Description                                                              | Default                                     |
| --------------------------- | ------------------------------------------------------------------------ | ------------------------------------------- |
| <br> `target_sos_directory` | <br>Used to change the default location for the `sos` report files.      | <br>`/tmp` directory of the current server. |
| <br> `case_number`          | <br>Specifies the support case number if relevant to the log gathering.  |                                             |
| <br> `clean`                | <br>Obfuscates sensitive data that might be present on the `sos` report. | <br> `false`                                |
| <br> `upload`               | <br>Automatically uploads the `sos` report data to Red Hat.              | <br> `false`                                |

5.  Gather the `sos` report files described in the playbook output and share them with the support engineer or directly upload the `sos` report to Red Hat using the `upload=true` additional parameter.

