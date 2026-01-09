# 6. Job templates
## 6.14. Benefits of fact caching




Fact caching saves you time over running fact gathering. If you have a playbook in a job that runs against a thousand hosts and forks, it can take 10 minutes to gather facts across all of those hosts.

If you run a job on a regular basis, the first run of it caches these facts and the next run pulls them from the database. This reduces the runtime of jobs against large inventories.

Note
Do not change the ansible.cfg file to apply fact caching. Custom fact caching could conflict with the controller’s fact caching feature. You must use the fact caching module that includes automation controller.



You can select to use cached facts in your job by checking the **Enable fact storage** option when you create or edit a job template.

The following is an example playbook that uses the Ansible `clear_facts` meta task.

```
- hosts: all
gather_facts: false
tasks:
- name: Clear gathered facts from all currently targeted hosts
meta: clear_facts
```

You can find the API endpoint for fact caching at:

http://<controller server name>/api/v2/hosts/x/ansible_facts

