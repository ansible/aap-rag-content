# 5. Jobs in automation controller
## 5.3. Playbook run jobs
### 5.3.1. Search




Use **Search** to look up specific events, hostnames, and their statuses. To filter only certain hosts with a particular status, specify one of the following valid statuses:

The following example shows a search with only unreachable hosts:

![Stdout pane unreachable](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Using_automation_execution-en-US/images/eced011387832440e5da14d93e0fca53/ug-std-out-unreachable.png)


For more information about using the search, see the [Search](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/using_automation_execution/assembly-controller-search) section.

The standard output view displays the events that occur on a particular job.

Click a line of an event from the **Stdout** pane and a **Host Events** window displays in a separate window. This window shows the host that was affected by that particular event.

Note
Upgrading to the latest versions of Ansible Automation Platform involves progressively migrating all historical playbook output and events. This migration process is gradual, and happens automatically in the background after installation is complete. Installations with very large amounts of historical job output (tens or hundreds of GB of output) can have missing job output until migration is complete. The most recent data shows up at the top of the output, followed by older events.



