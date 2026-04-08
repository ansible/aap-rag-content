# 1. Types of workloads
## 1.5. Collection synchronization




Private automation hub can synchronize collections from remote `ansible-galaxy` repositories, such as `galaxy.ansible.com` or automation hub on `console.redhat.com` .

Pulp content worker and the database sync repositories. The automation controller can download these collections during project updates, or use them to build automation execution environments. Collections are also available for any other client by using the `ansible-galaxy` CLI to download and use.

The performance of syncing collections is relative to the number of collections listed in the `requirements.yml` , the number of versions synced, and the number of versions retained. Specifically, synchronization uses memory in proportion to the number of collections and versions synchronized. Using a targeted `requirements.yml` with specific versions can limit this impact. Hosting collections uses storage space. Manage the storage space that collections use by specifying the retained number of versions on the repository.

