# Platform gateway

Platform gateway is the service that handles authentication and authorization for Ansible Automation Platform. It provides a single ingress into the Platform and serves the Platform’s user interface.

## About this task

From the Settings> (and then)Platform gateway menu, you can configure **Platform gateway**, **Security**, **Session**, **Platform Security**, **Custom Login**, and **Other** settings.

## Procedure

1.  From the navigation panel, select Settings> (and then)Platform gateway.
2.  The **Platform gateway settings** page is displayed.
3.  To configure the options, click Edit platform gateway settings.
4.  You can configure the following platform gateway options:

- **Platform gateway proxy url**: URL to the platform gateway proxy layer.
- **Platform gateway proxy url ignore cert**: Ignore the certificate to the platform gateway proxy layer.

5.  Click Save platform gateway settings to save the changes or proceed to configure the other platform options available.

## Configure platform security

From the **Platform gateway settings** page, you can configure platform security settings.

### Procedure

1.  From the navigation panel, select Settings> (and then)Platform gateway.
2.  The **Platform gateway settings** page is displayed.
3.  To configure the options, click Edit.
4.  You can configure the following **Security** settings:

- **Allow system administrators to set insecure user passwords**: Whether a superuser account can save an insecure password when editing any local user account.

- **Gateway basic auth enabled**: Enable basic authentication to the platform gateway API. Turning this off prevents all basic authentication (local users), so customers need to make sure they have their alternative authentication mechanisms correctly configured before doing so.

Turning it off with only local authentication configured also prevents all access to the UI.

**Gateway token name**: The header name to push from the proxy to the backend service.

- **Gateway access token expiration**: How long the access tokens are valid for.

- **Jwt private key**: The private key used to encrypt the JWT tokens sent to backend services. This should be a private RSA key and one should be generated automatically on installation.

Note:
Use caution when rotating the key as it will cause current sessions to fail until their JWT keys are reset.

- (Read only) **Jwt public key**: The private key used to encrypt the JWT tokens sent to backend services. This should be a private RSA key and one should be generated automatically on installation.

Note:
See other services' documentation on how they consume this key.

Warning:
If this name is changed, backends must be updated to compensate.

**Social auth username is full email**: Enabling this setting alerts social authentication to use the full email as username instead of the full name.

- **Csrf trusted origins**: If the service is behind a reverse proxy or load balancer, use this setting to configure the `schema://addresses` from which the service should trust Origin header values.

5.  Click Save changes to save the changes or proceed to configure the other platform options available.

## Configure platform sessions

From the **Platform gateway settings** page, you can configure platform session settings.

### Procedure

1.  From the navigation panel, select Settings> (and then)Platform gateway.
2.  The **Platform gateway settings** page is displayed.
3.  To configure the options, click Edit platform gateway settings.
4.  Enter the time in seconds before a session expires in the **Session cookie age** field.
5.  Click Save platform gateway settings to save the changes or proceed to configure the other platform options available.

## Configure a platform password security policy

From the **Platform gateway settings** page, you can configure a password security policy.

### Procedure

1.  From the navigation panel, select Settings> (and then)Platform gateway.
2.  The **Platform gateway settings** page is displayed.
3.  To configure the options, click Edit platform gateway settings.
4.  You can configure the following **Password Security** options:

- **Password minimum uppercase letters**: How many uppercase characters need to be in a local password.
- **Password minimum length**: The minimum length of a local password.
- **Password minimum numerical digits**: How many numerical characters need to be in a local password.
- **Password minimum special characters**: How many special characters need to be in a local password.

5.  Click Save platform gateway settings to save the changes or proceed to configure the other platform options available.

## Encrypt the platform gateway database password

System administrators can encrypt the database password used by platform gateway and apply it directly to the configuration file, resolving issues related to the `SECRET_KEY` loading order.

### About this task

Note:

Platform gateway uses the Django framework, which requires the `SECRET_KEY` to be fully loaded into memory before the decryption function (`ansible_encryption.decrypt_string()`) is called. If the decryption call runs before the key is loaded, the process fails, preventing platform gateway from accessing the database.

### Procedure

1.  Access the command line on the platform gateway node.
2.  Use the `aap-gateway-manage shell_plus` command to open an interactive Django shell:


```
aap-gateway-manage shell_plus
```

3.  Inside the shell, run the following commands to import the encryption library, set your password, and generate the encrypted string:


