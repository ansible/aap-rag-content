# 2. Ansible Automation Platform synchronization configuration reference
## 2.3. Filter Options




The following filter options apply only to Job Template synchronization.

The `surveyEnabled` filter accepts one of the following values:

- Omitted: Sync **all** Job Templates, regardless of their Ansible Automation Platform Survey status.
-  `    true` : Sync **only** Job Templates that have Ansible Automation Platform Surveys enabled.
-  `    false` : Sync **only** Job Templates that do **not** have Ansible Automation Platform Surveys enabled.


The `labels` filter accepts an array of strings:

-  `    []` (empty array) or omitted: Sync **all** Job Templates, regardless of associated Ansible Automation Platform Labels.
- ["label1", "label2"]: Sync **only** Job Templates that have **any** of the specified Ansible Automation Platform Labels ( **OR** logic).
- Label matching is case-insensitive.


