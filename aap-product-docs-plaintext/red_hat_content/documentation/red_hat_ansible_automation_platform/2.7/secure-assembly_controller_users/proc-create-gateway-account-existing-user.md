# View, create, or assign roles to users
## Create a platform gateway account for an existing user

By creating platform gateway accounts for existing users, you ensure they can continue to access the platform after upgrading. In Ansible Automation Platform 2.7, the automation controller password fallback authentication mechanism is removed.

### Before you begin

- You have platform administrator access.
- The user account already exists in automation controller.

### Procedure

1.  From the navigation panel, select Access Management> (and then)Users.
2.  Click Create user.
3.  Enter the following user information:

- **Username**: Enter the username that matches the automation controller username.
- **Email**: Enter the user's email address.
- **Password**: Set an initial password for the user.

4.  Click Create user.
5.  Notify the user of the new gateway credentials using your organization's secure communication method.

### Results

Log in to platform gateway by using the new user credentials to confirm the account is active.

