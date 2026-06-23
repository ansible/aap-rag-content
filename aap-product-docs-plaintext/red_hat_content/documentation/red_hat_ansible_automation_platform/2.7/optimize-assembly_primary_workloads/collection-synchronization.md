# Understand primary workloads for automation controller
## Minimize the impact of collection syncing

Private automation hub can synchronize collections from remote `ansible-galaxy` repositories, such as `galaxy.ansible.com` or automation hub on `console.redhat.com`.

Pulp content workers and the database synchronize the repositories. The automation controller can download these collections during project updates, or use them to build automation execution environments. Collections are also available for any other client by using the `ansible-galaxy` CLI to download and use.

The performance of collection synchronization is impacted by the following:

- The number of collections listed in the `requirements.yml`
- The number of versions synced
- The number of versions retained


Synchronization uses memory in direct proportion to the number of collections and versions synchronized. Using a targeted `requirements.yml` with specific versions can limit this impact.

Hosting collections uses storage space. Manage the storage space that collections use by specifying the retained number of versions on the repository.

