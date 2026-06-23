# Understand secret handling

Automation controller manages three sets of secrets:

- User passwords for local automation controller users.
- Secrets for automation controller operational use, such as database password or message bus password.
- Secrets for automation use, such as SSH keys, cloud credentials, or external password vault credentials.


Note:

You must have 'local' user access for the following users:

- postgres
- awx
- redis
- receptor
- nginx

