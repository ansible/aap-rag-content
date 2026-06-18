+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-assembly_settings_navigator"
title = "Automation content navigator command reference - Red Hat Ansible Automation Platform 2.6"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/develop-assembly_intro_navigator/", "Emulate a platform environment locally with automation content navigator"]]
category = "Develop"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/develop-assembly_settings_navigator/aem-page/develop-assembly_settings_navigator.html"
last_crumb = "Automation content navigator command reference"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Automation content navigator command reference"
oversized = "false"
page_slug = "develop-assembly_settings_navigator"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/develop-assembly_settings_navigator"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/develop-assembly_settings_navigator/toc/toc.json"
type = "aem-page"
+++

# Automation content navigator command reference

Configure automation content navigator settings to customize the tool for your specific development environment needs. This helps you optimize your workflow for efficiency.

## Create an automation content navigator settings file

Alter default automation content navigator settings using the command line, environment variables, or a dedicated settings file. Using a settings file helps ensure consistent configuration across sessions.

Automation content navigator checks for a settings file in the following order and uses the first match:

- `ANSIBLE_NAVIGATOR_CONFIG` - The settings file path environment variable if set.
- `./ansible-navigator.<ext>` - The settings file within the current project directory, with no dot in the file name.
- `\~/.ansible-navigator.<ext>` - Your home directory, with a dot in the file name.


Consider the following when you create an automation content navigator settings file:

- The settings file can be in `JSON` or `YAML` format.
- For settings in `JSON` format, the extension must be `.json`.
- For settings in `YAML` format, the extension must be `.yml` or `.yaml`.
- The project and home directories can only contain one settings file each.
- If automation content navigator finds more than one settings file in either directory, it results in an error.


You can copy the example settings file below into one of those paths to start your `ansible-navigator` settings file.

```yaml
---
ansible-navigator:
#   ansible:
#     config: /tmp/ansible.cfg
#     cmdline: "--forks 15"
#     inventories:
#     - /tmp/test_inventory.yml
#     playbook: /tmp/test_playbook.yml
#   ansible-runner:
#     artifact-dir: /tmp/test1
#     rotate-artifacts-count: 10
#     timeout: 300
#   app: run
#   collection-doc-cache-path: /tmp/cache.db
#   color:
#     enable: False
#     osc4: False
#   editor:
#     command: vim_from_setting
#     console: False
#   documentation:
#     plugin:
#       name: shell
#       type: become
#   execution-environment:
#     container-engine: podman
#     enabled: False
#     environment-variables:
#       pass:
#         - ONE
#         - TWO
#         - THREE
#       set:
#         KEY1: VALUE1
#         KEY2: VALUE2
#         KEY3: VALUE3
#     image: test_image:latest
#     pull-policy: never
#     volume-mounts:
#     - src: "/test1"
#       dest: "/test1"
#       label: "Z"
#   help-config: True
#   help-doc: True
#   help-inventory: True
#   help-playbook: False
#   inventory-columns:
#     - ansible_network_os
#     - ansible_network_cli_ssh_type
#     - ansible_connection
  logging:
#     append: False
    level: critical
#     file: /tmp/log.txt
#   mode: stdout
#   playbook-artifact:
#     enable: True
#     replay: /tmp/test_artifact.json
#     save-as: /tmp/test_artifact.json
```

## Automation content navigator general settings

The following table describes each general parameter and setting options for automation content navigator.

*Table 1. Automation content navigator general parameters settings*

