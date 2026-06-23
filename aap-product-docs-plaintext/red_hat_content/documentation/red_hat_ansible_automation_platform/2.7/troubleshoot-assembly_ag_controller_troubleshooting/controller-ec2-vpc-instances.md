# Troubleshoot automation controller
## View private EC2 VPC instances in the automation controller inventory

By default, automation controller only shows instances in a VPC that have an Elastic IP (EIP) associated with them.

### Procedure

1.  From the navigation panel, select Automation Execution> (and then)Infrastructure> (and then)Inventories.
2.  Select the inventory that has the **Source** set to **Amazon EC2**, and click the **Source** tab. In the **Source Variables** field, enter:

```
vpc_destination_variable: private_ip_address
```

3.  Click Save and trigger an update of the group.

### Results

Once you complete these steps, you can see your VPC instances.

Note:

Automation controller must be running inside the VPC with access to those instances if you want to configure them.
