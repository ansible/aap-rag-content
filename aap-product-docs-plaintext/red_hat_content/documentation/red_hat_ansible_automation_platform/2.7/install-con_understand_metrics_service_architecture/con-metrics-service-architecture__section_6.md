# Understand metrics service architecture
## Database schema architecture

*Figure 2. Metrics service database schema architecture*
![Architectural diagram for metrics service database schema (simplified)](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/metrics-service-simplified-schema.png)

**Collection phase**

1. Metrics service queries automation controller/`awx` database (read-only connection using `ms_awx_readonly` user)
2. Raw usage data extracted from the following tables: jobs, job host summaries, credentials, execution environments, controller versions, feature flags, and job events

**What is NOT collected:**

- Host inventory data
- Customer-defined template names, playbook names, or workflow names

Important:

Host and inventory data collection is handled separately by the metrics-utility CLI for CCSP reports only. Metrics service does not collect this data.

