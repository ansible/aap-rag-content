# 9. Logging and Aggregation
## 9.3. API 4XX error configuration




When the API encounters an issue with a request, it typically returns an HTTP error code in the 400 range along with an error. When this happens, an error message is generated in the log that follows the following pattern:

```
' status {status_code} received by user {user_name} attempting to access {url_path} from {remote_addr} '
```

These messages can be configured as required. Use the following procedure to modify the default API 4XX errors log message format.

**Procedure**

1. From the navigation panel, selectSettings→Automation Execution→Logging.
1. On the **Logging settings** page, clickEdit.
1. Modify the field **Log Format For API 4XX Errors** .

Items surrounded by `    {}` are substituted when the log error is generated.


1. The following variables can be used:


-  **status_code** : The HTTP status code the API is returning.
-  **user_name** : The name of the user that was authenticated when making the API request.
-  **url_path** : The path portion of the URL being called (the API endpoint).
-  **remote_addr** : The remote address received by automation controller.
-  **error** : The error message returned by the API or, if no error is specified, the HTTP status as text.