```
>>> from ansible_base.lib.utils.encryption import ansible_encryption
>>> value = 'your-database-password' # REPLACE with your actual password
>>> encrypted_value = ansible_encryption.encrypt_string(value)
>>> print(encrypted_value)
```

4.  Copy the entire output string starting with `$encrypted$`. This is your encrypted password.
5.  Exit the shell using `quit()`.
6.  Open the platform gateway configuration file for editing:


```
vi /etc/ansible-automation-platform/gateway/settings.py
```

7.  Locate the section defining the `DATABASES` variable. You must insert the code to load the `SECRET_KEY` before the `DATABASES` dictionary is defined.
8.  Update the file to include the highlighted code, replacing only the placeholder text for the `PASSWORD` key with your copied encrypted string:


```
from ansible_base.lib.utils.encryption import ansible_encryption
from django.conf import settings

# ... other configuration settings ...

# The GATEWAY_SECRET_KEY_FILE is typically defined earlier in settings.
# The SECRET_KEY must be loaded before the decryption function is called.
with open(GATEWAY_SECRET_KEY_FILE, 'rb') as f:
settings.SECRET_KEY = f.read().strip()

DATABASES = {
'default': {
'ENGINE': 'django.db.backends.postgresql',
'HOST': '10.0.108.77', # Example host, use your value
# ... other database settings ...
'PASSWORD':
ansible_encryption.decrypt_string('$encrypted$UTF8$AESCBC$Z0FBQUFBQnBBNU...
<YOUR_ENCRYPTED_STRING>...QWdPUHM9'),
# ... other database settings ...
'PORT': '5432', # Example port, use your value
}
}
```

9.  Save and close the file.
10.  Restart platform gateway to load the new encrypted configuration:


```
sudo systemctl restart aap-gateway
```

### Results

Confirm that platform gateway starts without errors and that you can access the platform UI, which indicates a successful database connection.

## Configure additional platform options

Configure extra settings in platform gateway, such as the JWT expiration buffer. Adjusting these options helps ensure continuous token validity and smooth communication between platform services.

### Procedure

1.  From the navigation panel, select Settings> (and then)Platform gateway.
2.  The **Platform gateway settings** page is displayed.
3.  Click Edit platform gateway settings.
4.  You can configure the following **Other settings**:

- **Jwt expiration buffer in seconds**: The number of seconds before a JWT token’s expiration to revoke from the cache. When authentication happens a JWT token is created for the user and that token is cached. When subsequent calls happen to services such as automation controller or Event-Driven Ansible, the token is taken from the cache and sent to the service. Both the token and the cache of the token have an expiration time. If the token expires while in the cache the authentication process attempts results in a 401 error (unauthorized). This setting gives Red Hat Ansible Automation Platform a buffer by removing the JWT token from the cache before the token expires. When a token is revoked from cache a new token with a new expiration is generated and cached for the user. As a result, expired tokens from the cache are never used. This setting defaults to 2 seconds. If you have a large latency between platform gateway and your services and observe 401 responses you must increase this setting to lower the number of 401 responses.

- **Status endpoint backend timeout seconds**: Timeout (in seconds) for the status endpoint to wait when trying to connect to a backend.

- **Status endpoint backend verify**: Specifies whether SSL/TLS certificates of the services are verified when calling individual nodes for statuses.

- **Resource client request timeout**: The timeout (in seconds) before the resource client will drop requests after forming connections.

- **Request timeout**: Specifies, in seconds, the length of time before the proxy will report a timeout and generate a 504.

- **Manage organization auth**: Controls whether any organization administrator has the privileges to create and manage users and teams. You might want to disable this ability if you are using an LDAP or SAML integration.  Important:
The `MANAGE_ORGANIZATION_AUTH` setting is moved to platform gateway during an upgrade from Ansible Automation Platform 2.4 to 2.6. However, the values are not automatically synchronized between platform gateway and automation controller after the migration. To prevent administrative issues, keep the `MANAGE_ORGANIZATION_AUTH` value consistent across both environments, especially if automation workflows run directly against automation controller.

- **Stream idle timeout**: Timeout in seconds for idle streaming connections, for example, for the Red Hat Ansible Lightspeed chatbot. Stream is closed if no data is transmitted within this period.

- **Max stream duration**: Maximum total duration in seconds for streaming connections, for example, for the Red Hat Ansible Lightspeed chatbot. Stream is closed after this time regardless of activity.

- **Aap deployment type**: The deployment type for this Ansible Automation Platform instance.

