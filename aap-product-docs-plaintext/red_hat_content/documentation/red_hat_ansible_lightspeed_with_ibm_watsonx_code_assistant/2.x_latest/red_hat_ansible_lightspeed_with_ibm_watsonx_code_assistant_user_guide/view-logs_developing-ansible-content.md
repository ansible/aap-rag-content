# 4. Developing Ansible content
## 4.6. Viewing the audit logs




The Ansible Visual Studio (VS Code) extension now records all Red Hat Ansible Lightspeed operations in an audit log for future use. Each interaction is recorded with a timestamp, the type of action performed, details of the requested task, and other relevant information. The logs are displayed in the Ansible Lightspeed Output Channel of the VS Code editor and are available until you close VS Code.

**Procedure**

1. Open VS Code.
1. Open the Command Palette of the VS Code editor.
1. ClickOutput→Show Output Channels, and then select **Ansible Lightspeed** .

An **Output** panel is displayed at the bottom of the VS Code editor with a log of all user actions.




Following is an example of an audit log:


<span id="idm139960283621984"></span>
**Figure 4.8. Audit log**

![Audit log](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Lightspeed_with_IBM_watsonx_Code_Assistant-2.x_latest-Red_Hat_Ansible_Lightspeed_with_IBM_watsonx_Code_Assistant_User_Guide-en-US/images/756000f459f9d589fc89bfd86e240e8b/example_view_logs.png)




