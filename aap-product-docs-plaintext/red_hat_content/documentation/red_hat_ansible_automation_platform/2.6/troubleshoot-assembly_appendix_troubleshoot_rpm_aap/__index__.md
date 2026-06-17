# Troubleshoot your RPM-based deployment of Ansible Automation Platform

Resolve common installation issues and errors that can occur when installing RPM-based Ansible Automation Platform. Learn how to generate diagnostic logs to identify problems.

## Gather Ansible Automation Platform logs

Run the setup script with the `-s` flag to collect diagnostic data from all nodes. This generates an `sos` report used by Red Hat Technical Support to resolve service requests.

### Procedure

1.  Access the installation program folder with the inventory file and run the installation program setup script the following command:
`$ ./setup.sh -s`

With this command, you can connect to each node present in the inventory, install the `sos` tool, and generate new logs.

Note:
If you are running the setup as a non-root user with sudo privileges, you can use the following command:

```
$ ANSIBLE_BECOME_METHOD='sudo'
ANSIBLE_BECOME=True ./setup.sh -s
```

2.  *Optional*: If required, change the location of the `sos` report files. The `sos` report files are copied to the `/tmp` folder for the current server. To change the location, specify the new location by using the following command:

```
$ ./setup.sh -e 'target_sos_directory=/path/to/files' -s
```
Where `target_sos_directory=/path/to/files` is used to specify the destination directory where the `sos` report will be saved. In this case, the `sos` report is stored in the directory `/path/to/files`.

3.  Gather the files described on the playbook output and share with the support engineer or directly upload the `sos` report to Red Hat. To create an `sos` report with additional information or directly upload the data to Red Hat, use the following command:

```
$ ./setup.sh -e 'case_number=0000000' -e 'clean=true' -e 'upload=true' -s
```
*Table 1. Parameter Reference Table*

| Parameter          | Description                                                              | Default value |
| ------------------ | ------------------------------------------------------------------------ | ------------- |
| <br> `case_number` | <br>Specifies the support case number that you want.                     | <br>-         |
| <br> `clean`       | <br>Obfuscates sensitive data that might be present on the `sos` report. | <br> `false`  |
| <br> `upload`      | <br>Automatically uploads the `sos` report data to Red Hat.              | <br> `false`  |