| Parameter                                 | Description                                                                                                                                                                                                                                                  | Setting options                                                                                                                                                                                                                                                                        |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <br>ansible-runner-artifact-dir           | <br>The directory path to store artifacts generated by ansible-runner.                                                                                                                                                                                       | <br>**Default:** No default value set<br>**CLI:**`--rad` or `--ansible-runner-artifact-dir`<br> **ENV:** `ANSIBLE_NAVIGATOR_ANSIBLE_RUNNER_ARTIFACT_DIR`<br> **Settings file:**    ```yaml ansible-navigator:   ansible-runner:     artifact-dir: ```                                  |
| <br>ansible-runner-rotate-artifacts-count | <br>Keep ansible-runner artifact directories, for last n runs. If set to 0, artifact directories are not deleted.                                                                                                                                            | <br>**Default:** No default value set<br>**CLI:**`--rac` or `--ansible-runner-rotate-artifacts-count`<br> **ENV:** `ANSIBLE_NAVIGATOR_ANSIBLE_RUNNER_ROTATE_ARTIFACTS_COUNT`<br> **Settings file:**    ```yaml ansible-navigator:   ansible-runner:     rotate-artifacts-count: ```    |
| <br>ansible-runner-timeout                | <br>The timeout value after which `ansible-runner` force stops the execution.                                                                                                                                                                                | <br>**Default:** No default value set<br>**CLI:**`--rt` or `--ansible-runner-timeout`<br> **ENV:** `ANSIBLE_NAVIGATOR_ANSIBLE_RUNNER_TIMEOUT`<br> **Settings file:**    ```yaml ansible-navigator:   ansible-runner:     timeout: ```                                                  |
| <br>app                                   | <br>Entry point for automation content navigator.                                                                                                                                                                                                            | <br>**Choices**: `collections`, `config`, `doc`, `images`, `inventory`, `replay`, `run` or `welcome`<br>**Default**: `welcome`<br>**CLI example**: `ansible-navigator collections`<br>**ENV**: `ANSIBLE_NAVIGATOR_APP`<br> **Settings file:**    ```yaml ansible-navigator:   app: ``` |
| <br>cmdline                               | <br>Extra parameters passed to the corresponding command.                                                                                                                                                                                                    | <br>**Default**: No default value<br>**CLI**: positional<br>**ENV**: `ANSIBLE_NAVIGATOR_CMDLINE`<br> **Settings file:**    ```yaml ansible-navigator:   ansible:     cmdline: ```                                                                                                      |
| <br>collection-doc-cache-path             | <br>The path to the collection doc cache.                                                                                                                                                                                                                    | <br>**Default**: `$HOME/.cache/ansible-navigator/collection_doc_cache.db`<br>**CLI**: `--cdcp` or `--collection-doc-cache-path`<br>**ENV**: `ANSIBLE_NAVIGATOR_COLLECTION_DOC_CACHE_PATH`<br> **Settings file:**    ```yaml ansible-navigator:   collection-doc-cache-path: ```        |
| <br>container-engine                      | <br>Specify the container engine (`auto`=`podman` then `docker`).                                                                                                                                                                                            | <br>**Choices:**`auto`, `podman` or `docker`<br> **Default:** `auto`<br>**CLI:**`--ce` or `--container-engine`<br> **ENV:** `ANSIBLE_NAVIGATOR_CONTAINER_ENGINE`<br> **Settings file:**    ```yaml ansible-navigator:   execution-environment:     container-engine: ```               |
| <br>display-color                         | <br>Enable the use of color in the display.                                                                                                                                                                                                                  | <br>**Choices:**`True` or `False`<br> **Default:** `True`<br>**CLI:**`--dc` or `--display-color`<br> **ENV:** `NO_COLOR`<br> **Settings file:**    ```yaml ansible-navigator:   color:     enable: ```                                                                                 |
| <br>editor-command                        | <br>Specify the editor used by automation content navigator                                                                                                                                                                                                  | <br>Default:\* vi +{line\_number} {filename}<br>**CLI:**`--ecmd` or `--editor-command`<br> **ENV:** `ANSIBLE_NAVIGATOR_EDITOR_COMMAND`<br> **Settings file:**    ```yaml ansible-navigator:   editor:     command: ```                                                                 |
| <br>editor-console                        | <br>Specify if the editor is console based.                                                                                                                                                                                                                  | <br>**Choices:**`True` or `False`<br> **Default:** `True`<br>**CLI:**`--econ` or `--editor-console`<br> **ENV:** `ANSIBLE_NAVIGATOR_EDITOR_CONSOLE`<br> **Settings file:**    ```yaml ansible-navigator:   editor:     console: ```                                                    |
| <br>execution-environment                 | <br>Enable or disable the use of an automation execution environment.                                                                                                                                                                                        | <br>**Choices:**`True` or `False`<br> **Default:** `True`<br>**CLI:**`--ee` or `--execution-environment`<br>**ENV:**\* `ANSIBLE_NAVIGATOR_EXECUTION_ENVIRONMENT`<br> **Settings file:**    ```yaml ansible-navigator:   execution-environment:     enabled: ```                        |
| <br>execution-environment-image           | <br>Specify the name of the automation execution environment image.                                                                                                                                                                                          | <br> **Default:** `quay.io/ansible/ansible-runner:devel`<br>**CLI:**`--eei` or `--execution-environment-image`<br> **ENV:** `ANSIBLE_NAVIGATOR_EXECUTION_ENVIRONMENT_IMAGE`<br> **Settings file:**    ```yaml ansible-navigator:   execution-environment:     image: ```               |
| <br>execution-environment-volume-mounts   | <br>Specify volume to be bind mounted within an automation execution environment (`--eev /home/user/test:/home/user/test:Z`)                                                                                                                                 | <br>**Default:** No default value set<br>**CLI:**`--eev` or `--execution-environment-volume-mounts`<br> **ENV:** `ANSIBLE_NAVIGATOR_EXECUTION_ENVIRONMENT_VOLUME_MOUNTS`<br> **Settings file:**    ```yaml ansible-navigator:   execution-environment:     volume-mounts: ```          |
| <br>log-append                            | <br>Specify if log messages should be appended to an existing log file, otherwise a new log file is created per session.                                                                                                                                     | <br>**Choices:**`True` or `False`<br>**Default:** True<br>**CLI:**`--la` or `--log-append`<br> **ENV:** `ANSIBLE_NAVIGATOR_LOG_APPEND`<br> **Settings file:**    ```yaml ansible-navigator:   logging:     append: ```                                                                 |
| <br>log-file                              | <br>Specify the full path for the automation content navigator log file.                                                                                                                                                                                     | <br> **Default:** `$PWD/ansible-navigator.log`<br>**CLI:**`--lf` or `--log-file`<br> **ENV:** `ANSIBLE_NAVIGATOR_LOG_FILE`<br> **Settings file:**    ```yaml ansible-navigator:   logging:     file: ```                                                                               |
| <br>log-level                             | <br>Specify the automation content navigator log level.                                                                                                                                                                                                      | <br>**Choices:**`debug`, `info`, `warning`, `error` or `critical`<br> **Default:** `warning`<br>**CLI:**`--ll` or `--log-level`<br> **ENV:** `ANSIBLE_NAVIGATOR_LOG_LEVEL`<br> **Settings file:**    ```yaml ansible-navigator:   logging:     level: ```                              |
| <br>mode                                  | <br>Specify the user-interface mode.                                                                                                                                                                                                                         | <br>**Choices:**`stdout` or `interactive`<br> **Default:** `interactive`<br>**CLI:**`-m` or `--mode`<br> **ENV:** `ANSIBLE_NAVIGATOR_MODE`<br> **Settings file:**    ```yaml ansible-navigator:   mode: ```                                                                            |
| <br>osc4                                  | <br>Enable or disable terminal color changing support with OSC 4.                                                                                                                                                                                            | <br>**Choices:**`True` or `False`<br> **Default:** `True`<br>**CLI:**`--osc4` or `--osc4`<br> **ENV:** `ANSIBLE_NAVIGATOR_OSC4`<br> **Settings file:**    ```yaml ansible-navigator:   color:     osc4: ```                                                                            |
| <br>pass-environment-variable             | <br>Specify an exiting environment variable to be passed through to and set within the automation execution environment (`--penv MY_VAR`)                                                                                                                    | <br>**Default:** No default value set<br>**CLI:**`--penv` or `--pass-environment-variable`<br> **ENV:** `ANSIBLE_NAVIGATOR_PASS_ENVIRONMENT_VARIABLES`<br> **Settings file:**    ```yaml ansible-navigator:   execution-environment:     environment-variables:       pass: ```        |
| <br>pull-policy                           | <br>Specify the image pull policy.<br>`always` - Always pull the image<br>`missing` - Pull if not locally available<br>`never` - Never pull the image<br>`tag` - If the image tag is `latest` always pull the image, otherwise pull if not locally available | <br>**Choices:**`always`, `missing`, `never`, or `tag`<br> **Default:** `tag`<br>**CLI:**`--pp` or `--pull-policy`<br> **ENV:** `ANSIBLE_NAVIGATOR_PULL_POLICY`<br> **Settings file:**    ```yaml ansible-navigator:   execution-environment:     pull-policy: ```                     |
| <br>set-environment-variable              | <br>Specify an environment variable and a value to be set within the automation execution environment `(--senv MY_VAR=42`)                                                                                                                                   | <br>**Default:** No default value set<br>**CLI:**`--senv` or `--set-environment-variable`<br> **ENV:** `ANSIBLE_NAVIGATOR_SET_ENVIRONMENT_VARIABLES`<br> **Settings file:**    ```yaml ansible-navigator:   execution-environment:     environment-variables:       set: ```           |

