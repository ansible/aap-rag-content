# Understand secret handling
## User passwords for local users

Automation controller hashes local automation controller user passwords with the PBKDF2 algorithm by using a SHA256 hash. Users who authenticate by external account mechanisms, such as LDAP, SAML, and OAuth, do not have any password or secret stored.

