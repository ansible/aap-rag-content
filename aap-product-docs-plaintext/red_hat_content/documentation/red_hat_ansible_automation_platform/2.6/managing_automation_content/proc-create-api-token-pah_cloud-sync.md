# 1. Red Hat Certified, validated, and Ansible Galaxy content in automation hub
## 1.1. Configuring remote repositories for content syncing
### 1.1.3. Creating the API token in private automation hub

In private automation hub, you can create an API token using API token management. The API token is a secret token used to protect your content, so be sure to store it in a secure location.

Note

The API token does not expire.

**Prerequisites**

- Valid subscription credentials for Red Hat Ansible Automation Platform.

**Procedure**

1. Log in to your private automation hub.
2. From the navigation panel, select Automation Content → API token.
3. Click Load Token.
4. To copy the API token, click the Copy to clipboard icon.
5. Paste the API token into a file and store in a secure location.

**Next step**

The API token is now available for configuring automation hub as your default collections server or uploading collections using the `ansible-galaxy` command line tool.