## Automation content navigator `config` subcommand settings

The following table describes each parameter and setting options for the automation content navigator `config` subcommand.

*Table 2. Automation content navigator `config` subcommand parameters settings*

| Parameter       | Description                                                         | Setting options                                                                                                                                                                                                         |
| --------------- | ------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <br>config      | <br>Specify the path to the Ansible configuration file.             | <br>**Default:** No default value set<br>**CLI:**`-c` or `--config`<br> **ENV:** `ANSIBLE_CONFIG`<br> **Settings file:**    ```yaml ansible-navigator:   ansible:     config:       path: ```                           |
| <br>help-config | <br>Help options for the `ansible-config` command in `stdout` mode. | <br>**Choices:**\* `True` or `False`<br> **Default:** `False`<br>**CLI:**`--hc` or `--help-config`<br> **ENV:** `ANSIBLE_NAVIGATOR_HELP_CONFIG`<br> **Settings file:**    ```yaml ansible-navigator:   help-config: ``` |

## automation content navigator `doc` subcommand settings

The following table describes each parameter and setting options for the automation content navigator `doc` subcommand.

*Table 3. automation content navigator `doc` subcommand parameters settings*

| Parameter       | Description                                                      | Setting options                                                                                                                                                                                                                                                                                                                                                      |
| --------------- | ---------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <br>help-doc    | <br>Help options for the `ansible-doc` command in `stdout` mode. | <br>**Choices:**`True` or `False`<br> **Default:** `False`<br>**CLI:**`--hd` or `--help-doc`<br> **ENV:** `ANSIBLE_NAVIGATOR_HELP_DOC`<br> **Settings file:**    ```yaml ansible-navigator:   help-doc: ```                                                                                                                                                          |
| <br>plugin-name | <br>Specify the plugin name.                                     | <br>**Default:** No default value set<br>**CLI:** positional<br> **ENV:** `ANSIBLE_NAVIGATOR_PLUGIN_NAME`<br> **Settings file:**    ```yaml ansible-navigator:   documentation:     plugin:       name: ```                                                                                                                                                          |
| <br>plugin-type | <br>Specify the plugin type.                                     | <br>**Choices:**`become`, `cache`, `callback`, `cliconf`, `connection`, `httpapi`, `inventory`, `lookup`, `module`, `netconf`, `shell`, `strategy`, or `vars`<br> **Default:** `module`<br>**CLI:**`-t` or `----type`<br> **ENV:** `ANSIBLE_NAVIGATOR_PLUGIN_TYPE`<br> **Settings file:**    ```yaml ansible-navigator:   documentation:     plugin:       type: ``` |

