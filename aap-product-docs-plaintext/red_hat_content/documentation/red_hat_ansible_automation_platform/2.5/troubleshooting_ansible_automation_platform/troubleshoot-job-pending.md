# 6. Jobs
## 6.3. Issue - Jobs in automation controller are stuck in a pending state




After launching jobs in automation controller, the jobs stay in a pending state and do not start.

There are a few reasons jobs can become stuck in a pending state. For more information about troubleshooting this issue, see [Playbook stays in pending](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/configuring_automation_execution/controller-troubleshooting#controller-playbook-pending) in _Configuring automation execution_

**Cancel all pending jobs**

1. Run the following commands to list all of the pending jobs:


```
# awx-manage shell_plus
```


```
&gt;&gt;&gt; UnifiedJob.objects.filter(status='pending')
```


1. Run the following command to cancel all of the pending jobs:


```
&gt;&gt;&gt; UnifiedJob.objects.filter(status='pending').update(status='canceled')
```




**Cancel a single job by using a job id**

- To cancel a specific job, run the following commands, replacing `    <span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">&lt;job_id&gt;</span></em></span>` with the job id to cancel:


```
# awx-manage shell_plus
```


```
&gt;&gt;&gt; UnifiedJob.objects.filter(id=_&lt;job_id&gt;_).update(status='canceled')
```




