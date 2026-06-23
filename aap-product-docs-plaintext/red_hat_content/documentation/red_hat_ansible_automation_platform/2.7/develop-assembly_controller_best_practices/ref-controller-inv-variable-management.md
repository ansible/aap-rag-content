# Best practices for automation execution
## Variable management for inventory

Variables associated with hosts and groups in an inventory can be managed in several ways in automation controller.

Keep variable data with the hosts and groups definitions (see the inventory editor), rather than using `group_vars/` and `host_vars/`. If you use dynamic inventory sources, automation controller can synchronize such variables with the database while the **Overwrite Variables** option is not set.

