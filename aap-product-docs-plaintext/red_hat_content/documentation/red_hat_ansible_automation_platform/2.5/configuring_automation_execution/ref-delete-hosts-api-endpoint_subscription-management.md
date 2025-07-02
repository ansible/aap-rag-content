# 11. Subscription management in Ansible Automation Platform and automation controller
## 11.3. Keeping your subscription in compliance
### 11.3.3. Deleting Hosts automated using API endpoint




The API lists only non-deleted records and are sortable by last_automation and used_in_inventories columns.

You can use the host metric API endpoint, `api/v2/host_metric` to soft delete hosts, using:

`api/v2/host_metric &lt;n&gt; DELETE`

A monthly scheduled task automatically deletes jobs that uses hosts from the Host Metric table that were last automated more than a year ago.