5.  Click Save platform gateway settings to save the changes or proceed to configure the other platform options available.

## Overlapping administrative settings

Manually synchronize duplicate operational and administrative settings between platform gateway and component services like automation controller. This helps ensure your workflows and scripts can interact directly with the component API without issues.

**Effective settings table**

The following table clarifies the authoritative source for administrative settings that you can configure in both automation controller and platform gateway.

| **Setting name (UI text)**                              | **API variable name**                  | **Platform gateway configuration location** | **Automation controller configuration location**         | **Synchronization requirement and notes**                                                                                                                                         |
| ------------------------------------------------------- | -------------------------------------- | ------------------------------------------- | -------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <br> **Organization Admins Can Manage Users and Teams** | <br> `MANAGE_ORGANIZATION_AUTH`        | <br>**Settings** > **Platform gateway**     | <br>**Settings** > **Automation Execution** > **System** | <br>Keep a consistent value across both systems. The automation controller setting might be used by direct API workflows.                                                         |
| <br> **All Users Visible to Organization Admins**       | <br> `ORG_ADMINS_CAN_SEE_ALL_USERS`    | <br>**Settings** > **Platform gateway**     | <br>**Settings** > **Automation Execution** > **System** | <br>Keep a consistent value across both systems. Automation controller does not follow gateway settings for this variable; direct API workflows use the controller’s local value. |
| <br> **Allow External Users to Create OAuth2 Tokens**   | <br> `ALLOW_OAUTH2_FOR_EXTERNAL_USERS` | <br>**Settings** > **Platform gateway**     | <br>N/A                                                  | <br>Platform gateway is authoritative. Configure this setting in the unified UI or through the gateway API.                                                                       |

## Configure system settings

Establish core automation controller operations by configuring proxy trusts, telemetry integration, default execution environments, and administrator permissions to ensure your platform integrates securely with your network infrastructure.

### Procedure

1.  Navigate to Settings> (and then)Automation Execution> (and then)System.
2.  Click Edit.
3.  Configure the necessary options to achieve your administrative goals:


Ensure services generate correct links
Define the Base URL of the service so external integrations (like notifications) can accurately point back to the controller.

Secure reverse proxy connections
If your controller sits behind a load balancer or reverse proxy, configure the Proxy IP allowed list to restrict which IPs are trusted for custom `REMOTE_HOST_HEADERS`.  Note:
Leaving this empty trusts these headers unconditionally.

Ensure accurate IP identification behind a proxy
Configure Remote Host Headers to specify which HTTP headers (e.g., `HTTP_X_FORWARDED_FOR`) the system uses to identify remote hostnames.  Important:
When you need to establish a hard directive for your infrastructure, define your settings within a server file (such as Python or YAML) or an environment variable. The platform treats these server-level files as the official source of truth. If you use this method, UI fields like **Remote Host Headers** become read-only to prevent interface changes from overriding your established configurations.

Synchronize with Red Hat services
Input your Red Hat Client ID and Client Secret for both Analytics and Subscriptions to enable telemetry, retrieve subscription data, and access content.

Establish a fallback runtime environment
Define a Global default execution environment to ensure jobs can run even if a specific job template lacks an assigned environment.

Utilize legacy Python environments
Specify Custom virtual environment paths (one per line) to instruct the controller where to find locally managed environments.

Manage telemetry reporting
Toggle Gather data for Automation Analytics to enable or disable telemetry. If enabled, control the reporting frequency using the Automation Analytics Gather Interval and verify the destination through the Automation Analytics upload URL.

Control managed node licensing
Define your subscription usage model to determine how hosts are counted. Choose whether to track historical unique nodes (allowing deletion of unused nodes) or operate with no subscription tracking for host metrics.

Maintain an audit trail
Toggle Enable Activity Stream and Enable Activity Stream for Inventory Sync to capture detailed logs of system changes and inventory updates.

Delegate or restrict administrator permissions
Use All Users Visible to Organization Admins and Organization Admins Can Manage Users and Teams to dictate cross-organization visibility and user creation rights.  Tip:
Disable the management toggle if your users are centrally managed using LDAP.

4.  Click Save to apply your configurations.

## Configure jobs

You can use the **Job** option to define the operation of Jobs in automation controller.

### Procedure

1.  Navigate to Settings> (and then)Automation execution> (and then)Job
2.  On the **Job settings** page, Click Edit


