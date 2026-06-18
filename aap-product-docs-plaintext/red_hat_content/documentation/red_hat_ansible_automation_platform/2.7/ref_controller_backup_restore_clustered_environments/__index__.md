# Backup and restore in clustered environments

Learn how to back up and restore automation controller in a clustered environment.

The procedure for backup and restore for a clustered environment is similar to a single install, except for some of the following considerations:

- If restoring to a new cluster, ensure that the old cluster is shut down before proceeding because they can conflict with each other when accessing the database.
- Per-node backups are only restored to nodes bearing the same hostname as the backup.
- When restoring to an existing cluster, the restore has the following:
* A dump of the PostgreSQL database
* UI artifacts, included in the database dump
* An automation controller configuration (retrieved from `/etc/tower`)
* An automation controller secret key
* Manual projects
