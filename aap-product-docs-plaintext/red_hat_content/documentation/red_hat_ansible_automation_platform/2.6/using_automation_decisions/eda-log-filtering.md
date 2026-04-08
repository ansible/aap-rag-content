# 8. Rulebook activations troubleshooting
## 8.1. Event-Driven Ansible log filtering




Event-Driven Ansible includes tracking identifiers in all log output to significantly improve troubleshooting. These identifiers help track user actions and activation processes across multiple services and log files.


<span id="idm139919145896464"></span>
**Table 8.1. Event-Driven Ansible log tracking IDs**

| Identifier | Abbreviation | Purpose | Location |
| --- | --- | --- | --- |
|  **X-REQUEST-ID** |  `rid` | Tracks HTTP requests from the platform gateway through the entire Event-Driven Ansible request lifecycle. Use this to correlate UI actions or API calls with backend processing. | Included in the HTTP response headers and Event-Driven Ansible log entries. |
|  **Log Tracking ID** |  `tid` | Tracks the **activation lifecycle** from creation through completion, persisting across restarts and multiple log files. | Included in all activation-related log entries. It can be obtained from the activation **History** tab in the UI. |
|  **Activation Instance ID** |  `aiid` | Identifies the logs specific to a single execution instance of a rulebook activation, allowing you to view `ansible-rulebook` output for that run. | Included in activation logs. |




Note
Not all processes originate from a user or external client. When an Event-Driven Ansible orchestrator internally triggers a process (for example, a monitor request), the `rid` UUID is generated internally to track that process lifecycle and will not be present in the platform gateway logs.



The enhanced log format places these identifiers at the start of the message, making them easy to filter:

`[rid: &lt;UUID&gt;] [tid: &lt;UUID&gt;] [aiid: &lt;ID&gt;] aap_eda.tasks.orchestrator Processing request…​`


