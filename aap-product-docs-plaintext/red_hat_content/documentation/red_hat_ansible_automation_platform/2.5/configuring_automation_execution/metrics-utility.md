# Chapter 12. Usage reporting with metrics-utility




The Ansible Automation Platform metrics utility tool ( `metrics-utility` ) is a command-line utility that is installed on a system containing an instance of automation controller.

When installed and configured, `metrics-utility` gathers billing-related metrics from your system and creates a consumption-based billing report. The `metrics-utility` tool is especially suited for users who have multiple managed hosts and want to use consumption-based billing. After a report is generated, it is deposited in a target location that you specify in the configuration file.

`metrics-utility` collects two types of data from your system: configuration data and reporting data.

The configuration data includes the following information:

- Version information for automation controller and for the operating system
- Subscription information
- The base URL


The reporting data includes the following information:

- Job name and ID
- Host name
- Inventory name
- Organization name
- Project name
- Success or failure information
- Report date and time


To ensure that `metrics-utility` continues to work as configured, clear your report directories of outdated reports regularly.

