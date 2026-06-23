# Control where automation runs with container groups
## Verify the container group functions

Verify the deployment and termination of your container.

### Procedure

1.  Create a mock inventory and associate the container group to it by populating the name of the container group in the **Instance groups** field. For more information, see [Add a new inventory](/documentation/en-us/red_hat_ansible_automation_platform/2.7/proc_controller_adding_new_inventory "To add a new inventory, you must configure permissions, groups, hosts, and sources, then view the completed jobs.").
![Create test inventory](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/ag-inventories-create-new-test-inventory.png)
2.  Create the `localhost` host in the inventory with the following variables:


```
{'ansible_host': '127.0.0.1', 'ansible_connection': 'local'}
```

3.  Launch an ad hoc job against the localhost using the *ping* or *setup* module. Even though the **Machine Credential** field is required, it does not matter which one is selected for this test:
![Launch ad hoc localhost](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/ag-inventories-launch-adhoc-localhost.png)

![Launch ad hoc localhost 2](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/ag-inventories-launch-adhoc-localhost2.png)

### Results

You can see in the **Jobs** details view that the container was reached successfully by using one of the ad hoc jobs.

If you have an OpenShift UI, you can see pods appear and disappear as they deploy and end. You can also use the CLI to perform a `get pod` operation on your namespace to watch these same events occurring in real-time.