*Figure 1. Job settings page*
![Job settings page](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/job-settings-full.png)

3.  You can configure the following options:

- **Ansible Modules Allowed For Ad Hoc Jobs**: List of modules you can use for ad hoc jobs.

- **When can extra variables contain Jinja templates?**: Ansible allows variable substitution through the Jinja2 templating language for `--extra-vars`. This poses a potential security risk where users with the ability to specify extra vars at job launch time can use Jinja2 templates to run arbitrary Python.

Set this value to either `template` or `never`.

- **Paths to expose to isolated jobs**: List of paths that would otherwise be hidden to expose to isolated jobs. Enter one path per line. If a path to a specific file is entered, then the entire directory containing that file will be mounted inside the execution environment.

Volumes are mounted from the execution node to the container.

The supported format is `HOST-DIR[:CONTAINER-DIR[:OPTIONS]]`.

- **Extra Environment Variables**: Additional environment variables set for playbook runs, inventory updates, project updates, and notification sending.

- **K8S Ansible Runner Keep-Alive Message Interval**: Only applies to jobs running in a Container Group. If not 0, send a message every specified number of seconds to keep the connection open.

- **Environment Variables for Galaxy Commands**: Additional environment variables set for invocations of ansible-galaxy within project updates. Useful if you must use a proxy server for ansible-galaxy but not git.

- **Standard Output Maximum Display Size**: Maximum Size of Standard Output in bytes to display before requiring the output be downloaded.

- **Job Event Standard Output Maximum Display Size**: Maximum Size of Standard Output in bytes to display for a single job or ad hoc command event. stdout ends with `…` when truncated.

- **Job Event Maximum Websocket Messages Per Second**: The maximum number of messages to update the UI live job output with per second. A value of 0 means no limit.

- **Maximum Scheduled Jobs**: Maximum number of the same job template that can be waiting to run when launching from a schedule before no more are created.

- **Ansible Callback Plugins**: List of paths to search for extra callback plugins to be used when running jobs.

- **Default Job Timeout**: If no output is detected from ansible in this number of seconds the execution will be terminated. Use a value of 0 to indicate that no idle timeout should be imposed.

Enter one path per line.

- **Default Inventory Update Timeout**: Maximum time in seconds to allow inventory updates to run. Use a value of 0 to indicate that no timeout should be imposed.

A timeout set on an individual inventory source will override this.

- **Default Project Update Timeout**: Maximum time in seconds to allow project updates to run. Use a value of 0 to indicate that no timeout should be imposed.

A timeout set on an individual project will override this.

- **Per-Host Ansible Fact Cache Timeout**: Maximum time, in seconds, that stored Ansible facts are considered valid since the last time they were modified. Only valid, non-stale, facts are accessible by a playbook.

This does not influence the deletion of `ansible_facts` from the database.

Use a value of 0 to indicate that no timeout should be imposed.

- **Maximum number of forks per job**: Saving a Job Template with more than this number of forks results in an error. When set to 0, no limit is applied.

- **Job execution path**: Only available in operator-based installations.

- **Container Run Options**: Only available in operator-based installations. List of options to pass to Podman run example: `['--network', 'slirp4netns:enable_ipv6=true', '--log-level', 'debug']`.



You can set the following options:

- **Run Project Updates With Higher Verbosity**: Select this to add the CLI `-vvv` flag to playbook runs of `project_update.yml` used for project updates.

- **Enable Role Download**: Select this to allow roles to be dynamically downloaded from a `requirements.yml` file for SCM projects.

- **Enable Collection(s) Download**: Select this to allow collections to be dynamically downloaded from a `requirements.yml` file for SCM projects.

- **Follow symlinks**: Select to follow symbolic links when scanning for playbooks. Be aware that setting this to `True` can lead to infinite recursion if a link points to a parent directory of itself.

- **Expose host paths for Container Groups**: Select this to expose paths through hostPath for the Pods created by a Container Group.  Note:
HostPath volumes present many security risks, and it is best practice to avoid the use of HostPaths when possible.

- **Ignore Ansible Galaxy SSL Certificate Verification**: If set to `true`, certificate validation is not done when installing content from any Galaxy server. Click the tooltip ![Questioncircle](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Configuring_automation_execution-en-US/images/0c17081b1d1293156a760e9a6e06634a/question_circle.png) icon next to the field that you need additional information about.

Note:
The values for all timeouts are in seconds.

4.  Click Save to apply the settings.
