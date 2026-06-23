# Job type impact on capacity

When configuring automation controller capacity, it is important to understand how different job types impact the system capacity.

automation controller uses Ansible to run jobs. Each job can have a different impact on system resources depending on the number of forks used for the job.

The default forks value for Ansible is five. This means that, by default, each job can run tasks on up to five systems concurrently.

However, if you set up automation controller to run against fewer systems than that, then the actual concurrency value is lower.

When a job is run in automation controller, the number of forks selected is incremented by 1, to compensate for the Ansible parent process.

For example, if you run a playbook against five systems with forks value of 5, then the actual forks value from the Job Impact perspective is 6.

