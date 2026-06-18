# User and external authentication mapping

Ansible Automation Platform manages user accounts and synchronizes attributes by centralizing user identification around a matching email address. You can sign in with existing accounts from different sources while maintaining a consistent user profile and access permissions.

Warning:

The platform accepts email claims from identity providers without verifying email ownership. Before you configure an external authenticator, verify that your identity provider enforces email verification and restricts self-service email changes.

When you log in to the platform for the first time with an authenticator, such as Local, GitHub, SAML, or LDAP, the platform evaluates the username and email address. If a single email match exists, the platform links the external identity to that existing account.

- Subsequent logins with the same authenticator and external Unique Identifier (UID) directly sign the user into their linked account.
- If a user's external UID changes, the system re-triggers the email-based linking logic. If the new UID's email matches the existing account, the new authenticator is linked. If the email does not match or is not provided, a new user account might be created.
- If a user's external email changes, the platform does not automatically update the email address in the existing account, but the user can still sign in and a new account with the new email is created for the user.


If a user has a hashed account, such as `bob-hash`, due to a username collision from a previous version, that association is honored for that authenticator. However, for new authentications from other identity providers, the platform maps to the user's primary account, such as `bob`, provided a single matching email exists. This consolidates user identities and prevents the creation of new hashed accounts. If users should have been previously merged, you can delete the user-<hash> account from Ansible Automation Platform and on a subsequent login, the users are merged based on emails as described above.

Important:

- **Authenticators without email**: If an authenticator such as RADIUS or TACACS+ does not return an email address, a new account is created on first sign-in. To ensure consistent future access, manually add an email to the account after creation.
- **Multiple users with the same email**: If an email from an authenticator matches multiple existing platform accounts, the sign-in process fails.
- **LDAP usernames**: The platform treats LDAP usernames as case-insensitive. It converts the username to lowercase and stores it in the database.
- `associated_authenticators` field: The `associated_authenticators` field in the API supports multiple UIDs per user.
