# Understand primary workloads for automation controller
## Jobs and automation workloads
### System jobs

System jobs involve internal maintenance tasks, such as clean up of old job event data. The execution frequency of system jobs is managed by schedules. System jobs run on the control plane, because they run management commands that interact with the database. These workloads involve key platform activities.

Reducing the frequency of system jobs or increasing the number of days of data to retain can degrade database performance. It is generally recommended to retain as few days of data as possible. Use external logging features for long-term audit data storage. Storing more data in the database can make queries that scan large tables more costly.

