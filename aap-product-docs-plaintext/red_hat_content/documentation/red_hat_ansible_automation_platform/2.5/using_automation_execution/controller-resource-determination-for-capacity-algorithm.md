# 5. Jobs in automation controller
## 5.4. Automation controller capacity determination and job impact
### 5.4.1. Resource determination for capacity algorithm




Capacity algorithms determine how many forks a system is capable of running simultaneously. These algorithms control how many systems Ansible can communicate with simultaneously. Increasing the number of forks an automation controller system is running enables jobs to run faster by performing more work in parallel. However, this increases the load on the system, which can cause work to slow down.

The default, `mem_capacity` , enables you to over-commit processing resources while protecting the system from running out of memory. If most of your work is not processor-bound, then selecting this mode maximizes the number of forks.

#### 5.4.1.1. Memory relative capacity




`mem_capacity` is calculated relative to the amount of memory needed per fork. Taking into account the overhead for internal components, this is about 100MB per fork. When considering the amount of memory available to Ansible jobs, the capacity algorithm reserves 2GB of memory to account for the presence of other services. The algorithm formula for this is:

```
(mem - 2048) / mem_per_fork
```

The following is an example:

```
(4096 - 2048) / 100 == ~20
```

A system with 4GB of memory is capable of running 20 forks. The value `mem_per_fork` is controlled by setting the value of `SYSTEM_TASK_FORKS_MEM` , which defaults to 100.

#### 5.4.1.2. CPU relative capacity




Ansible workloads are often processor-bound. In such cases, you can reduce the simultaneous workload to enable more tasks to run faster and reduce the average time-to-completion of those jobs.

Just as the `mem_capacity` algorithm adjusts the amount of memory required per fork, the `cpu_capacity` algorithm adjusts the amount of processing resources required per fork. The baseline value for this is four forks per core. The algorithm formula for this is:

```
cpus * fork_per_cpu
```

For example, a 4-core system looks like the following:

```
4 * 4 == 16
```

You can control the value of `fork_per_cpu` by setting the value of `SYSTEM_TASK_FORKS_CPU` which defaults to 4.

