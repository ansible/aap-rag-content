# 10. Patch releases
## 10.8. Ansible Automation Platform patch release March 26, 2025
### 10.8.1. General




- The `    ansible.controller` collection has been updated to 4.6.10.(AAP-42242)
- Service account support has been integrated into Ansible Automation Platform Analytics; service account credentials have replaced basic auth credentials when linking to Analytics.(AAP-39472)


- For more information, see the KCS article [Configure Ansible Automation Platform to use service account credentials for authentication.](https://access.redhat.com/articles/7112649)



#### 10.8.1.1. Deprecated




- Deprecated and suppressed the warning about `    ANSIBLE_COLLECTIONS_PATHS` in the job output.(AAP-41566)


