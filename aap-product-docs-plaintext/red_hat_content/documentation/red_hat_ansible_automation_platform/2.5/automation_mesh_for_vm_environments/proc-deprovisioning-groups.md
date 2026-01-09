# 4. Deprovisioning individual nodes or groups
## 4.3. Deprovisioning groups using the installer




You can deprovision entire groups from your automation mesh using the Ansible Automation Platform installer. Running the installer will remove all configuration files and logs attached to the nodes in the group.

Note
You can deprovision any hosts in your inventory except for the first host specified in the `[automationcontroller]` group.



**Procedure**

- Add `    <span class="strong strong"><strong><span class="Role ARG Spec Role ARG Spec">node_state=deprovision</span></strong></span>` to the [group:vars] associated with the group you want to deprovision.



<span id="idm140138490675120"></span>
**Example 4.2. Group deprovision**

```
[execution_nodes]
execution-node-1.example.com peers=execution-node-2.example.com
execution-node-2.example.com peers=execution-node-3.example.com
execution-node-3.example.com peers=execution-node-4.example.com
execution-node-4.example.com peers=execution-node-5.example.com
execution-node-5.example.com peers=execution-node-6.example.com
execution-node-6.example.com peers=execution-node-7.example.com
execution-node-7.example.com

[execution_nodes:vars]
node_state=deprovision
```




