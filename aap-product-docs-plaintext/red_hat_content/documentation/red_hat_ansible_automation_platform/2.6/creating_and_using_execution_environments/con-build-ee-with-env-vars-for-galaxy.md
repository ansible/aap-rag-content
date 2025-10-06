# 3. Using Ansible Builder
## 3.9. Additional custom build steps
### 3.9.2. Building execution environments with environment variables for Galaxy configuration




Ansible Builder schema 3 enables you to perform complex scenarios such as specifying custom Galaxy configurations. You can use this approach to pass sensitive information, such as authentication tokens, into the execution environment build without leaking them into the final execution environment image.

The following example uses Ansible Galaxy Server environment variables.

```
additional_build_steps:
prepend_galaxy:
# Environment variables used for Galaxy client configurations
- ENV ANSIBLE_GALAXY_SERVER_LIST=automation_hub
- ENV ANSIBLE_GALAXY_SERVER_AUTOMATION_HUB_URL=https://console.redhat.com/api/automation-hub/content/xxxxxxx-synclist/
- ENV ANSIBLE_GALAXY_SERVER_AUTOMATION_HUB_AUTH_URL=https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token
# define a custom build arg env passthru - we still also have to pass
# `--build-arg ANSIBLE_GALAXY_SERVER_AUTOMATION_HUB_TOKEN` to get it to pick it up from the env
- ARG ANSIBLE_GALAXY_SERVER_AUTOMATION_HUB_TOKEN

options:
package_manager_path: /usr/bin/microdnf  # downstream images use non-standard package manager
```

You can provide environment variables such as `ANSIBLE_GALAXY_SERVER_LIST` , `ANSIBLE_GALAXY_SERVER_AUTOMATION_HUB_URL` and `ANSIBLE_GALAXY_SERVER_AUTOMATION_HUB_AUTH_URL` using the `ENV` directive. For more information, see the [Galaxy User Guide](https://docs.ansible.com/ansible/latest/galaxy/user_guide.html#configuring-the-ansible-galaxy-client) in the Ansible documentation.

For security reasons, you must not store sensitive information in `ANSIBLE_GALAXY_SERVER_AUTOMATION_HUB_TOKEN` . You can use the ARG directive to receive sensitive information from the user as input.

`–build-args` can be used to provide this information while invoking the ansible-builder command.

