# Add a source to an inventory
## Source an inventory from Amazon Web Services EC2

Use the following procedure to configure an AWS EC2-sourced inventory.

### Procedure

1.  From the navigation panel, select Automation Execution> (and then)Infrastructure> (and then)Inventories.
2.  Select the inventory name you want a source to and click the **Sources** tab.
3.  Click Create source.
4.  In the **Create source** page, select **Amazon EC2** from the **Source** list.
5.  The **Create source** window expands with additional fields. Enter the following details:

- Optional: **Credential**: Choose from an existing AWS credential. For more information, see [Managing user credentials](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_controller_credentials#controller-credentials "Credentials authenticate the automation controller user when launching jobs against machines, synchronizing with inventory sources, and importing project content from a version control system."). If automation controller is running on an EC2 instance with an assigned IAM Role, the credential can be omitted, and the security credentials from the instance metadata are used instead. For more information about using IAM Roles, see [IAM roles for Amazon EC2_documentation_at_Amazon](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html) documentation at Amazon.

6.  Optional: You can specify the verbosity, host filter, enabled variables or values, and update options as described in [Adding a source](/documentation/en-us/red_hat_ansible_automation_platform/2.7/administer-proc_controller_add_source#proc-controller-add-source "Use the following procedure to add a source to an inventory. When you add a source to an inventory, the system creates a new group for that source.").
7.  Use the **Source variables** field to override variables used by the `aws_ec2` inventory plugin. Enter variables by using either JSON or YAML syntax. Use the radio button to toggle between the two. For more information about these variables, see the [aws inventory plugin documentation](https://console.redhat.com/ansible/automation-hub/repo/published/amazon/aws/content/inventory/aws_ec2).

If you only use `include_filters`, the AWS plugin always returns all the hosts. To use this correctly, the first condition on the `or` must be on `filters` and then build the rest of the `OR` conditions on a list of `include_filters`.

