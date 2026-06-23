# Ensure system health and efficiency through monitoring
## System level monitoring

Monitoring CPU and memory is vital since instance capacity management doesn't introspect host resource usage. Automation impact varies by playbook; cloud modules process on the execution node, while native modules like "yum" perform work on target hosts, leaving the node waiting for results.

If CPU or memory usage is very high, consider lowering the capacity adjustment (available on the instance detail page) on affected instances in the automation controller. This limits how many jobs are run on or controlled by this instance.

Monitor the disk I/O and use of your system. The manner in which an automation controller node runs Ansible and caches output on the file system, and eventually saves it in the database, creates high levels of disk reads and writes. Identifying poor disk performance early can help prevent poor user experience and system degradation.
