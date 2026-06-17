# Red Hat Lightspeed credential type

Select this credential type to enable synchronization of cloud inventory with Red Hat Lightspeed.

Red Hat Lightspeed credentials are the Red Hat Lightspeed **Username** and **Password**, which are the user’s Red Hat Customer Portal Account username and password.

The `extra_vars` and `env` injectors for Red Hat Lightspeed are as follows:

```
ManagedCredentialType(
namespace='insights',
....
....
....

injectors={
'extra_vars': {
"scm_username": "{{username}}",
"scm_password": "{{password}}",
},
'env': {
'INSIGHTS_USER': '{{username}}',
'INSIGHTS_PASSWORD': '{{password}}',
},
```
