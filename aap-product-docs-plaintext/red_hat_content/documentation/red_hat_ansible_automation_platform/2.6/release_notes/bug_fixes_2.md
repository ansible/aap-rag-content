# 9. Patch releases
## 9.2. Ansible Automation Platform patch release March 25, 2026
### 9.2.6. Bug fixes

#### 9.2.6.1. Ansible Automation Platform

- Fixed an issue where the “Organization Admins Can Manage Users and Teams” setting did not correctly disable the create-team button in the UI when turned off, so organization admins now see the correct state. AAP-68843
- Fixed an issue where organization administrators were still able to delete or modify teams when “Organization Admins Can Manage Users and Teams” was disabled, so this setting now enforces the intended restrictions. AAP-68842
- Fixed an issue where teams from other organizations were not visible to organization administrators as expected when organization-wide visibility was enabled. AAP-68841
- Fixed an issue where an organization administrator could not assign team access to projects in Ansible Automation Platform 2.6, preventing proper delegation of permissions. AAP-65081
- Fixed an issue where list views in the gateway UI loaded slowly because of excessive duplicate API requests and aggressive polling intervals, improving responsiveness. AAP-67460
- Fixed an issue where redirects using the `next` URL parameter failed when the value included a plus sign (`+`), whether encoded or unencoded, so redirects now work correctly. AAP-64996
- Fixed an issue where creating Event-Driven Ansible projects concurrently from multiple users could result in server errors when handling project creation. AAP-67749
- Fixed an issue where general project creation flows in Django Ansible Base could lead to errors when invoked by multiple users, improving stability. AAP-60238

#### 9.2.6.2. Container-based installer Ansible Automation Platform

- Fixed an issue where containerized controller installs could fail after the Django 5.2 upgrade because Django output changed and broke parsing in the installer. AAP-68135
- Fixed an issue where Podman’s `pids_limit` could be set to an extremely large value on nodes with large memory, exceeding system-supported limits, by capping the value. AAP-67579

#### 9.2.6.3. Automation controller

- Fixed an issue where facts could become inconsistent when running job templates with fact storage enabled, particularly when multiple inventories had same-name hosts or concurrent jobs updated facts. AAP-67371
- Fixed an issue where constructed inventories could not be saved when verbosity was greater than 2, so higher verbosity levels are now supported. AAP-66864
- Fixed an issue where job events missing an event type caused uncaught exceptions in the job events children summary view, improving reliability. AAP-64630

#### 9.2.6.4. Event-Driven Ansible

- Fixed an issue where Decision Environment credential validation rejected container registry credentials when the password came from an external credential provider unless placeholder text was used, allowing those credentials to be attached without workarounds. AAP-69005
- Fixed an issue where Jinja2 variable substitution in rule names failed in Event-Driven Ansible controller worker mode even though the same variables worked in action `extra_vars`, aligning behavior with the CLI. AAP-67038
- Fixed an issue where Event-Driven Ansible server could not sync git projects using `ssh:// or git+ssh://` URL schemes, restoring project sync behavior. AAP-66353

#### 9.2.6.5. Automation execution environment

- Fixed an issue where a change in the `certifi` package affected default trust store paths in Ansible Automation Platform 2.6 execution environments by switching to `system-certifi` to restore expected behavior. AAP-58769

#### 9.2.6.6. Automation hub

- Fixed an issue where the X-Forwarded-Proto header could be incorrectly set in conjunction with the `alter_hostname_settings` configuration on Azure when passing traffic from gateway to Automation hub. AAP-66706

#### 9.2.6.7. Red Hat Ansible Lightspeed

- Fixed an issue where OAuth2 authentication on containerized installer deployments could fail when the Red Hat Ansible Lightspeed port was set to 443 because of incorrect URL handling and default port logic. AAP-66845
- Fixed an issue where the platform configuration MCP server exposed the `settings_list` tool twice, causing API errors in clients, by renaming the tools to `controller-settings_list` and `gateway-settings_list`. AAP-66400
- Fixed an issue where the /check endpoint of the Ansible Red Hat Ansible Lightspeed API container reported an incorrect commit version and SHA, improving diagnostics. AAP-60313

#### 9.2.6.8. Ansible Automation Platform Operator

- Fixed an issue where deleting a restored Ansible Automation Platform object did not delete the associated deployment or pods, leaving orphaned resources. AAP-68079
- Fixed an issue where IRSA-based S3 authentication support from galaxy-operator was not available in Automation hub operator for stable-2.6, allowing S3 access-key fields to be optional. AAP-67498
- Fixed an issue where Galaxy operator restores with `force_drop_db` failed due to missing CREATEDB privileges and partitioned index handling, causing `pg_restore` to fail during restores. AAP-67081
- Fixed an issue where EDA operator restores with `force_drop_db` failed because the managed PostgreSQL user lacked permissions to recreate databases, causing failures on restore. AAP-67080
- Fixed an issue where gateway operator restores with `force_drop_db` failed because required privileges were missing and partitioned indexes caused errors during `pg_restore`. AAP-67079
- Fixed an issue where AWX operator restores with `force_drop_db` were ignored, preventing databases from being dropped and recreated as expected. AAP-67078

#### 9.2.6.9. Receptor

- Fixed an issue where receptor reported “Error locating unit” when running in controller because cancelled work units were deleted prematurely across restarts. AAP-22149

