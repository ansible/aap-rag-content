# Prepare platform gateway accounts for the 2.7 upgrade

In Red Hat Ansible Automation Platform 2.6, users without a platform gateway account can authenticate using an automation controller password. In Ansible Automation Platform 2.7, this fallback authentication mechanism is removed.

## About this task

Important:

You must configure platform gateway accounts for all users before upgrading. Users cannot authenticate after the upgrade if they rely on the automation controller password fallback.

## Procedure

1.  Identify users who authenticate through the automation controller password fallback.
2.  Create platform gateway accounts for these users or instruct users to set platform gateway passwords.

Note:
If you miss this step before upgrading, automation controller accounts are automatically created in platform gateway during the upgrade, but passwords are not set. Users with automatically-created accounts must reset their passwords before they can log in.

## Results

Confirm that all active users can log in to their platform gateway accounts.
