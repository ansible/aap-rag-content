# Filter events before triggering automation

Events sometimes have extra data that is unnecessary and might overwhelm the rule engine. Use event filters to remove that extra data so you can focus on what matters to your rules. Event filters might also change the format of the data so that the rule conditions can better match the data.

Events are defined as python code and distributed as collections. The default EDA collection has the following filters:

| Name                                    | Description                                                                                                      |
| --------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| <br>json\_filter                        | <br>This filter includes and excludes keys from the event object                                                 |
| <br>dashes\_to\_underscores             | <br>This filter changes the dashes in all keys in the payload to be underscore                                   |
| <br>ansible.eda.insert\_hosts\_to\_meta | <br>This filter is used to add host information into the event so that ansible-rulebook can locate it and use it |
| <br>ansible.eda.normalize\_keys         | <br>This filter is used if you want to change non alpha numeric keys to underscore                               |


You can chain event filters one after the other, and the updated data is sent from one filter to the next. Event filters are defined in the rulebook after a source is defined. When the rulebook starts the source plugin it associates the correct filters and transforms the data before putting it into the queue.

```
sources:
- name: azure_service_bus
ansible.eda.azure_service_bus:
conn_str: "{{connection_str}}"
queue_name: "{{queue_name}}"
filters:
- json_filter:
include_keys: ['clone_url']
exclude_keys: ['*_url', '_links', 'base', 'sender', 'owner', 'user']
- dashes_to_underscores:
```
In this example the data is first passed through the `json_filter` and then through the `dashes_to_underscores` filter. In the event payload, keys can only contain letters, numbers, and underscores. The period (.) is used to access nested keys.

Since every event should record the origin of the event the filter `eda.builtin.insert_meta_info` is added automatically by ansible-rulebook to add the `source name`, `type`, and `received_at`. The `received_at` stores a date time in UTC ISO8601 format and includes the microseconds. The `uuid` stores the unique id for the event. The `meta key` is used to store metadata about the event and its needed to correctly report about the events in the aap-server.

