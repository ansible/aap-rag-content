# 6. Jobs
## 6.3. Issue - Jobs in automation controller are stuck in a pending state

After launching jobs in automation controller, the jobs stay in a pending state and do not start.

There are a few reasons jobs can become stuck in a pending state. For more information about troubleshooting this issue, see [Playbook stays in pending](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/configuring_automation_execution/controller-troubleshooting#controller-playbook-pending) in *Configuring automation execution*

**Procedure**

1. Run the following commands to list all of the pending jobs:

# awx-manage shell_plus

>>> UnifiedJob.objects.filter(status='pending')

2. Cancel the pending jobs by using one of the following methods:


- To cancel all pending jobs, run the following command:

>>> UnifiedJob.objects.filter(status='pending').update(status='canceled')

- To cancel a single job, run the following command, replacing `<job_id>` with the job ID to cancel:

>>> UnifiedJob.objects.filter(id=<job_id>).update(status='canceled')

