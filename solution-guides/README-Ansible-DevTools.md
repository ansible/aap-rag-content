<div class="guide-header">

<h1>AI-Assisted Ansible Developer Experience</h1>

<span class="guide-type-badge guide-type-badge--solution"><i class="fas fa-check-circle" aria-hidden="true"></i> Solution Guide</span>

</div>

<div class="guide-hero-callout guide-hero-partner guide-hero-partner--redhat" role="img" aria-label="Ansible Automation Platform and Red Hat">
  <img src="assets/images/logos/aap-ansible-icon.png" alt="" class="guide-hero-callout__icon" width="36" height="36">
  <span class="guide-hero-partner__plus" aria-hidden="true">+</span>
  <span class="guide-hero-partner__partner card-partner-logo-set">
    <img src="assets/images/logos/redhat-logo.svg" alt="Red Hat" class="card-partner-logo" width="118" height="28">
  </span>
</div>

## Overview

Onboarding a new automation developer takes anywhere from 1 to 3 months when done manually: waiting for laptop provisioning, requesting access permissions, installing the right Python version, resolving dependency conflicts, configuring linting rules to match the team's standards, and debugging why molecule tests pass on a colleague's machine but fail on theirs. Multiply that across a team of 10 or 15 engineers, and the cost of inconsistent development environments becomes significant: delayed projects, "works on my machine" bugs, and quality standards that exist on paper but not in practice.

**Ansible Development Tools (ADT)** solves this by bundling essential CLI tools into a single, versioned package -- no Ansible Automation Platform installation required. ADT is available through four delivery methods that represent an evolution from individual setup to enterprise-governed environments:

```mermaid
graph LR
    A["uv/pip<br/><b>Individual</b><br/>~30 min"] -->|standardize| B["RPM<br/><b>Managed</b><br/>~15 min"]
    B -->|containerize| C["Dev Container<br/><b>Standardized</b><br/>~10 min"]
    C -->|centralize| D["Dev Spaces<br/><b>Governed</b><br/>~5 min"]
```

