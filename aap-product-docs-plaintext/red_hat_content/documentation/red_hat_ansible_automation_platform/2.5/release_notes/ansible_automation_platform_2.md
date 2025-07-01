# 8. Fixed issues
## 8.1. Ansible Automation Platform




- The installer now ensures semanage command is available when SELinux is enabled. (AAP-24396)
- The installer can now update certificates without attempting to start the nginx service for previously installed environments. (AAP-19948)
- Event-Driven Ansible installation now fails when the pre-existing automation controller is older than version 4.4.0. (AAP-18572)
- Event-Driven Ansible can now successfully install on its own with a controller URL when the controller is not in the inventory. (AAP-16483)
- Postgres tasks that create users in FIPS environments now use **scram-sha-256** . (AAP-16456)
- The installer now successfully generates a new `    SECRET_KEY` for controller. (AAP-15513)
- Ensure all backup and restore staged files and directories are cleaned up before running a backup or restore. You must also mark the files for deletion after a backup or restore. (AAP-14986)
- Postgres certificates are now temporarily copied when checking the Postgres version for SSL mode verify-full. (AAP-14732)
- The setup script now warns if the provided log path does not have write permissions, and fails if default path does not have write permissions. (AAP-14135)
- The linger configuration is now correctly set by the root user for the Event-Driven Ansible user. (AAP-13744)
- Subject alternative names for component hosts will now only be checked for signing certificates when HTTPS is enabled. (AAP-7737)
- The UI for creating and editing an organization now validates the **Max hosts** value. This value must be an integer and have a value between 0 and 214748364. (AAP-23270)
- Installations that do not include the automation controller but have an external database will no longer install an unused internal Postgres server. (AAP-29798)
- Added default port values for all `    pg_port` variables in the installer. (AAP-18484)
-  **XDG_RUNTIME_DIR** is now defined when applying Event-Driven Ansible linger settings for Podman. (AAP-18341)*
- Fixed an issue where the restore process failed to stop **pulpcore-worker** services on RHEL 9. (AAP-12829)
- Fixed Postgres **sslmode** for verify-full that affected external Postgres and Postgres signed for 127.0.0.1 for internally managed Postgres. (AAP-7107)
- Fixed support for automation hub content signing. (AAP-9739)
- Fixed conditional code statements to align with changes from ansible-core issue #82295. (AAP-19053)
- Resolved an issue where providing the database installation with a custom port broke the installation of Postgres. (AAP-30636)


