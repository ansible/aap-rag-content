# 1. View key usage metrics with Automation Dashboard
## 1.7. Analyzing costs and savings




The costs and savings analysis compares the cost of manual automation compared to the cost of automation execution by using Ansible Automation Platform to calculate the total savings derived from automation execution.

**Procedure**

1. Use the **Average cost per minute to manually run the job** field to enter the average cost per minute for an engineer to manually run jobs.
1. Use the **Average cost per minute of running on Ansible Automation Platform** field to enter an average cost per minute of running a job using Ansible Automation Platform.
1. Select **Time taken to create automation into calculation** to include the costs associated with creating the initial or ongoing automation execution.

Automation Dashboard supplies the following data:


-  **Cost of manual automation** : This number represents the estimated cost of manually performing all of the automated tasks. This is an estimated value, not an actual expenditure. It represents the potential expenses that the organization would incur without automation. The calculation is based on the time taken to manually run each job, multiplied by a labor cost rate.
-  **Cost of automated execution** : This is the cost of automation execution using Ansible Automation Platform. This cost includes the resources consumed by Ansible Automation Platform, such as server time, processing power, and any other operational expenses associated with automation execution. It represents the actual cost incurred for automation execution.
-  **Total savings/cost avoided** : This is the difference between the **Cost of manual automation** and the **Cost of automated execution** . This is a key metric for demonstrating the return on investment attainable by using Ansible Automation Platform.
-  **Total hours saved/avoided** : This figure is calculated by adding host executions and automation creation time, then subtracting the running time in minutes.
-  **Time taken to manually execute (min)** : This metric represents the amount of time it would take for a user to perform the task manually on a host. It is an input provided to compare the value of manual execution and automated execution using the time taken by the organization to manually automate.

Note
You can export the data from your cost and savings analysis as a CSV.







