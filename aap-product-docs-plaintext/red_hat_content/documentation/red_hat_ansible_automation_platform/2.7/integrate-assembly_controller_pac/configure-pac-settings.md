# Implement policy enforcement
## Configure policy enforcement settings

You can specify how your Ansible Automation Platform instance interacts with OPA by modifying your global settings.

### Before you begin

- To configure policy enforcement, you must have administrative privileges.


Note:

If you do not configure the OPA server in your policy settings, policy evaluation will not occur when you run the job.

### Procedure

1.  From the navigation panel, select Settings> (and then)Automation Execution> (and then)Policy.
2.  Click **Edit policy settings**.
3.  On the Policy Settings page, fill out the following fields:


OPA Server hostname
Enter the name of the host that connects to the OPA service.

OPA server port
Enter the port that connects to the OPA service.

OPA authentication type
Select the OPA authentication type.

OPA custom authentication header
Enter a custom header to append to request headers for OPA authentication.

OPA request timeout
Enter the number of seconds until the connection times out.

OPA request retry count
Enter a figure for the number of times a request can attempt to connect to the OPA service before failing.

4.  Depending on your authentication type, you might need to fill out the following fields.   1.  If you selected Token as your authentication type:


OPA authentication token
Enter the OPA authentication token.

2.  If you selected Certificate as your authentication type:


OPA client certificate content
Enter content of the CA certificate for mTLS authentication.

OPA client key content
Enter the client key for mTLS authentication.

OPA CA certificate content
Enter the content of the CA certificate for mTLS authentication.

5.  Beneath the heading labeled **Options**:


Use SSL for OPA connection
Check this box to enable an SSL/TLS connection to the OPA service.

6.  Click Save policy settings.

