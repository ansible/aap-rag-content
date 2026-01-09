# 6. Jobs
## 6.3. Issue - Jobs in automation controller are stuck in a pending state




After launching jobs in automation controller, the jobs stay in a pending state and do not start.

There are a few reasons jobs can become stuck in a pending state. For more information about troubleshooting this issue, see [Playbook stays in pending](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/configuring_automation_execution/controller-troubleshooting#controller-playbook-pending) in _Configuring automation execution_

**Procedure**

1. Run the following commands to list all of the pending jobs:


```
# awx-manage shell_plus
```


```
&gt;&gt;&gt; UnifiedJob.objects.filter(status='pending')
```


1. Cancel the pending jobs by using one of the following methods:


- To cancel all pending jobs, run the following command:


```
&gt;&gt;&gt; UnifiedJob.objects.filter(status='pending').update(status='canceled')
```


- To cancel a single job, run the following command, replacing `        &lt;job_id&gt;` with the job ID to cancel:


```
&gt;&gt;&gt; UnifiedJob.objects.filter(id=&lt;job_id&gt;).update(status='canceled')
```