The goal is to move every automation developer in your organization onto the same toolchain, with the same versions, the same linting rules, and the same testing frameworks. Dev containers and Dev Spaces are the recommended enterprise options: they require an initial investment in image management to account for different project scenarios, but once that setup is done, the environment is completely transparent to developers. See the [Maturity Path](#maturity-path) for a detailed comparison of each method.

> **Example:** Dev Spaces onboarding.
>
> A network automation team of 12 engineers across three offices adopts Dev Spaces. A new engineer joins on Monday, opens a browser, navigates to the Dev Spaces URL, and clicks "Create Workspace" on the team's Git repository. Five minutes later they have a full VS Code environment with ansible-lint, molecule, ansible-navigator, and the team's linting profile, identical to every other engineer on the team. No local installs, no "which Python version do I need," no VPN issues with package mirrors.

### AI-Assisted Ansible Development

The Model Context Protocol (MCP) is an open standard that enables AI coding assistants to interact with external tools through a unified interface. The Ansible ecosystem provides two MCP servers that enhance the developer experience when used with AI assistants like Claude Code, VS Code Copilot Chat, or Cursor:

- **Ansible Devtools MCP Server** -- gives AI assistants direct access to ADT tools (lint, scaffold, navigate, build) so they can create, validate, and fix Ansible content on your behalf.
- **Ansible Automation Platform MCP Server** -- gives AI assistants access to your AAP instance (inventory, job templates, workflows) so they can query platform state and launch automation during development and testing.

```mermaid
graph LR
    IDE["<b>VS Code / AI Assistant</b><br/>Claude Code, Copilot Chat, Cursor"]
    IDE -->|MCP| DT["<b>Devtools MCP Server</b><br/>Scaffold, lint, run, build EEs"]
    IDE -->|MCP| AAP["<b>AAP MCP Server</b><br/>Jobs, inventory, monitoring, RBAC"]
    DT --> LOCAL["<b>Local Development</b><br/>ansible-creator · ansible-lint<br/>ansible-navigator · ansible-builder"]
    AAP --> PLATFORM["<b>AAP Instance</b><br/>Launch jobs · Query inventory<br/>Platform health · Credentials"]
```

> **Tip:** MCP server availability.
>
> The Ansible Devtools MCP Server is currently available as a technology preview. The AAP MCP Server is generally available.

Together, these turn your AI assistant into an Ansible-aware pair programmer that can scaffold a collection, lint it, run it against a development AAP instance, and troubleshoot the results -- all within a single conversation:

```mermaid
graph LR
    A["<b>Scaffold</b><br/>ansible-creator"] -->|lint & fix| B["<b>Validate locally</b><br/>ansible-lint"]
    B -->|query targets| C["<b>Check inventory</b><br/>AAP MCP"]
    C -->|launch job| D["<b>Run on AAP</b><br/>AAP MCP"]
    D -->|inspect results| E["<b>Troubleshoot</b><br/>Devtools + AAP MCP"]
```

1. **Scaffold** -- the AI assistant uses the Devtools MCP server to create a new role or playbook with `ansible-creator`, pre-configured with the correct structure and metadata.
2. **Validate locally** -- the assistant runs `ansible-lint` through the Devtools MCP server, identifies issues, and applies fixes automatically before the code ever reaches AAP.
3. **Check inventory** -- the assistant queries the AAP inventory through the AAP MCP server to verify target hosts, groups, and variables match what the playbook expects.
4. **Run on AAP** -- the assistant launches the playbook as a job on a development AAP instance, using the correct job template, credentials, and survey variables.
5. **Troubleshoot** -- if the job fails, the assistant inspects the job output through AAP MCP, correlates it with the playbook logic it can read locally through Devtools MCP, and proposes a fix. The cycle repeats from step 2 until the job succeeds.

> **Example:** NTP configuration with AI-assisted workflow.
>
> A developer asks the AI assistant to "configure NTP on my RHEL hosts." Before writing any code, the assistant searches Automation Hub and discovers `redhat.rhel_system_roles.timesync`, a certified, tested role that handles chrony, ntp, and linuxptp configuration. It asks: "There's a certified role for this. Want to use it, or build a custom one?"
>
> **Path 1: Use existing content.** The developer chooses the certified role. The assistant looks up the role's parameters, generates a playbook that sets `timesync_ntp_servers` with the organization's NTP pool, lints it, queries the AAP development instance to confirm the RHEL inventory group exists, launches a test job, and validates that chrony is running with the correct sources. The developer never had to read the role's documentation.
>
> **Path 2: Build from scratch.** The developer also needs clock drift reported to an internal monitoring system. The `timesync` role configures NTP perfectly, but it does not export metrics. The assistant scaffolds a custom role with `ansible-creator` that queries `chronyc tracking`, extracts drift values, and posts them to the monitoring API. It lints the new role, runs it against the dev AAP instance alongside the certified role, and confirms both work together. The certified role handles NTP configuration; the custom role handles observability.
>
> In both paths, the developer stays in one conversation. The AI assistant handles discovery, scaffolding, validation, and troubleshooting while the developer focuses on intent and decisions.

---

## Background

The Ansible content lifecycle -- **Create, Test, Deploy** -- requires a set of specialized tools at each stage. When each developer installs and maintains these tools individually, environment drift is inevitable: one developer runs ansible-lint 24.x while another has 25.x, molecule tests pass on Linux but fail on macOS because of a missing dependency, and the new hire spends their first week troubleshooting Python conflicts instead of writing automation.

This drift compounds across teams. A role that passes CI on one developer's machine may fail on another's. Linting rules that are enforced locally may not match the CI pipeline. When something breaks in production, the first question is always "which version were you running?" instead of "what changed?"

ADT addresses this by providing a single installable package (or container image) that bundles known-good versions of all essential tools. Whether you install via uv/pip, RPM, or use a containerized environment, you get the same toolchain with the same integration guarantees. The container-based methods (dev containers and Dev Spaces) go further: they guarantee not just the same tool versions but the same OS, the same Python, the same VS Code extensions, and the same linting configuration for every developer.

> **Why a bundle instead of individual installs?**
>
> The tools in ADT are tightly integrated -- `ansible-lint` feeds into the VS Code extension, `molecule` uses `ansible-navigator` and `podman` under the hood, and `ansible-creator` scaffolds projects pre-configured for all of them. Installing them separately risks version conflicts and broken integrations.

---

## Solution

### What's in the Bundle

ADT includes ten tools covering the full content lifecycle:

```mermaid
graph LR
    A["<b>Create</b><br/>ansible-creator<br/>ansible-dev-environment<br/>ansible-core"] -->|validate| B["<b>Test</b><br/>ansible-lint<br/>molecule<br/>pytest-ansible<br/>tox-ansible"]
    B -->|package & run| C["<b>Deploy</b><br/>ansible-builder<br/>ansible-navigator<br/>ansible-sign"]
```

| Stage | Tool | Purpose |
|-------|------|---------|
| **Create** | `ansible-creator` | Scaffold collections, roles, playbooks, and plugins |
| **Create** | `ansible-dev-environment` | pip-like install for Ansible collections in virtual environments |
| **Create** | `ansible-core` | Core automation engine |
| **Test** | `ansible-lint` | Static analysis for playbooks, roles, and collections |
| **Test** | `molecule` | Integration testing with ephemeral infrastructure |
| **Test** | `pytest-ansible` | pytest plugin for testing module and plugin Python code |
| **Test** | `tox-ansible` | Test matrix across Python and ansible-core versions |
| **Deploy** | `ansible-builder` | Build execution environments (container images) |
| **Deploy** | `ansible-galaxy` | Install collections and roles from Galaxy or Automation Hub (included with `ansible-core`) |
| **Deploy** | `ansible-navigator` | TUI for running and troubleshooting automation with EEs |
| **Deploy** | `ansible-sign` | Sign and verify Ansible project contents |

### Who Benefits

| Persona | Challenge | What They Gain |
|---------|-----------|----------------|
| **Automation Developer** | Spending days or weeks assembling tools, resolving conflicts, and matching versions with the rest of the team instead of writing automation | A single install (or a container they never have to configure) that provides all tools in known-good, compatible versions |
| **Platform Engineer / SRE** | Inconsistent environments across developers causing "works on my machine" failures that waste CI cycles and delay releases | Containerized workspaces that guarantee identical toolchains for every developer, eliminating environment as a variable |
| **Automation Architect** | Enforcing development standards and testing practices across multiple teams when each team manages tools differently | Standardized tooling embedded in the project repo (`.devcontainer/`) or the platform (Dev Spaces), so standards are inherited, not documented |
| **Engineering Manager** | New developers take 1 to 3 months to become productive, with most of that time spent on environment setup and troubleshooting | Onboarding drops to minutes with dev containers or Dev Spaces. New hires open a browser or VS Code and start contributing on day one |

---

## Prerequisites

### Ansible Automation Platform

- **uv/pip methods:** No AAP subscription required -- these use the upstream community packages.
- **Dev container method:** Available in two variants -- a free upstream community image (no subscription required) and a supported downstream image from `registry.redhat.io` (requires an AAP or Ansible Developer subscription).
- **RPM method:** Requires an AAP or Ansible Developer subscription (supported) and RHEL 9 registered with Red Hat Subscription Manager.
- **Dev Spaces method:** Requires an OpenShift subscription (supported) with the Dev Spaces operator installed.

### System Requirements

| Requirement | uv/pip | RPM | Dev Container | Dev Spaces |
|-------------|-----|-----|---------------|------------|
| **Python** | 3.10+ | 3.10+ (included in RHEL 9+) | N/A (in container) | N/A (in container) |
| **OS** | Linux, macOS, WSL | RHEL 9 | Any (VS Code + container runtime) | Browser only |
| **Container runtime** | Optional (for molecule, builder) | Optional (for molecule, builder) | Docker or Podman | Managed by OpenShift |
| **Disk space** | ~500 MB | ~500 MB | ~2 GB (image) | Managed by cluster |
| **Subscription** | None | AAP or Ansible Developer (supported) | None (community) or AAP/Ansible Developer (supported) | OpenShift (supported) |

---

## Maturity Path

| Maturity | Method | Onboarding | What You Do | Consistency | Who manages it |
|----------|--------|-----------|-------------|-------------|---------------|
| **Crawl** | pipx/pip | ~30 min | Individual developers install ADT on their own workstations. Each developer manages their own Python version and tool upgrades. Teams coordinate versions manually via chat or documentation. | Low: each developer manages their own environment, drift is inevitable | Developer |
| **Walk** | RPM | ~15 min | IT includes ADT in the standard RHEL laptop provisioning via Satellite. All developers on RHEL get the same RPM version. Add `ansible-lint` and `molecule` to CI pipelines for a second layer of consistency. | Medium: same tool versions across RHEL systems, but no guarantee of IDE config, linting profiles, or Python library alignment | IT / Platform team |
| **Run** | Dev Container | ~10 min | Add a `.devcontainer/` directory to every Ansible project repo. Developers open the repo in VS Code and get the full environment automatically. The platform team manages a base container image; teams can extend it for project-specific needs. | High: same OS, same Python, same tools, same VS Code extensions, same linting config | Team lead / repo owner |
| **Fly** | Dev Spaces | ~5 min | Deploy Dev Spaces on OpenShift for the entire organization. Developers open a browser, click create, and start coding. The platform team manages workspace images, resource limits, and access centrally. | Highest: zero local dependencies, zero configuration, fully governed | Platform team / IT |

> **Tip:** Dev containers and Dev Spaces are the target.
>
> The pipx/pip and RPM methods are stepping stones. They get individual developers productive quickly, but they don't solve the consistency problem at scale. Invest in a base container image early. Once that image exists, both dev containers and Dev Spaces use it, and every developer gets an identical environment from day one.

### Detailed Comparison

| Dimension | pipx/pip | RPM | Dev Container | Dev Spaces |
|-----------|--------|-----|---------------|------------|
| **Local install required** | Python 3.10+ | RHEL + subscription | VS Code + container runtime | Browser only |
| **Image management needed** | No | No | Yes (initial investment) | Yes (initial investment) |
| **Nested containers** | N/A (use host runtime) | N/A (use host runtime) | Yes (with capabilities) | Yes (OCP user namespaces) |
| **Offline / air-gapped** | PyPI mirror | Satellite | Registry mirror | Internal registry |
| **Vendor support** | Community | Red Hat (supported) | Community or Red Hat (supported) | Red Hat (supported) |
| **Cost** | Free | AAP or Ansible Developer subscription (supported) | Free (community) or AAP/Ansible Developer subscription (supported) | OpenShift subscription (supported) |

By standardizing on ADT, your organization eliminates environment drift as a source of CI failures, reduces developer onboarding from weeks to minutes, and ensures that every automation artifact is created, tested, and deployed with the same governed toolchain. The investment shifts from individual troubleshooting to platform management -- a one-time image setup that scales across every team and project without requiring action from individual developers.

---

## Installation Methods

### Method A: Dev Container (VS Code)

**Best for:** Teams wanting a consistent, reproducible development environment without managing Python installations. Works on any OS that runs VS Code and a container runtime.

Pre-built container images with all ADT tools, the Ansible VS Code extension, and nested Podman support are available in two variants:

- **Red Hat supported:** `registry.redhat.io/ansible-automation-platform-26/ansible-dev-tools-rhel9` (requires [Red Hat registry authentication](https://access.redhat.com/RegistryAuthentication))
- **Community:** `ghcr.io/ansible/community-ansible-dev-tools:latest`

**Step 1:** Install prerequisites:

- [VS Code](https://code.visualstudio.com/)
- [Ansible extension for VS Code](https://marketplace.visualstudio.com/items?itemName=redhat.ansible) (`redhat.ansible`)
- [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) (`ms-vscode-remote.remote-containers`)
- A container runtime: [Docker Desktop](https://www.docker.com/products/docker-desktop/) or [Podman Desktop](https://podman-desktop.io/)

**Step 2:** Add a devcontainer to your project using one of these methods:

**Option A: CLI.** Run `ansible-creator` to scaffold devcontainer files into an existing project:

```bash
ansible-creator add resource devcontainer /path/to/your/project
```

This generates a `.devcontainer/` directory with both Docker and Podman configurations.

**Option B: VS Code UI.** Open the command palette (`Ctrl+Shift+P` / `Cmd+Shift+P`) and run **Ansible: Add devcontainer configuration**. The Ansible extension generates the same `.devcontainer/` directory.

> **Tip:** Using the supported downstream image.
>
> To use the Red Hat supported image instead of the community one, replace the `image` value in your `devcontainer.json` with `registry.redhat.io/ansible-automation-platform-26/ansible-dev-tools-rhel9:latest`. You must authenticate to `registry.redhat.io` first -- run `podman login registry.redhat.io` (or `docker login`) with your Red Hat account credentials. See [Red Hat Registry Authentication](https://access.redhat.com/RegistryAuthentication) for details.

**Step 3:** Open your project in VS Code, and when prompted, click **Reopen in Container** (or run the command `Dev Containers: Reopen in Container` from the command palette).

**Step 4:** Open a terminal in VS Code and verify:

```bash
adt --version
```

> **Tip:** Nested Podman is supported.
>
> The container image supports nested Podman, so you can run `molecule test` and `ansible-builder build` inside the dev container without additional configuration.

---

### Method B: RPM (Red Hat Subscription)

**Best for:** Enterprise environments running RHEL with Red Hat subscriptions, air-gapped networks with Satellite.

**Step 1:** Register your system and enable a repository that includes ADT. Two subscription options are available:

```bash
# Option 1: Ansible Automation Platform subscription (AAP 2.6, RHEL 9)
sudo subscription-manager repos \
  --enable ansible-automation-platform-2.6-for-rhel-9-x86_64-rpms

# Option 2: Ansible Developer subscription (Developer 1.3, RHEL 9)
sudo subscription-manager repos \
  --enable ansible-developer-1.3-for-rhel-9-x86_64-rpms
```

> **Tip:** Choose the right subscription for your use case.
>
> The **Ansible Developer** subscription provides the development tools without bundling the full AAP platform -- this is often more appropriate for developer workstations. The **AAP** subscription includes the dev tools alongside the full platform components.

**Step 2:** Install ADT:

```bash
sudo dnf install ansible-dev-tools
```

**Step 3:** Verify the installation:

```bash
adt --version
```

> **Why RPM over uv/pip?**
>
> The RPM packages are built and tested by Red Hat, receive security errata through the standard RHEL advisory process, and are supported under a Red Hat subscription. This is the recommended method for enterprises that need vendor-backed support and predictable update cycles.

**Available repositories:**

Both subscriptions provide repos for RHEL 9 across four architectures: `x86_64`, `aarch64`, `ppc64le`, and `s390x`. Replace the architecture in the repo name to match your system:

- **Ansible Automation Platform:** `ansible-automation-platform-{version}-for-rhel-9-{arch}-rpms` (versions: 2.6, 2.5)
- **Ansible Developer:** `ansible-developer-{version}-for-rhel-9-{arch}-rpms` (versions: 1.3, 1.2)

---

### Method C: Python Package (pipx)

**Best for:** Individual developers, quick setup on Linux/macOS/WSL, CI pipelines.

```bash
pipx install ansible-dev-tools
adt --version
```

To upgrade: `pipx upgrade ansible-dev-tools`. To pin a version: `pipx install ansible-dev-tools==26.4.6`.

> **Tip:** Install pipx first if you don't have it.
>
> macOS: `brew install pipx`. Fedora/RHEL: `dnf install pipx`. Ubuntu/Debian: `apt install pipx`.

---

### Method D: Red Hat OpenShift Dev Spaces

**Best for:** Enterprise teams wanting centralized, browser-based development environments with zero local setup. Ideal for onboarding, workshops, and environments where developers cannot install software on their workstations.

Dev Spaces provides a full VS Code environment running in the browser, backed by an OpenShift cluster. All tools, extensions, and project sources are defined in a `devfile.yaml` -- a declarative workspace specification.

**Step 1:** Ensure your OpenShift cluster has the Dev Spaces operator installed and configured.

**Step 2:** Log into the Dev Spaces dashboard:

```
https://devspaces.<your-openshift-ingress-domain>
```

**Step 3:** Import a workspace from a Git repository. Paste the URL of a repository containing a `devfile.yaml`, for example:

```
https://github.com/rhpds/ansible-dev-tools-workspace.git
```

Click **Create & Open**. The workspace provisions automatically with all ADT tools pre-installed.

**Step 4:** Once the VS Code interface loads in your browser, open a terminal and verify:

```bash
adt --version
```

> **Why Dev Spaces?**
>
> Unlike local dev containers, Dev Spaces runs entirely in the cloud. Developers only need a browser. The platform administrator controls the image, resource limits, and access -- ensuring every developer gets an identical, governed environment. This also enables features like rootless nested containers via OpenShift user namespaces, which are difficult to configure on local workstations.

**Key capabilities in Dev Spaces:**

| Feature | Details |
|---------|---------|
| **Browser-based VS Code** | Full IDE experience with no local install |
| **Nested containers** | Rootless Podman for molecule tests and EE builds |
| **Workspace-as-code** | `devfile.yaml` defines tools, repos, and resources declaratively |
| **Multi-user** | Each developer gets an isolated workspace on shared infrastructure |
| **Preloaded extensions** | Ansible VS Code extension with lint, navigator, and creator integration |
| **Git integration** | OAuth2 for GitHub/GitLab, SSH key forwarding |

---

## Configuring MCP Servers

### Ansible Devtools MCP Server

The <a href="https://docs.ansible.com/projects/vscode-ansible/mcp/" target="_blank">Ansible Devtools MCP Server</a> (`@ansible/ansible-mcp-server`) exposes ADT tools to any MCP-compatible AI client. It provides capabilities for playbook and collection scaffolding, automated linting with fix suggestions, execution environment building, and playbook execution via ansible-navigator.

**Installation options:**

| Method | Command | Requirements |
|--------|---------|-------------|
| **npm** | `npx -y @ansible/ansible-mcp-server --stdio` | Node.js 24+ |
| **Container** | `ghcr.io/ansible/devtools-mcp-server:latest` | Docker or Podman |
| **VS Code extension** | Enable `ansible.mcpServer.enabled` in settings | Ansible VS Code extension |

**Adding to Claude Code:**

```bash
claude mcp add ansible -- npx -y @ansible/ansible-mcp-server --stdio
```

**Adding to Claude Code (container):**

```bash
claude mcp add ansible -- podman run --rm -i \
  -v /path/to/your/ansible/project:/workspace \
  -e WORKSPACE_ROOT=/workspace \
  ghcr.io/ansible/devtools-mcp-server:latest --stdio
```

**Adding to VS Code Copilot Chat** (in `.vscode/settings.json`):

```json
{
  "mcp": {
    "servers": {
      "ansible": {
        "command": "npx",
        "args": ["-y", "@ansible/ansible-mcp-server", "--stdio"],
        "env": {
          "WORKSPACE_ROOT": "${workspaceFolder}"
        }
      }
    }
  }
}
```

When using the Ansible VS Code extension, the MCP server can be started automatically -- no manual configuration is required. Set `ansible.mcpServer.enabled` to `true` in your extension settings.

### Connecting to Ansible Automation Platform

When developing against a development or staging AAP instance, the <a href="https://www.redhat.com/en/blog/it-automation-agentic-ai-introducing-mcp-server-red-hat-ansible-automation-platform" target="_blank">AAP MCP server</a> allows your AI assistant to query inventories, inspect job templates, launch jobs, and monitor results -- all without leaving your editor. This is particularly useful for iterating on automation content: write a playbook, push it to your dev AAP instance, run it, and troubleshoot failures in a single workflow.

The AAP gateway (starting with AAP 2.6.4) exposes MCP on port **8448**. In **AAP 2.7**, URLs use the `/mcp/<toolset>` pattern (older guides used `/<toolset>/mcp`). See [Deploying the Ansible MCP server](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/extend-assembly_deploying_ansible_mcp_server#proc-connect-ai-agent-ansible-mcp-server).

| Service | Endpoint (2.7) | What It Provides |
|---------|------------------|------------------|
| **Discover (recommended)** | `/mcp/discover` | Lightweight toolset summary; loads only the toolset you need per session |
| **All tools** | `/mcp` | Full catalog on every connection (higher token use) |
| **Job Management** | `/mcp/job_management` | Launch, monitor, and inspect job runs |
| **Inventory Management** | `/mcp/inventory_management` | Query hosts, groups, and inventory sources |
| **System Monitoring** | `/mcp/system_monitoring` | Check platform health and capacity |
| **User Management** | `/mcp/user_management` | Inspect users, teams, and organizations |
| **Security & Compliance** | `/mcp/security_compliance` | Review RBAC policies and credentials |
| **Platform Configuration** | `/mcp/platform_configuration` | Inspect settings and configuration |
| **Content Discovery** | `/mcp/content_discovery` | Search collections, EEs, and intelligent assistant knowledge |

**Adding AAP MCP to Claude Code** (using a `.mcp.json` file in your project root):

```json
{
  "mcpServers": {
    "aap-mcp-discover": {
      "type": "http",
      "url": "https://aap-gateway.example.com:8448/mcp/discover",
      "headersHelper": "echo '{\"Authorization\": \"Bearer '\"$MCP_AAP_TOKEN\"'\"}'"
    },
    "aap-mcp-job-management": {
      "type": "http",
      "url": "https://aap-gateway.example.com:8448/mcp/job_management",
      "headersHelper": "echo '{\"Authorization\": \"Bearer '\"$MCP_AAP_TOKEN\"'\"}'"
    },
    "aap-mcp-inventory-management": {
      "type": "http",
      "url": "https://aap-gateway.example.com:8448/mcp/inventory_management",
      "headersHelper": "echo '{\"Authorization\": \"Bearer '\"$MCP_AAP_TOKEN\"'\"}'"
    }
  }
}
```

> **Tip:** Prefer a single **`/mcp/discover`** entry unless you need to restrict which toolsets the agent can load.
>
> You don't have to configure all six AAP MCP services at once. For content development, `job_management` and `inventory_management` are typically the most useful -- they let your AI assistant launch test runs and inspect target hosts.

Authentication uses an AAP personal access token passed via `MCP_AAP_TOKEN`. The MCP server inherits the user's RBAC permissions, so the AI assistant can only access what the token owner is authorized to see. Tokens can be scoped as read-only or read-write, providing an additional layer of control -- a read-only token lets the AI assistant query inventories, inspect job results, and review platform configuration without being able to launch jobs or modify state. Note that job execution requires a write-scoped token.

> **Warning:** Use development or staging AAP instances for AI-assisted workflows.
>
> AI assistants can launch jobs and modify platform state through the AAP MCP server. Always point MCP configurations at non-production instances during development, and use a read-only token unless you specifically need the AI assistant to launch jobs.

---

## Related Guides

- **Database automation:** The [EDB Postgres automation guide](README-EDB.md) demonstrates a multi-role deployment that benefits from consistent dev environments -- teams working on complex database automation can use ADT dev containers to ensure every contributor has the same linting rules and molecule test setup.
- **ITSM integration:** The [ServiceNow ITSM guide](README-ServiceNow-ITSM.md) and [RHEL patching guide](README-Patching-RHEL.md) show production automation workflows where environment consistency directly reduces "works on my machine" failures in CI/CD pipelines.
- **AI-assisted operations:** The [Intelligent Assistant with RHAIIS guide](README-Intelligent-Assistant-RHAIIS.md) extends the AI-assisted development theme -- once your dev environment includes the Ansible MCP server, the same AI assistant that helps you write automation can also interact with your AAP instance.
- **Network automation:** The [NetBox + AAP guide](README-NetBox-WAN-EDA-Failover.md) and [NetBox + EDA guide](README-NetBox-SoT-EDA-Config.md) are examples of multi-tool integrations where standardized dev environments prevent version conflicts across collections.

---

## Sources

**Red Hat product documentation**

- [Ansible development tools overview (AAP 2.7)](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/develop-assembly_devtools_intro)
- [Installing Ansible development tools (AAP 2.7)](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/extend-install_ansible_development_tools_with_the_ai_assistant)
- [Using Ansible development workspaces (AAP 2.7)](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/develop-assembly_workspaces_intro)
- [MCP server integration (AAP 2.7)](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/develop-con_mcp_server_integration)
- [ansible-dev-tools-rhel9 container](https://catalog.redhat.com/en/software/containers/ansible-automation-platform-27/ansible-dev-tools-rhel9/69fb1e26616f0fc2878516a6)
- [Red Hat OpenShift Dev Spaces documentation](https://access.redhat.com/documentation/en-us/red_hat_openshift_dev_spaces/)

**Community**

- [Ansible Development Tools documentation](https://docs.ansible.com/projects/dev-tools/)
- [ansible-dev-tools on GitHub](https://github.com/ansible/ansible-dev-tools)
- [community-ansible-dev-tools container](https://docs.ansible.com/projects/dev-tools/container/)
- [community-ansible-dev-tools on GHCR](https://github.com/ansible/community-ansible-dev-tools/pkgs/container/community-ansible-dev-tools)
- [OpenShift Dev Spaces with ADT](https://docs.ansible.com/projects/dev-tools/devspaces/)
- [ansible-dev-tools on PyPI](https://pypi.org/project/ansible-dev-tools/)
- [Ansible extension for VS Code](https://marketplace.visualstudio.com/items?itemName=redhat.ansible)
- [Ansible Forum (devtools)](https://forum.ansible.com/tags/devtools)
- [Molecule documentation](https://ansible.readthedocs.io/projects/molecule/)
- [ansible-sign documentation](https://docs.ansible.com/projects/sign/)

---

*Copyright 2026 Red Hat, Inc.*
