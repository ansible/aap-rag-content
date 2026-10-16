# Understand metrics service architecture
## Anonymization phase

No personal data leaves the customer environment. Only publicly available collection names (for example from Galaxy) and built-in object names (such as built-in credential types and execution environments) are transmitted.

**Anonymization method:** Statistics and counts only

Metrics service transmits only aggregated statistics, counts, and built-in/public object names. Customer-defined object names are never transmitted. For example, if you have 3 custom credentials, metrics service sends the count "3" but does not send the credential names.

**What data is sent:**

- **Job statistics:** Aggregated job execution data grouped by job type, launch type, and version (success/failure counts, duration statistics, timestamps). Job template names are NOT included.
- **Job host summary statistics:** Aggregated job execution results per host (success/failure counts, execution performance metrics).
- **Credential type statistics:** Built-in credential type names (e.g., "Machine", "Source Control", "Vault") and count of customer-defined credentials (e.g., "3 custom credentials"). Customer-defined credential names are NOT sent.
- **Execution environment statistics:** Built-in EE names (e.g., "ee-minimal-rhel9", "ee-supported-rhel9") and count of customer-defined EEs (e.g., "5 custom EEs"). Customer-defined EE names are NOT sent.
- **Collection statistics:** Public collection names from Galaxy or Red Hat Certified Collections (e.g., "ansible.builtin", "ansible.posix") and count of customer-defined collections. Customer-defined collection names are NOT sent.
- **Collection, module, and role usage statistics**: Agregated counts of Ansible collection, module, and role usage extracted from job events. Data includes module execution counts, job success/failure rates, task retry and unreachable events, and collection-level host counts. Only publicly available (Certified, Community, and Validated) collection and module names are included. Custom-source entries and customer-defined role names are stripped during anonymization. Skipped tasks are excluded - only events from automation work that was actually performed are counted.
- **Project SCM types:** Source control management types for projects (e.g., Git, SVN).
- **Organization counts:** Total number of organizations configured.
- **Version information:** Controller version, Ansible core version, installed collection versions.
- **Warnings and deprecations:** Statistics on deprecation warnings encountered.
- **Feature flag states:** Boolean status of enabled/disabled feature flags.

**What data is NOT sent:**

- **Job template names** (not collected at all)
- **Customer-defined credential names** (only counts transmitted, e.g., "3 custom credentials")
- **Customer-defined execution environment names** (only counts transmitted, e.g., "5 custom EEs")
- **Customer-defined collection names** (only counts transmitted)
- **Host inventory data** (not queried by metrics service; handled separately by metrics-utility CLI for CCSP reports only)
- **Playbook names** (customer-defined content)
- **Variable names and values** (customer-defined content)
- **Workflow template names** (customer-defined content)

Important:

Customer-defined object names are never transmitted. Metrics service sends only counts (e.g., "3 custom credentials") and statistics (e.g., "50 jobs executed"). There is no way to identify which specific custom objects belong to which customer, and no individual object names can be recovered from the transmitted data.

