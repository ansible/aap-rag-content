# Ansible Automation Platform patch release June 17, 2026 (2.7-1)
## Controller

- Installed collections and Ansible version are now recorded for every job run, regardless of whether the Indirect Node Counting feature flag is enabled. Previously, this metadata was only collected when `FEATURE_INDIRECT_NODE_COUNTING_ENABLED` was on. (AAP-76810)

