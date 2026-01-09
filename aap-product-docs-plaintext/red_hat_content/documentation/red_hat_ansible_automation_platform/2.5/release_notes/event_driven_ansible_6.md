# 10. Patch releases
## 10.6. Ansible Automation Platform patch release July 2, 2025
### 10.6.9. Event-Driven Ansible




#### 10.6.9.1. Features




- API REST supports the editing of the URL of the project.(AAP-47459)
- Prior to this release, we suggested utilizing `    ansible.builtin.set_fact` within playbooks. We now advise using `    ansible.builtin.set_stats` as it enables seamless integration with job templates. We encourage migrating from `    ansible.builtin.set_fact` to `    ansible.builtin.set_stats` for optimal results, although `    ansible.builtin.set_fact` will continue to be supported.(AAP-46841)


#### 10.6.9.2. Enhancements




- Previously, when a project `    url/branch/scm_refspec` was edited, users had to manually trigger a project resync through either the UI or API. Now, Event-Driven Ansible automatically does a resync in case one of `    url/branch/scm_refspec` is modified.(AAP-46254)
- Relevant settings and versions are emitted in logs when the worker starts.(AAP-40984)


#### 10.6.9.3. Bug Fixes




- Fixed an issue when using `    gather_facts` in a rulebook a user had to provide an inventory. This is only available when running ansible-rulebook as a CLI. When the rulebook with `    gather_facts` is run as part of Activation the `    gather_facts` is ignored, since Activations does not include inventory.(AAP-47846)
- Fixed an issue where DE images that use an SHA digest in the URI would fail to pull. This is now addressed, enabling user reminders to be sent actively.(AAP-47725)
- Fixed an issue introduced in #1296 where we were running under the advisory lock and not the actual import/sync task, but the proxy that schedules the job for rq and `    dispatcherd` .(AAP-47554)
- Fixed an issue where there were no validations to `    URL` , `    branch/tag/commit` , and `    refspec` fields when creating or updating a project.(AAP-47227)
- Fixed an issue on k8s-based deployments where activations would hang while being deleted or disabled.(AAP-46559)
- Fixed an issue where the activation could get stuck in the **disabling** or **deleting** state under OpenShift Container Platform.(AAP-45298)


