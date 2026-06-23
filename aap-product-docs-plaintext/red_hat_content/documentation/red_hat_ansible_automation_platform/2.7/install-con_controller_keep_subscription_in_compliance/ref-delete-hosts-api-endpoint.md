# Keep subscriptions for managed hosts in compliance
## Deleting Hosts automated using API endpoint

You can soft delete hosts that have been automated in automation controller using the host metric API endpoint.

The API lists only non-deleted records and are sortable by last_automation and used_in_inventories columns.

To soft delete hosts, use:

`api/v2/host_metric <n> DELETE`

A monthly scheduled task automatically deletes jobs that uses hosts from the Host Metric table that were last automated more than a year ago.
