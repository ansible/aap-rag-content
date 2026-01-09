# 2. Credentials
## 2.5. Deleting a credential




You can permanently delete unused credentials. You must first ensure they are detached from any event stream before the deletion process can be completed.

**Prerequisites**

1. Ensure that your credential is not currently linked to any rulebook activations.


**Procedure**

1. Delete the credential by using one of these methods:


- From the **Credentials** list view, click theMore Actionsicon **⋮** next to the desired credential and clickDelete credential.
- From the **Credentials** list view, select the name of the credential, click theMore Actionsicon **⋮** next toEdit credential, and clickDelete credential.

1. In the pop-up window, select **Yes, I confirm that I want to delete this credential** .

Note
If your credential is still in use by other resources in your organization, a warning message is displayed letting you know that the credential cannot be deleted. Also, if your credential is being used in an event stream, you cannot delete it until the event stream is deleted or attached to a different credential. In general, avoid deleting a credential that is in use because it can lead to broken activations.




1. ClickDelete credential.


**Results**

You can delete multiple credentials at a time by selecting the checkbox next to each credential, clicking theMore Actionsicon **⋮** in the menu bar, and then clickingDelete selected credentials.


