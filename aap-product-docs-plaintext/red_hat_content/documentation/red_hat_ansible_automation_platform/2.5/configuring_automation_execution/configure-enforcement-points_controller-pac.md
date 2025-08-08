# 7. Implementing policy enforcement
## 7.3. Configuring enforcement points




After you have set up your Ansible Automation Platform instance to communicate with the OPA server, you can set up enforcement points where you want the policy to be applied.

You can associate a policy with a job template, an inventory, or an organization. Enforcement then occurs in the following ways:

Note
If you do not associate a policy with a resource, policy evaluation will not occur when you run the related job.



