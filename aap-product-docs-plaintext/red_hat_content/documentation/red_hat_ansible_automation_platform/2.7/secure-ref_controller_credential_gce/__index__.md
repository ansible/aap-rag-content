# Google Compute Engine credential type

Select this credential to enable synchronization of a cloud inventory with Google Compute Engine (GCE).

Automation controller uses the following environment variables for GCE credentials:

```
GCE_EMAIL
GCE_PROJECT
GCE_CREDENTIALS_FILE_PATH
```
These are fields prompted in the user interface:

GCE credentials require the following information:

- **Service Account Email Address**: The email address assigned to the Google Compute Engine **service account**.
- Optional: **Project**: Provide the GCE assigned identification or the unique project ID that you provided at project creation time.
- Optional: **Service Account JSON File**: Upload a GCE service account file. Click Browse to browse for the file that has the special account information that can be used by services and applications running on your GCE instance to interact with other Google Cloud APIs. This grants permissions to the service account and virtual machine instances.
- **RSA Private Key**: The PEM file associated with the service account email.
