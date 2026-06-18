# General changes

In Ansible Automation Platform 2.5 and later, API endpoints across components changed with the addition of platform gateway.

| Component                 | 2.4 and earlier endpoints start with… | 2.5 and later endpoints start with… | Notes                                                                                                   |
| ------------------------- | ------------------------------------- | ----------------------------------- | ------------------------------------------------------------------------------------------------------- |
| <br>Automation controller | <br> `/api/v2/`                       | <br> `/api/controller/v2/`          |                                                                                                         |
| <br>Automation hub        | <br> `/api/automation-hub`            | <br> `/api/galaxy/v1`               | <br>This is the default path, but this path can be changed. For example: `https://<local_hub_URL>/api/` |
| <br>Platform gateway      | <br>Not applicable                    | <br> `/api/gateway/v1/`             |                                                                                                         |
| <br>Event-Driven Ansible  | <br>Not applicable                    | <br> `/api/eda/v1/`                 |                                                                                                         |
