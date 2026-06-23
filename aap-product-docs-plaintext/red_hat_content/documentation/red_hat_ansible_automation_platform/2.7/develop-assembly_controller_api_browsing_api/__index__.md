# Browse the REST API

Access and use the platform gateway REST API through a web browser. You can find the recommended current version (v2), view documentation for endpoints, and use GET, PUT, and POST methods with JSON formatting.

## Procedure

1.  Go to the REST API in a web browser at:
`https://<gateway server name>/api/controller/v2`

2.  Click the **v2** link next to **current versions** or **available versions**.
The API supports version 2.

3.  Perform a `GET` with the `/api/` endpoint to get the `current_version`, which is the recommended version.
4.  Click the question mark icon on the navigation menu for documentation on the access methods for that particular API endpoint and what data is returned when using those methods.
5.  Use the `PUT` and `POST` verbs on the specific API pages by formatting JSON in the various text fields.

Note:
You can also view changed settings from factory defaults at the `/api/gateway/v1/settings/` endpoint. It reflects changes you made in the API browser, not changed settings that come from static settings files.

