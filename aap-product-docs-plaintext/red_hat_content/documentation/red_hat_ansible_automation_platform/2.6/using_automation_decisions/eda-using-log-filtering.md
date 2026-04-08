# 8. Rulebook activations troubleshooting
## 8.1. Event-Driven Ansible log filtering
### 8.1.1. Using log filtering for troubleshooting




Learn to filter logs using specialized tracking identifiers for efficient troubleshooting of activation issues and API request lifecycles.

**Procedure**

1.  **Collect identifiers:**


1. When an issue occurs, retrieve the **Log Tracking ID** ( `        tid` ) from the failed activation instance’s logs in the UI **History tab** .
1. If the issue was triggered by a user action (like restarting an activation), obtain the **X-REQUEST-ID** ( `        rid` ) from the HTTP response headers.

1.  **Search system logs:**


1. Use the collected UUID to search through your backend logs (worker, scheduler, API, and the like.). This filters out irrelevant noise, allowing you to focus on the full timeline of the specific request or activation across all services.

1.  **Correlate timeline:**


1. Use the common `        tid` to follow the activation’s progress (or failure) across different log files and services.

1.  **Use support tools:**


1. If necessary, use `        sosreport` or `        mustgather` tools, which automatically collect all relevant Event-Driven Ansible logs from `        /var/log/ansible-automation-platform/eda/` .



