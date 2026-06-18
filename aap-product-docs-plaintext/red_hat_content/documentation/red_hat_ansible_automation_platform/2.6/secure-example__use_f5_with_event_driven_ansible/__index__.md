# Example: Use F5 with Event-Driven Ansible

Use F5 with Event-Driven Ansible to watch for events and trigger a rulebook based on F5 monitoring logs.

## About this task

Example code using F5 and Event-Driven Ansible is available on GitHub. This code notes each instance of the watcher finding a match in its filter and then copies the source IP from that code into a CSV list. The list is then sent as a variable within the webhook along with the message to execute the code, as described in the high level workflow.

![](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/f5-and-ansible.png)

## Procedure

1.  The F5 BIGIP pushes the monitoring logs to Elastic.
2.  Elastic takes that data and stores it while using a watcher with its filters and criteria.
3.  The Watcher detects an event that matches its criteria and sends the webhook with pauload to Event-Driven Ansible.
4.  From the event, the Event-Driven Ansible rulebook triggers a job template within Ansible Automation Platform, which sends the payload provided by Elastic.
5.  An Ansible Automation Platform template executes a playbook to secure the F5 BIG-IP using the payload provided by Event-Driven Ansible (originally provided by Elastic).

## Drive responses from logging events

Ansible validated content provides pre-tested, trusted Roles and playbooks for secure, consistent infrastructure management. Use this content out-of-the-box to reduce the time needed for custom development, such as automating Event-Driven Ansible’s response to log events.

## Use case: AWS CloudTrail

Configure Event-Driven Ansible rulebooks to automatically monitor and secure your AWS CloudTrail logs. Triggering actions to re-enable encryption or restore deleted trails helps ensure your sensitive data remains protected and compliant.

AWS CloudTrail is a service that logs all the API calls made in your AWS account, including API calls made by other AWS services. By default, CloudTrail logs are stored in an S3 bucket in an unencrypted form. To verify that your CloudTrail logs are secure, enable encryption for CloudTrail logs using AWS KMS. Enable encryption for CloudTrail logs by creating a KMS key that is used to encrypt the S3 bucket where your CloudTrail logs are stored. Then configure CloudTrail to use this key to encrypt the logs.

With encryption enabled, all CloudTrail logs are automatically encrypted when they are written to the S3 bucket. The logs can only be decrypted using the KMS key that you specified. This establishes that your logs are secure and can only be accessed by authorized users and services.

Encrypting AWS CloudTrail logs is important for several reasons:

- Protection of sensitive information: CloudTrail logs contain a wealth of information about the AWS account, including API calls, user identities, and resource information. Encrypting CloudTrail logs helps protect this sensitive information from unauthorized access or tampering.
- Compliance requirements: Many compliance standards, such as HIPAA and PCI DSS, require log encryption to protect sensitive information. Encrypting CloudTrail logs enables compliance with these standards.
- Prevent tampering: CloudTrail’s log encryption helps prevent logs from being tampered with. This helps maintain log integrity and an accurate record of all API calls made to your AWS account.
- Secure data: CloudTrail log’s encryption provides an additional layer of security for data. In the event that your S3 bucket is compromised, the encrypted logs cannot be accessed without the encryption key.


The Event-Driven Ansible rulebook is comprised of the following components to assist in actions on the log files:

- **Sources**: define which event source will be used
- **Rules**: define which conditionals will be matched from the event source
- **Actions**: trigger events when conditions are met


In the following example, the rulebook implements a ruleset with three rules as follows:

**Rule #1: Enable trail encryption**

This rule handles the case when trail encryption is disabled. It is triggered when an UpdateTrail operation is performed on the trail and the parameters contained in the UpdateTrail request match these conditions:

`event.CloudTrailEvent.requestParameters.kmsKeyId==""` AND `event.CloudTrailEvent.requestParameters.name==vars.cloudtrail_name.`

The action that is taken to mitigate this drift will run the

'playbooks/eda/aws_restore_cloudtrail_encryption.yml playbook` This playbook runs the Ansible validated role `cloud.aws_ops.enable_cloudtrail_encryption_with_kms` that re-enables the trail’s encryption, restoring the system to its status quo.

**Rule#2: Re-create the trail**

This rule handles the case when the trail is deleted.

When the following conditions are met:

`event.CloudTrailEvent.eventName=="DeleteTrail"` AND `event.CloudTrailEvent.requestParameters.name==vars.cloudtrail_name`

The action is running the `playbooks/eda/aws_restore_cloudtrail.yml` playbook. This playbook runs the Ansible validated content `cloud.aws_ops.awsconfig_multiregion_cloudtrail` role first, which re-creates the trail and then the `cloud.aws_ops.enable_cloudtrail_encryption_with_kms` role, to enable the encryption on the newly created trail.

**Rule#3: Cancels the deletion of the KMS key and re-enables it**

This rule responds to the case of a KMS key being deleted or disabled. This results in the condition

`event.CloudTrailEvent.eventName=="ScheduleKeyDeletion"` OR `event.CloudTrailEvent.eventName=="DisableKey"`

When someone attempts to delete a KMS key intentionally or accidentally, a `ScheduleKeyDeletion` event is displayed in AWS CloudTrail. The KMS key is not deleted immediately, because deleting a KMS key is destructive and potentially dangerous. AWS KMS requires setting a 7–30 day waiting period. This situation is handled promptly by running playbooks/eda/aws_restore_kms_key.yml playbook, which cancels the deletion of the KMS key. Similarly, when the KMS key is disabled, the playbook reactivates it to restore the original state of the system. The playbook sets the KMS key ARN and uses it to determine whether to cancel the KMS key deletion, to re-enable the KMS key, or both.

Ansible validated content for cloud.aws_ops and Event-Driven Ansible create many opportunities for automated issue resolution and observation of cloud computing environments, helping you to easily automate, mitigate security issues, and maximize your mastery of cloud environments. For more information on using rulebooks, see [Validated content for Event-Driven ansible for AWS](https://www.redhat.com/en/blog/ansible-validated-content-with-event-driven-ansible#:~:text=Event%2DDriven%20Ansible%20refers%20to,application%20failures%2C%20or%20security%20breaches).
