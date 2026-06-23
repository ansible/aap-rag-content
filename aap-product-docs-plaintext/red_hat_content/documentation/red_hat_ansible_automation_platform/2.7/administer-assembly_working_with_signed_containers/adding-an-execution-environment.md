# Secure your automation with container signing
## Add and sign an execution environment

Push a signed execution environment to your private automation hub for added security.

### Procedure

1.  From the navigation panel, select Automation Content> (and then)Execution Environments.
2.  Click Create execution environment and enter the relevant information in the fields that appear.   1.  The **Name** field displays the name of the execution environment on your local registry.
2.  The **Upstream name** field is the name of the image on the remote server.
3.  Under **Registry**, select the name of the registry from the drop-down menu.
4.  Optional: Enter tags in the **Add tag(s) to include** field. If the field is blank, all the tags are passed. You must specify which repository-specific tags to pass.
5.  Optional: Enter tags to exclude in the **Add tag(s) to exclude** field.
3.  Click Create execution environment. You should see your new execution environment in the list that appears.
4.  Sync and sign your new automation execution environment.   1.  Click the More Actions icon **⋮** and select **Sync execution environment**.
2.  Click the More Actions icon **⋮** and select **Sign execution environment**.
5.  Click on your new execution environment. On the Details page, find the **Signed** label to determine that your execution environment has been signed.

