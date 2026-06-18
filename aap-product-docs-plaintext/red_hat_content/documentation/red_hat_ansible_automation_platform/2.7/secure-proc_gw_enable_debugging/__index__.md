# Enable debugging for enterprise authentication

To further diagnose authentication issues, enable debug logging in platform gateway.

## Procedure

1.  Change the logging configuration in the platform gateway’s `settings.py` file.
2.  Set the logging level for the `ansible_base` logger to `DEBUG`:


```
LOGGING['loggers']['ansible_base']['level'] = 'DEBUG'
```
After this change, detailed `AuthTokenError` messages are displayed in the logs, providing specific information about the cause of the failure.
