# 9. Patch releases
## 9.1. Ansible Automation Platform patch release May 4, 2026
### 9.1.2. Enhancements

#### 9.1.2.1. Automation hub

- Added verification that Hub supports Execution Environments with PQC signatures.(AAP-71606)

#### 9.1.2.2. Container-based installer Ansible Automation Platform

- Fixed the preflight check to allow hop nodes to run on systems with less than 16GB of RAM.(AAP-71341)

#### 9.1.2.3. Red Hat Lightspeed

- Support for llama-stack 0.4.3.(AAP-69996)
- Support for llama-stack 0.4.3.(AAP-65012)

#### 9.1.2.4. Ansible Automation Platform Operator

- Allows the ability to disable backup db compression per component using the use_db_compression parameter (default: true). (AAP-69747)

#### 9.1.2.5. Ansible Automation Platform ui

- Private flags only appear in UI when enabled - this applies uniformly to both runtime and install-time private flags. Private runtime flags can be toggled off via the UI, which causes them to disappear. This prevents users from easily discovering feature flags that are not meant to be advertised to all customers.(AAP-69669)
- Added a Feature Flags page under Settings that allows platform administrators to view feature flags and toggle runtime flags on or off without restarting services.(AAP-69001)

#### 9.1.2.6. Automation controller

- Sets `XDG_CONFIG_HOME=/tmp/.config` in the `Containerfile` so podman-remote can write its config at runtime.
- Fixes `handle_removed_image` task failing with `RuntimeError`: Error running command in containerized installer deployments. (AAP-68260)

