# 3. Common automation execution environment scenarios
## 3.2. Using automation hub authentication details when building automation execution environments




Use the following example to customize the default definition file to pass automation hub authentication details into the automation execution environment build without exposing them in the final automation execution environment image.

**Prerequisites**

- You have created an API token, as in [Retrieving the API token for your Red Hat Certified Collection](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/managing_automation_content/managing-cert-valid-content#proc-create-api-token) and stored it in a secure location, for example in a file named `    token.txt` .
- Define a build argument that gets populated with the automation hub API token:


```
export ANSIBLE_GALAXY_SERVER_AUTOMATION_HUB_TOKEN=$(cat &lt;token.txt&gt;)
```

```
additional_build_steps:
prepend_galaxy:
# define a custom build arg env passthru- we still also have to pass
# `--build-arg ANSIBLE_GALAXY_SERVER_AUTOMATION_HUB_TOKEN` to get it to pick it up from the host env
- ARG ANSIBLE_GALAXY_SERVER_AUTOMATION_HUB_TOKEN
- ENV ANSIBLE_GALAXY_SERVER_LIST=automation_hub
- ENV ANSIBLE_GALAXY_SERVER_AUTOMATION_HUB_URL=https://console.redhat.com/api/automation-hub/content/&lt;yourhuburl&gt;-synclist/
- ENV ANSIBLE_GALAXY_SERVER_AUTOMATION_HUB_AUTH_URL=https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token
```

**Additional resources**

-  [Breakdown of definition file content](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/creating_and_using_execution_environments/index#con-definition-file-breakdown)


