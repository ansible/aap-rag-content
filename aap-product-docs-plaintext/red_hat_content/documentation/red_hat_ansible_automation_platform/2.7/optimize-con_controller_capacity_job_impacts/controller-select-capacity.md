# Job type impact on capacity
## Select the correct capacity

When an instance is created, automation controller calculates the capacity of the instance based on two algorithms: CPU-bound and memory-bound. The CPU-bound algorithm calculates the number of forks based on the number of CPU cores available to the instance.

### About this task

The memory-bound algorithm calculates the number of forks based on the amount of memory available to the instance. By default, automation controller selects the minimum number of forks calculated by these two algorithms. This is to ensure that the instance does not overcommit resources. However, in some cases, you might want to adjust this behavior.

Selecting a capacity out of the CPU-bound or the memory-bound capacity limits is selecting between the minimum or maximum number of forks. In the [previous examples](/documentation/en-us/red_hat_ansible_automation_platform/2.7/optimize-con_controller_capacity_determination#controller-memory-relative-capacity "The memory relative capacity option allows you to set the maximum number of concurrent tasks (forks) that can run on a controller based on the amount of memory available on the system. This setting is useful for systems where memory is a limiting factor for running Ansible jobs."), the CPU capacity permits a maximum of 16 forks while the memory capacity permits 20. For some systems, the disparity between these can be large and you might want to have a balance between these two.

The instance field `capacity_adjustment` enables you to select how much you want to consider. It is represented as a value between 0.0 and 1.0. If set to a value of 1.0, then the largest value is used. The previous example involves memory capacity, so a value of 20 forks can be selected. If set to a value of 0.0 then the smallest value is used. A value of 0.5 is a 50/50 balance between the two algorithms, which is 18:

```
16 + (20 - 16) * 0.5 = 18
```

### Procedure

1.  From the navigation panel, select Automation Execution> (and then)Infrastructure> (and then)Instance Groups.
2.  On the **Instance Groups** list view, select the required instance.
3.  Select the **Instances** tab and adjust the **Capacity adjustment** slider. Note:
The slider adjusts whether the instance capacity algorithm yields less forks (towards the left) or yields more forks (towards the right).
