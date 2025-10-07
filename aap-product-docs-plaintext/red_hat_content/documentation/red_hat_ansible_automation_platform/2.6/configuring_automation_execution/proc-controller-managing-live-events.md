# 3. Performance tuning for automation controller
## 3.7. Automation controller tuning
### 3.7.1. Managing live events in the automation controller UI




Events are sent to any node where there is a UI client subscribed to a job. This task is expensive, and becomes more expensive as the number of events that the cluster is producing increases and the number of control nodes increases, because all events are broadcast to all nodes regardless of how many clients are subscribed to particular jobs.

To reduce the overhead of displaying live events in the UI, administrators can choose to either:

- Disable live streaming events.
- Reduce the number of events shown per second or before truncating or hiding events in the UI.


When you disable live streaming of events, they are only loaded on hard refresh to a job’s output detail page. When you reduce the number of events shown per second, this limits the overhead of showing live events, but still provides live updates in the UI without a hard refresh.

#### 3.7.1.1. Disabling live streaming events




**Procedure**

1. Disable live streaming events by using one of the following methods:


1. In the API, set `        UI_LIVE_UPDATES_ENABLED` to **False** .
1. Go to your automation controller. Open the **Miscellaneous System Settings** window. Set the **Enable Activity Stream** toggle to **Off** .



#### 3.7.1.2. Settings to modify rate and size of events




If you cannot disable live streaming of events because of their size, reduce the number of events that are displayed in the UI. You can use the following settings to manage how many events are displayed:

**Settings available for editing in the UI or API** :

-  `    EVENT_STDOUT_MAX_BYTES_DISPLAY` : Maximum amount of `    stdout` to display (as measured in bytes). This truncates the size displayed in the UI.
-  `    MAX_WEBSOCKET_EVENT_RATE` : Number of events to send to clients per second.


**Settings available by using file based settings** :

-  `    MAX_UI_JOB_EVENTS` : Number of events to display. This setting hides the rest of the events in the list.
-  `    MAX_EVENT_RES_DATA` : The maximum size of the ansible callback event’s "res" data structure. The "res" is the full "result" of the module. When the maximum size of ansible callback events is reached, then the remaining output will be truncated. Default value is 700000 bytes.
-  `    LOCAL_STDOUT_EXPIRE_TIME` : The amount of time before a `    stdout` file is expired and removed locally.


