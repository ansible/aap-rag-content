# Troubleshoot automation dashboard configuration and deployment
## Issue 3: Date range and currency selectors not working (UI features missing)

**Symptom**

- Cannot select custom date ranges in dashboard UI
- Date range selector shows only predefined options (or is missing entirely)
- Cannot change currency in dashboard settings
- All cost values display in USD only


**Root cause**

Custom date range selection and currency selector features are not implemented in Ansible Automation Platform 2.7 Technology Preview dashboard UI.

**Impact**

**Technology Preview Limitations:**

- **Date filtering:** Users can only use predefined date range options (Last 7 days, Last 30 days, Last 90 days, etc.)
- **Currency:** All cost values display in USD. Multi-currency support not available.


**Solution**

**Workaround:**

No workaround is available for Technology Preview.

Important:

**Date range filtering (Technology Preview limitation):**

In Ansible Automation Platform 2.7 Technology Preview, dashboard supports the following predefined date ranges:

- Last 7 days
- Last 30 days
- Last 90 days


Custom date range selection (choosing specific start and end dates) is not available in Technology Preview.

Important:

**Cost currency (Technology Preview limitation):**

In Ansible Automation Platform 2.7 Technology Preview, all dashboard cost values display in USD ($). Currency selection and multi-currency support are not available in Technology Preview.

