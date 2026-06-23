# Respond to events from external systems
## Update an event stream with a static UUID (API Method)

Access the API to set a static UUID, a feature critical for maintaining webhook URL consistency across service recreations, such as in disaster recovery scenarios.

### Before you begin

- Ansible Automation Platform 2.6-next

### Procedure

1.  Log in to Ansible Automation Platform.
2.  From the navigation panel, select Overview.
3.  In the URL, replaceOverview with the API endpoint, `api/eda/v1/` (for example, `https://<gateway-host>/api/eda/v1/`). The `Api V1 Root` page displays a list of Event-Driven Ansible resource URLs.

```
{
"config": "http://<gateway-host>/api/eda/v1/config/",
"status": "http://<gateway-host>/api/eda/v1/status/",
"openapi-json": "http://<gateway-host>/api/eda/v1/openapi.json",
"openapi-yaml": "http://<gateway-host>/api/eda/v1/openapi.yaml",
"openapi-docs": "http://<gateway-host>/api/eda/v1/docs/",
"openapi-redoc": "http://<gateway-host>/api/eda/v1/redoc/",
"session-login": "http://<gateway-host>/api/eda/v1/auth/session/login/",
"session-logout": "http://<gateway-host>/api/eda/v1/auth/session/logout/",
"token-refresh": "http://<gateway-host>/api/eda/v1/auth/token/refresh/",
"current-user": "http://<gateway-host>/api/eda/v1/users/me/",
"project-list": "http://<gateway-host>/api/eda/v1/projects/",
"rulebook-list": "http://<gateway-host>/api/eda/v1/rulebooks/",
"activation-list": "http://<gateway-host>/api/eda/v1/activations/",
"activationinstance-list": "http://<gateway-host>/api/eda/v1/activation-instances/",
"auditrule-list": "http://<gateway-host>/api/eda/v1/audit-rules/",
"user-list": "http://<aap.platform>/api/eda/v1/users/",
"controller-token-list": "http://<gateway-host>/api/eda/v1/users/me/awx-tokens/",
"credentialtype-list": "http://<gateway-host>/api/eda/v1/credential-types/",
"edacredential-list": "http://<gateway-host>/api/eda/v1/eda-credentials/",
"credentialinputsource-list": "http://<gateway-host>/api/eda/v1/credential-input-sources/",
"decisionenvironment-list": "http://<gateway-host>/api/eda/v1/decision-environments/",
"organization-list": "http://<gateway-host>/api/eda/v1/organizations/",
"team-list": "http://<gateway-host>/api/eda/v1/teams/",
"eventstream-list": "http://<gateway-host>/api/eda/v1/event-streams/"
```

4.  At the end of the list, click the `eventstream-list` URL. This takes you to the Event Stream List page.
5.  Locate and copy the `“id”` of the event stream UUID that you want to update. This can be found at the end of the event stream data.

```
},
"id": *1*,
"owner": "admin",
"url": "https://<platformURL>/eda-event-streams/api/eda/v1/external_event_stream/bab8dddd-51cc-424f-87a4-0ed8ebe0a755/post/",
"created_at": "2025-11-18T16:30:45.622363Z",
"modified_at": "2025-11-18T16:30:45.622374Z",
"test_content_type": "",
"test_content": "",
"test_error_message": "",
"test_headers": "",
"events_received": 0,
"last_event_received_at": null
```

6.  Paste the id at the end of the URL (for example, `https://<platformURL>.com/api/eda/v1/<id#>`) and press **Enter**. The **Event Stream Instance** page is displayed, including the current `“uuid”` value.
7.  In the form at the end of the **Event Stream Instance** page, update the value of the `“uuid”` field to a unique static string of your choice.
8.  Click **Patch**.

### Results

- Confirm that the UUID of your event stream has been updated to the new static string.

