# 5. Jobs in automation controller
## 5.4. Automation controller capacity determination and job impact
### 5.4.2. Capacity job impacts




When selecting the capacity, it is important to understand how each job type affects capacity.

The default forks value for Ansible is five. However, if you set up automation controller to run against fewer systems than that, then the actual concurrency value is lower.

When a job is run in automation controller, the number of forks selected is incremented by 1, to compensate for the Ansible parent process.

**Example**

If you run a playbook against five systems with forks value of 5, then the actual forks value from the Job Impact perspective is 6.


#### 5.4.2.1. Impact of job types in automation controller




Jobs and ad hoc jobs follow the preceding model, forks +1. If you set a fork value on your job template, your job capacity value is the minimum of the forks value supplied and the number of hosts that you have, plus one. The +1 is to account for the parent Ansible process.

Instance capacity determines which jobs get assigned to any specific instance. Jobs and ad hoc commands use more capacity if they have a higher forks value.

Job types including the following, have a fixed impact:

- Inventory updates: 1
- Project updates: 1
- System jobs: 5


Note
If you do not set a forks value on your job template, your job uses Ansible’s default forks value of five. However, it uses fewer if your job has fewer than five hosts. In general, setting a forks value higher than what the system is capable of can cause issues by running out of memory or over-committing CPU. The job template fork values that you use must fit on the system. If you have playbooks using 1000 forks but none of your systems individually has that much capacity, then your systems are undersized and at risk of performance or resource issues.



#### 5.4.2.2. Selecting the correct capacity




Selecting a capacity out of the CPU-bound or the memory-bound capacity limits is selecting between the minimum or maximum number of forks. In the [previous examples](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/using_automation_execution/index#controller-memory-relative-capacity) , the CPU capacity permits a maximum of 16 forks while the memory capacity permits 20. For some systems, the disparity between these can be large and you might want to have a balance between these two.

The instance field `capacity_adjustment` enables you to select how much you want to consider. It is represented as a value between 0.0 and 1.0. If set to a value of 1.0, then the largest value is used. The previous example involves memory capacity, so a value of 20 forks can be selected. If set to a value of 0.0 then the smallest value is used. A value of 0.5 is a 50/50 balance between the two algorithms, which is 18:

```
16 + (20 - 16) * 0.5 = 18
```

**Procedure**

View or edit the capacity:


1. From the navigation panel, selectAutomation Execution→Infrastructure→Instance Groups.
1. On the **Instance Groups** list view, select the required instance.
1. Select the **Instances** tab and adjust the **Capacity adjustment** slider.

Note
The slider adjusts whether the instance capacity algorithm yields less forks (towards the left) or yields more forks (towards the right).