## Automation content navigator `inventory` subcommand settings

The following table describes each parameter and setting options for the automation content navigator `inventory` subcommand.

*Table 4. Automation content navigator `inventory` subcommand parameters settings*

| Parameter            | Description                                                            | Setting options                                                                                                                                                                                                              |
| -------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <br>help-inventory   | <br>Help options for the `ansible-inventory` command in `stdout` mode. | <br>**Choices:**`True` or `False`<br> **Default:** `False`<br>**CLI:**`--hi` or `--help-inventory`<br> **ENV:** `ANSIBLE_NAVIGATOR_INVENTORY_DOC`<br> **Settings file:**    ```yaml ansible-navigator:   help-inventory: ``` |
| <br>inventory        | <br>Specify an inventory file path or comma separated host list.       | <br>**Default:** no default value set<br>**CLI:**`--i` or `--inventory`<br> **ENV:** `ANSIBLE_NAVIGATOR_INVENTORIES`<br> **Settings file:**    ```yaml ansible-navigator:   inventories: ```                                 |
| <br>inventory-column | <br>Specify a host attribute to show in the inventory view.            | <br>**Default:** No default value set<br>**CLI:**`--ic` or `--inventory-column`<br>**ENV:**\* `ANSIBLE_NAVIGATOR_INVENTORY_COLUMNS`**Settings file:**   ```yaml ansible-navigator:   inventory-columns: ```                  |

