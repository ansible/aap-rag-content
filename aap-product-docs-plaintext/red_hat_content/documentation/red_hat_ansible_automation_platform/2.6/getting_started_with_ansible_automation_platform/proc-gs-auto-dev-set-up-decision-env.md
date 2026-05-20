# 3. Getting started as an automation developer
## 3.9. Build and use a decision environment
### 3.9.1. Setting up a new decision environment

The following steps describe how to import a decision environment into the platform.

**Prerequisites**

- You have set up any necessary credentials. For more information, see the [Setting up credentials](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/using_automation_decisions/eda-credentials#eda-set-up-credential) section of the Using automation decisions guide.
- You have pushed a decision environment image to an image repository or you chose to use the image `de-supported` provided at [registry.redhat.io](http://registry.redhat.io/).

**Procedure**

1. Navigate to Automation Decisions → Decision Environments.

2. Click Create decision environment.

3. Enter the following:



Name
Insert the name.

Description
This field is optional.

Image
This is the full image location, including the container registry, image name, and version tag.

Credential
This field is optional. This is the token needed to use the decision environment image.

4. Select Create decision environment.

Your decision environment is now created and can be managed on the **Decision Environments** page.

**Verification**

After saving the new decision environment, the decision environment’s details page is displayed. From there or the **Decision Environments** list view, you can edit or delete it.

