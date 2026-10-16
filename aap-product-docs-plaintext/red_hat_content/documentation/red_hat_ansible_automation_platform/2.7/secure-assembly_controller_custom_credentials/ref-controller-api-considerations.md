# Custom credential types
## Backwards-compatible API considerations

When using the automation controller API, there are some considerations to remember regarding backwards compatibility between version 1 (`api/v1/`) and version 2 (`api/v2/`).

Support for version 2 of the API (`api/v2/`) means a one-to-many relationship for job templates to credentials (including multicloud support).

You can filter credentials the v2 API:

```
curl "https://controller.example.org/api/v2/credentials/?credential_type__namespace=aws"
```

In the V2 Credential Type model, the relationships are defined as follows:

| Machine  | SSH                                                             |
| -------- | --------------------------------------------------------------- |
| Vault    | Vault                                                           |
| Network  | Sets environment variables, for example `ANSIBLE_NET_AUTHORIZE` |
| SCM      | Source Control                                                  |
| Cloud    | EC2, AWS                                                        |
| Cloud    | Many others                                                     |
| Insights | Insights                                                        |
| Galaxy   | galaxy.ansible.com, console.redhat.com                          |
| Galaxy   | on-premise automation hub                                       |

