# Automation dashboard deployment options
## When to use each option

Use the **integrated automation dashboard** when:

- You are installing, or already running, Ansible Automation Platform 2.7 or later with the containerized or operator-based installer.
- You want the dashboard deployed, upgraded, and maintained as part of the platform.
- Your automation savings data comes from a single Ansible Automation Platform deployment.

Use the **standalone automation dashboard utility (RHEL only)** when:

- You run on RHEL and cannot or do not want to enable the dashboard during a platform installation.
- You want to connect to and aggregate savings from multiple Ansible Automation Platform deployments (2.4 and later).
- You want to manage the dashboard on its own lifecycle, separate from the platform.
