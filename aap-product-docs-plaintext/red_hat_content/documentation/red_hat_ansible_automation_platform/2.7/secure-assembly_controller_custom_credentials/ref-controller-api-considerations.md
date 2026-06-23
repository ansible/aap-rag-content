# Custom credential types
## Backwards-compatible API considerations

When using the automation controller API, there are some considerations to remember regarding backwards compatibility between version 1 (`api/v1/`) and version 2 (`api/v2/`).

Support for version 2 of the API (`api/v2/`) means a one-to-many relationship for job templates to credentials (including multicloud support).

You can filter credentials the v2 API:

```
curl "https://controller.example.org/api/v2/credentials/?credential_type__namespace=aws"
```
In the V2 Credential Type model, the relationships are defined as follows:

| Machine      | SSH                                                                 |
| ------------ | ------------------------------------------------------------------- |
| <br>Vault    | <br>Vault                                                           |
| <br>Network  | <br>Sets environment variables, for example `ANSIBLE_NET_AUTHORIZE` |
| <br>SCM      | <br>Source Control                                                  |
| <br>Cloud    | <br>EC2, AWS                                                        |
| <br>Cloud    | <br>Many others                                                     |
| <br>Insights | <br>Insights                                                        |
| <br>Galaxy   | <br>galaxy.ansible.com, console.redhat.com                          |
| <br>Galaxy   | <br>on-premise automation hub                                       |

