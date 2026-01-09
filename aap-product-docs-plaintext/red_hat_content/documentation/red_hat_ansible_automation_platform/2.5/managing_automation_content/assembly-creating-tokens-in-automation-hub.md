# 1. Red Hat Certified, validated, and Ansible Galaxy content in automation hub
## 1.1. Configuring remote repositories for content syncing




Use remote configurations to configure your private automation hub to synchronize with Ansible Certified Content Collections hosted on `console.redhat.com` or with your collections in Ansible Galaxy.

Each remote configuration inAutomation Content→Remotesprovides information for both the **community** and **rh-certified** repository about when the repository was **last updated** . You can add new content to Ansible automation hub at any time by using the **Edit** and **Sync** features included on theAutomation Content→Repositoriespage.

**Understanding the difference between Ansible Galaxy and Ansible automation hub collections**

Collections published to Ansible Galaxy are the latest content published by the Ansible community and have no joint support claims associated with them. Ansible Galaxy is the recommended front end directory for the Ansible community to access content.

Collections published to Ansible automation hub are targeted to joint customers of Red Hat and selected partners. Customers need an Ansible subscription to access and download collections on Ansible automation hub. A certified collection means that Red Hat and partners have a strategic relationship in place and are ready to support joint customers. Collections might also have had additional testing and validation done against them.

**Requesting a namespace on Ansible Galaxy**

To request a namespace through an Ansible Galaxy GitHub issue, send an email request to [ansiblepartners@redhat.com](mailto:ansiblepartners@redhat.com) that includes the GitHub username used to sign up on Ansible Galaxy.

You must have logged in at least once for the system to validate.

After users are added as administrators of the namespace, you can use the self-serve process to add more administrators.

**Ansible Galaxy namespace naming guidelines**

Collection namespaces must follow Python module name convention. This means collections should have short, all lowercase names. You can use underscores in the collection name if it improves readability.

