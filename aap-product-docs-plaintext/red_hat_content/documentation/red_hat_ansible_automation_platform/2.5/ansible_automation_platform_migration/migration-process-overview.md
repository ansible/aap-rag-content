# Chapter 3. Migration process overview




Important
You can only migrate to a different installation type of the same Ansible Automation Platform version. For example you can migrate from RPM version 2.5 to containerized 2.5, but not from RPM version 2.4 to containerized 2.5.



The migration between Ansible Automation Platform installation types follows this general workflow:

1. Prepare and assess the source environment - Prepare and assess the existing source environment for migration.
1. Export the source environment - Extract the necessary data and configurations from the source environment.
1. Create and verify the migration artifact - Package all collected data and configurations into a migration artifact.
1. Prepare and assess the target environment - Prepare and assess the new target environment for migration.
1. Import the migration content to the target environment - Transfer the migration artifact into the prepared target environment.
1. Reconcile the target environment post-import - Address any inconsistencies and reconfigure services in the target environment after import.
1. Validate the target environment - Confirm the migrated environment is fully operational.


