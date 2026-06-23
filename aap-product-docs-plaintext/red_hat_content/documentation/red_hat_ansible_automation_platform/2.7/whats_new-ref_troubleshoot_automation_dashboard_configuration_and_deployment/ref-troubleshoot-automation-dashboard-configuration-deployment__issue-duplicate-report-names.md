# Troubleshoot automation dashboard configuration and deployment
## Issue 4: Duplicate saved report names allowed

**Symptom**

- Creating a saved report (filter set) with an existing name succeeds
- No warning or error message displayed
- No overwrite confirmation dialog
- Results in two different reports with identical names in the list


**Root cause**

Dashboard does not validate saved report names for uniqueness. The system allows multiple reports with the same name, relying on internal IDs to differentiate them.

**Impact**

User confusion when multiple reports have the same name. Users must open each report to see its filter configuration to determine which is which.

**Solution**

**Workaround:**

Use unique, descriptive names for all saved reports. Include identifying information in the name.

**Best practices:**

- **Good:** "Q1-2026-Production-Org", "Weekly-Template-Usage", "EMEA-Region-ROI"
- **Avoid:** "Test Report", "My Report", "Dashboard" (too generic, likely to duplicate)


**Recommended naming convention:**

```
[Purpose]-[Timeframe/Scope]-[Date Created]

Examples:
- Compliance-Audit-Last-90-Days-2026-04-27
- Executive-Summary-Q1-2026
- Development-Org-Weekly-Usage
```
**Managing duplicate names**

If you have multiple reports with the same name:

1.      **Identify each report:**

- Open each report with duplicate name
- Note the filter configuration
- Determine purpose/owner

2.      **Rename to unique names:**

- Update each report with descriptive unique name
- Save changes

3.      **Delete unwanted duplicates:**

- Remove any obsolete or test reports

**Verification**

Expected behavior:

- Attempting to save report with existing name triggers warning
- User can choose to overwrite or rename
- System prevents unintentional duplicates

