# 10. Patch releases
## 10.1. Ansible Automation Platform patch release July 2, 2025
### 10.1.3. Ansible Automation Platform




#### 10.1.3.1. Enhancements




- Refactored `    V1RootView.get()` and improve reverse lookup logic.(AAP-47366)
- Refactored `    process_statuses()` method to reduce its cognitive complexity.(AAP-47341)
- All UI elements related to policy enforcement are visible to all users. See the [policy enforcement documentation](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/configuring_automation_execution/controller-pac) for more information. (AAP-47006)
- On the inventory source form, for a source type of **VMware ESXi** the user will be able to select credentials of type **VMware vCenter** .(AAP-46784)
- Reduced the cognitive complexity of method `    migrate_resource()` in `    migrate_service_data.py` from 56 to < =15.(AAP-45822)
- Reduce the cognitive complexity of the `    process_fields()` method in `    serializers/preference.py` file.(AAP-45820)
- Reduced the cognitive complexity of `    unique_fields_for_model()` method to below 15.(AAP-45819)


#### 10.1.3.2. Bug fixes




- Fixed an issue that did not allow role assignments using `    object_ansible_id` in the `    role_user_assignment` module.(AAP-48042)
- Fixed an issue that did not allow the `    object_id` field in the `    role_user_assignment` module to accept a list of items.(AAP-47979)
- Fixed an example task in the `    ansible.platform.token` module.(AAP-47976)
- Fixed an issue to `    aap_*` parameters in `    ansible.platform.token` module that resulted in user reminders not being sent out.(AAP-47975)
- Fixed an API error messaging in the event a user logs in as the admin user via legacy **auth** on one component, then tries to do so via the other component.(AAP-47541)
- Fixed an issue where API records could be missing or duplicated across pages.(AAP-47504)
- Fixed a bug that was causing the UI to throw an error when launching a workflow job template with both **Prompt on Launch** and **Survey** enabled.(AAP-46813)
- Fixed an issue where the platform gateway **OpenAPI** schema file was not being generated correctly.(AAP-46639)
- Fixed an issue where modules in the `    ansible.platform` collection did not accept `    AAP_*` variable for authentication.(AAP-45363)
- Fixed an issue where there was a missing option in the ansible.platform.user module to allow setting the `    is_platform_auditor` flag on a user.(AAP-45244)
- Fixed an issue where an extra validation to handle incorrect user input in the variables field was needed, as the API did not return an error for it.(AAP-42563)
- Fixed an issue with the **Hosts** links in the **Resource Counts** section of the overview page to redirect to the **Hosts** page, filtered by either **Show only ready hosts** or **Show only failed hosts** depending on which count was clicked on.(AAP-42288)
- Fixed an issue where API records could be missing or duplicated across pages.(AAP-41842)


