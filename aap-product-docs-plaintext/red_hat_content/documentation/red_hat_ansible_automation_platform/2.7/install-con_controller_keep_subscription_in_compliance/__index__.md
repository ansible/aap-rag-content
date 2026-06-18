# Keep subscriptions for managed hosts in compliance

To ensure that your automation controller installation remains compliant with your Red Hat subscription, automation controller provides a way to monitor your subscription status and usage.

Your subscription has two possible statuses:

- **Compliant**: Indicates that your subscription is appropriate for the number of hosts that you have automated within your subscription count.
- **Out of compliance**: Indicates that you have exceeded the number of hosts in your subscription.


Compliance is computed as follows:

```
managed > manifest_limit    =>  non-compliant
managed =< manifest_limit   =>  compliant
```
Where: `managed` is the number of unique managed hosts without deletions, and `manifest_limit` is the number of managed hosts in the subscription manifest.

Other important information displayed are:

- **Hosts automated**: The number of hosts automated by the job, which consumes the license count.
- **Hosts imported**: The number of hosts considering unique host names across all inventory sources. This number does not impact hosts remaining.
- **Hosts remaining**: The number of hosts minus the number of hosts automated.
- **Hosts deleted**: The number of hosts that were deleted, freeing the license capacity.
- **Active hosts previously deleted**: The number of hosts now active that were previously deleted.


For example, if you have a subscription capacity of 10 hosts:

- Starting with 9 hosts, 2 hosts were added and 3 hosts were deleted, you now have 8 hosts (compliant).
- 3 hosts were automated again, now you have 11 hosts, which puts you over the subscription limit of 10 (noncompliant).
- If you delete hosts, refresh the subscription details to see the change in count and status.

## View hosts automated in the user interface

Learn how to view and manage the hosts that have been automated in automation controller.

### Procedure

1.  In the navigation panel, select Automation Analytics> (and then)Host Metrics to view the activity associated with hosts, such as those that have been automated and deleted. Each unique hostname is listed and sorted by the user’s preference. ![Host metrics](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/ug-host-metrics.png)

Note:
A scheduled task automatically updates these values on a weekly basis and deletes jobs with hosts that were last automated more than a year ago.

2.  Delete unnecessary hosts directly from the Host Metrics view by selecting the required hosts and clicking Delete. These are soft-deleted, meaning their records are not removed, but are not being used and thereby not counted towards your subscription.

## View hosts automated in the CLI

Automation controller provides a way to generate a CSV output of the host metric data and host metric summary through the *Command Line Interface* (CLI). You can also soft delete hosts in bulk through the API.

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

## Deleting Hosts automated using API endpoint

You can soft delete hosts that have been automated in automation controller using the host metric API endpoint.

The API lists only non-deleted records and are sortable by last_automation and used_in_inventories columns.

To soft delete hosts, use:

`api/v2/host_metric <n> DELETE`

A monthly scheduled task automatically deletes jobs that uses hosts from the Host Metric table that were last automated more than a year ago.