## Automation content navigator `replay` subcommand settings

The following table describes each parameter and setting options for the automation content navigator `replay` subcommand.

*Table 5. Automation content navigator `replay` subcommand parameters settings*

| Parameter                    | Description                                               | Setting options                                                                                                                                                                                                  |
| ---------------------------- | --------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <br>playbook-artifact-replay | <br>Specify the path for the playbook artifact to replay. | <br>**Default:** No default value set<br>**CLI:** positional<br> **ENV:** `ANSIBLE_NAVIGATOR_PLAYBOOK_ARTIFACT_REPLAY`<br> **Settings file:**    ```yaml ansible-navigator:   playbook-artifact:     replay: ``` |

## Automation content navigator `run` subcommand settings

The following table describes each parameter and setting options for the automation content navigator `run` subcommand.

*Table 6. Automation content navigator `run` subcommand parameters settings*

| Parameter                     | Description                                                                                                                                           | Setting options                                                                                                                                                                                                                                                                     |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <br>playbook-artifact-replay  | <br>Specify the path for the playbook artifact to replay.                                                                                             | <br>**Default:** No default value set<br>**CLI:** positional<br> **ENV:** `ANSIBLE_NAVIGATOR_PLAYBOOK_ARTIFACT_REPLAY`<br> **Settings file:**    ```yaml ansible-navigator:   playbook-artifact:     replay: ```                                                                    |
| <br>help-playbook             | <br>Help options for the `ansible-playbook` command in `stdout` mode.                                                                                 | <br>**Choices:**`True` or `False`<br> **Default:** `False`<br>**CLI:**`--hp` or `--help-playbook`<br> **ENV:** `ANSIBLE_NAVIGATOR_HELP_PLAYBOOK`<br> **Settings file:**    ```yaml ansible-navigator:   help-playbook: ```                                                          |
| <br>inventory                 | <br>Specify an inventory file path or comma separated host list.                                                                                      | <br>**Default:** no default value set<br>**CLI:**`--i` or `--inventory`<br> **ENV:** `ANSIBLE_NAVIGATOR_INVENTORIES`<br> **Settings file:**    ```yaml ansible-navigator:   inventories: ```                                                                                        |
| <br>inventory-column          | <br>Specify a host attribute to show in the inventory view.                                                                                           | <br>**Default:** No default value set<br>**CLI:**`--ic` or `--inventory-column`<br>**ENV:**\* `ANSIBLE_NAVIGATOR_INVENTORY_COLUMNS`**Settings file:**   ```yaml ansible-navigator:   inventory-columns: ```                                                                         |
| <br>playbook                  | <br>Specify the playbook name.                                                                                                                        | <br>**Default:** No default value set<br>**CLI:** positional<br> **ENV:** `ANSIBLE_NAVIGATOR_PLAYBOOK`<br>**Settings file:**\*   ```yaml ansible-navigator:   ansible:     playbook: ```                                                                                            |
| <br>playbook-artifact-enable  | <br>Enable or disable the creation of artifacts for completed playbooks. Note: not compatible with `--mode stdout` when playbooks require user input. | <br>**Choices:**`True` or `False`<br> **Default:** `True`<br>**CLI:**`--pae` or `--playbook-artifact-enable`**ENV:**`ANSIBLE_NAVIGATOR_PLAYBOOK_ARTIFACT_ENABLE`**Settings file:**   ```yaml ansible-navigator:   playbook-artifact:     enable: ```                                |
| <br>playbook-artifact-save-as | <br>Specify the name for artifacts created from completed playbooks.                                                                                  | <br> **Default:** `{playbook_dir}/{playbook_name}-artifact-{ts_utc}.json`<br>**CLI:**`--pas` or `--playbook-artifact-save-as`<br> **ENV:** `ANSIBLE_NAVIGATOR_PLAYBOOK_ARTIFACT_SAVE_AS`<br> **Settings file:**    ```yaml ansible-navigator:   playbook-artifact:     save-as: ``` |
