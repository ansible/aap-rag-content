# Audit email address modifications

Use the detect_changed_emails management command to identify users whose email addresses have been modified. The command analyzes audit data from the activity stream and compares it against current user records.

## About this task

The command does not attribute changes to specific causes. It provides data for you to investigate changes that might require further action.

## Procedure

1.  Run the following command to list email changes recorded in the activity stream:


```
$ aap-gateway-manage detect_changed_emails
```

2.  Optional: To run a full security audit that includes authenticator linkage checks, duplicate email detection, and high-risk scoring, add the `--audit` flag:


```
$ aap-gateway-manage detect_changed_emails --audit
```

3.  Review the output and investigate any accounts where the email address does not match the expected owner based on your organization's directory, the account has elevated RBAC permissions, the email change occurred shortly before a new identity provider login, or the account has both local and external authenticators linked.
