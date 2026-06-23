# Use TF Actions with Event-Driven Ansible
## Create and apply the plan

After you configure your Terraform plan to include Event-Driven Ansible events, you create and apply the plan to trigger the events.

### Procedure

1.  Run `terraform init` to initialize your working directory.
2.  Use `terraform plan` to commit to create the plan. The following example also saves the plan to a file named `tfplan.out`, but you can specify any name for the plan. Saving the plan is a best practice for automation because the saved plan is strictly enforced.

```
terraform plan -out=tfplan.out
```

3.  Review the plan output.
4.  Apply the saved plan.

```
terraform apply tfplan.out
```
This creates and sends an event to the specified event stream. As each resource is created, TF actions are invoked and the corresponding Ansible Automation Platform playbooks are executed sequentially.

### Results

1. Verify that the runs are updated in the Terraform user interface. Drill down on a resource to see that the action was invoked and a post event was executed.
2. From the Ansible Automation Platform user interface, verify that the event is successfully received by (EDAName} and triggers the appropriate rulebook activation:
1. Check the **Event Streams** dashboard to see the TF Actions events were received.
2. Check the **Jobs** dashboard to see the jobs running sequentially and with a **Success** status.
3. Check the **Inventory** dashboard to see the updates. For example, if you created new servers, check the **Hosts** tab for the Terraform provisioned inventory.

