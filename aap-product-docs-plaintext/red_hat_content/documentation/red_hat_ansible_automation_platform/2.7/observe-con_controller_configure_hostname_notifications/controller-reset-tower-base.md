# Advanced notification settings
## Reset TOWER_URL_BASE

Automation controller determines how the base URL (`TOWER_URL_BASE`) is defined by looking at an incoming request and setting the server address based on that incoming request.

### About this task

Automation controller takes settings values from the database first. If no settings values are found, it uses the values from the settings files. If you post a license by navigating to the automation controller host’s IP address, the posted license is written to the settings entry in the database.

Use the following procedure to reset `TOWER_URL_BASE` if the wrong address has been picked up:

### Procedure

1.  From the navigation panel, select Settings> (and then)System.
2.  Click Edit.
3.  Enter the address in the **Base URL of the service** field for the DNS entry you want to appear in notifications.

