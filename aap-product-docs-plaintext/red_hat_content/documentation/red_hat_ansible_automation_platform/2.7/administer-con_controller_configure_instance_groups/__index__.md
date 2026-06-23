# Configure instance groups from the API

You can configure instance groups in automation controller using the REST API.

You can create instance groups by POSTing to `/api/v2/instance_groups` as a system administrator.

Once created, you can associate instances with an instance group by using:

```
HTTP POST /api/v2/instance_groups/x/instances/ {'id': y}`
```
An instance that is added to an instance group automatically reconfigures itself to listen on the group’s work queue. For more information, see Instance group policies.

