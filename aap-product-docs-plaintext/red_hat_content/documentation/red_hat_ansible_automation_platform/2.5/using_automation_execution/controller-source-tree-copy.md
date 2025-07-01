# 5. Jobs in automation controller
## 5.5. Job branch overriding
### 5.5.1. Source tree copy behavior




Every job run has its own private data directory. This directory contains a copy of the project source tree for the given `scm_branch` that the job is running. Jobs are free to make changes to the project folder and make use of those changes while it is still running. This folder is temporary and is removed at the end of the job run.

If you check the **Clean** option, modified files are removed in automation controller’s local copy of the repository. This is done through use of the force parameter in its corresponding Ansible modules pertaining to git or Subversion.

**Additional resources**

For more information, see the [Parameters](https://docs.ansible.com/ansible/latest/modules/git_module.html#parameters) section of the Ansible documentation.


