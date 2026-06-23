# Install automation dashboard to calculate savings (RHEL only)

By effectively using automation dashboard, you can gain valuable insights into your Ansible Automation Platform usage and drive continuous improvement in your automation practices.

## About the automation dashboard

The automation dashboard utility is a web-based container application that provides key metrics related to job execution, efficiency, and the value derived from automation.

Automation dashboard uses automation metrics to supply automation usage data from Ansible Automation Platform. This data helps you compare the cost of performing tasks manually to the cost of performing tasks through automation, allowing you to show what savings are achievable through automation.

**Key benefits**

Automation dashboard helps you:

- Get a clear overview of the automation occurring in your environment.
- Track metrics such as time saved and errors reduced, to quantify the benefits of automation.
- Analyze job execution times and failure rates to pinpoint areas for automation improvement.
- Use the generated data to make informed decisions about automation strategy, resource allocation, and prioritization of automation projects.


**Automation Dashboard and Red Hat Ansible Automation Platform 2.7**

In Red Hat Ansible Automation Platform 2.7, two dashboard solutions are available:

- **Native Automation Dashboard (Technology Preview):** Integrated into Red Hat Ansible Automation Platform 2.7 as part of the Metrics Service. Suitable for single Red Hat Ansible Automation Platform instance monitoring with integrated Red Hat Ansible Automation Platform UI experience.
- **Standalone automation dashboard:** This guide describes the standalone utility, which continues to be supported in Red Hat Ansible Automation Platform 2.7 and later releases. Use the standalone utility when you need:
* Multi-instance monitoring (aggregating data across multiple Red Hat Ansible Automation Platform deployments)
* Independent dashboard infrastructure separate from Red Hat Ansible Automation Platform installation
* Dashboard for Red Hat Ansible Automation Platform versions prior to 2.7

## Choose between standalone and native dashboard (Red Hat Ansible Automation Platform 2.7+)

If you are running Red Hat Ansible Automation Platform 2.7, two dashboard options are available. Use this guidance to determine which dashboard solution meets your needs.

**Use standalone automation dashboard when:**

- **Multi-cluster monitoring is required:** You need to aggregate data across multiple Red Hat Ansible Automation Platform deployments (for example, production, staging, and development environments)
- **Using Red Hat Ansible Automation Platform version is 2.4, 2.5, or 2.6:** Native dashboard is only available in Red Hat Ansible Automation Platform 2.7
- **Independent infrastructure preferred:** You want dashboard infrastructure separate from Red Hat Ansible Automation Platform installation (for example, different security zones, independent scaling, disaster recovery isolation)


**Use native Automation Dashboard (Red Hat Ansible Automation Platform 2.7) when:**

- **Single Red Hat Ansible Automation Platform instance monitoring:** You only need to monitor one Red Hat Ansible Automation Platform deployment
- **Integrated experience preferred:** You want dashboard integrated into Red Hat Ansible Automation Platform unified UI with Gateway authentication
- **No additional infrastructure:** You do not want to deploy separate VMs or containers for dashboard
- **Using a new Red Hat Ansible Automation Platform 2.7 deployment:** You are installing Red Hat Ansible Automation Platform 2.7 for the first time

## Coexistence

Both dashboard solutions can run simultaneously. For example, you might use:

- **Standalone dashboard:** For aggregated view across multiple Red Hat Ansible Automation Platform environments
- **Native dashboard:** For detailed single-instance view of your Red Hat Ansible Automation Platform 2.7 production cluster

## Architecture comparison

**Standalone dashboard infrastructure:**

- Separate RHEL host or VM
- Dedicated PostgreSQL database
- Independent Redis instance
- Podman containerized deployment
- Manual OAuth2 token configuration
- Pulls data by using Red Hat Ansible Automation Platform API


**Native dashboard infrastructure (Technology Preview):**

- Integrated with Metrics Service (no separate VM)
- Uses Metrics Service PostgreSQL database
- Automatic Gateway authentication
- Enabled by using installer flag
- Data collected by Metrics Service backend

## Migration considerations

Important:

There is no automatic migration path from standalone dashboard to native dashboard in Red Hat Ansible Automation Platform 2.7. If you plan to transition from standalone to native dashboard in the future:

- Continue using standalone dashboard until multi-instance support is added to native dashboard (planned for future GA release)
- Contact Red Hat Support for guidance on migration planning

