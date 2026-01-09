# 8. Workflow job templates
## 8.7. Workflow visualizer
### 8.7.3. Building nodes scenarios




Learn how to manage nodes in the following scenarios.

**Procedure**

1. Click the (![Plus icon](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Using_automation_execution-en-US/images/65fed3eab4f6ac2075ffa1b3caa55e46/options_menu.png)
) icon on the parent node and **Add step and link** to add a sibling node:

![Create sibling node](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Using_automation_execution-en-US/images/1effaa69b00b49d2df1c7770bba2fcd5/ug-wf-create-sibling-node.png)



1. ClickAdd steporStart(![Plus icon](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Using_automation_execution-en-US/images/65fed3eab4f6ac2075ffa1b3caa55e46/options_menu.png)
) and **Add step** , to add a root node to depict a split scenario.
1. At any node where you want to create a split scenario, hover over the node from which the split scenario begins and click the plus (![Plus icon](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Using_automation_execution-en-US/images/65fed3eab4f6ac2075ffa1b3caa55e46/options_menu.png)
) icon on the parent node and **Add step and link** . This adds multiple nodes from the same parent node, creating sibling nodes.
1. Refer to the key by clickingLegendto identify the meaning of the symbols and colors associated with the graphical depiction.

Note
If you remove a node that has a follow-on node attached to it in a workflow with a set of sibling nodes that has varying edge types, the attached node automatically joins the set of sibling nodes and retains its edge type:






