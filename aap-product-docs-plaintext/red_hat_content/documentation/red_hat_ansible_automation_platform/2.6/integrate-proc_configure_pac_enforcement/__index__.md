# Configure enforcement points

After you have set up your Ansible Automation Platform instance to communicate with the OPA server, you can set up enforcement points where you want the policy to be applied.

## Procedure

You can associate a policy with a job template, an inventory, or an organization. Enforcement then occurs in the following ways:

Organization
Jobs launched from a template owned by an organization will fail if the policy is violated. This configuration provides broad control over automation within organizational boundaries.

Inventory
Jobs that use an inventory associated with a policy fail if the policy is violated. This configuration allows you to control access to specific infrastructure resources.

Job template
Jobs launched from a template associated with a policy fail if the job violates the associated policy. This configuration provides granular control over specific automation tasks.

Note:

If you do not associate a policy with a resource, policy evaluation will not occur when you run the related job.

## Associate a policy with an organization

Learn how to associate a policy with an organization.

### Procedure

1.  From the navigation panel, select Access Management> (and then)Organizations.
2.  On the **Organizations** page:
1.  To edit an existing organization, find the organization you want to edit and click the pencil icon ![Edit page](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/leftpencil.png) to go to the editing screen.
2.  To create a new organization, click Create organization.
3.  In the field labeled **Policy enforcement**, enter the query path associated with the policy you want to implement. You must format the query path as `package/rule`.
4.  Click Next and then Finish to save your settings.

## Associate a policy with an inventory

Learn how to associate a policy with an inventory.

### Procedure

1.  From the navigation panel, select Automation Execution> (and then)Infrastructure> (and then)Inventories.
2.  On the **Inventories** page:
1.  To edit an existing inventory, find the inventory you want to edit and click the pencil icon ![Edit page](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/leftpencil.png) to go to the editing screen.
2.  To create a new inventory, click Create inventory.
3.  In the field titled **Policy enforcement.**, enter the query path associated with the policy you want to implement. You must format the query path as `package/rule`.
4.  Click Save inventory if you are editing an existing inventory, or click Create inventory if you are creating a new inventory.

## Associate a policy with a job template

Learn how to associate a policy with a job template.

### Procedure

1.  From the navigation panel, select Automation Execution> (and then)Templates.
2.  On the **Automation Templates** page:
1.  To edit an existing job template, find the job template you want to edit and click the pencil icon ![Edit page](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/leftpencil.png) to go to the editing screen.
2.  To create a new job template, click Create template.
3.  In the field titled **Policy enforcement**, enter the query path associated with the policy you want to implement. You must format the query path as `package/rule`.
4.  Click Save job template if you are editing an existing job template, or click Create job template if you are creating a new job template.
