# Overview
## Patch updates compared with version upgrades

The operator supports two types of upgrades, each with different scope and risk profiles:

In-channel patch updates
Patch updates deliver bug fixes, security patches, and minor improvements within the same Ansible Automation Platform version (for example, 2.6.1 to 2.6.2). These updates are lower risk and typically do not include breaking changes. If your subscription is set to automatic approval, patch updates apply as soon as they are available.

Cross-channel version upgrades
Version upgrades move your deployment to a new Ansible Automation Platform release (for example, 2.6 to 2.7). These upgrades require you to change the subscription channel, are always manual, and may include infrastructure changes, API changes, or authentication changes that require additional preparation.

