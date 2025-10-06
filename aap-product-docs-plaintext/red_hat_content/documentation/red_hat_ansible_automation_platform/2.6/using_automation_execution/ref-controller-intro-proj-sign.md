# 12. Project Signing and Verification
## 12.1. About project signing




For project maintainers, the supported way to sign content is to use the `ansible-sign` utility, using the _command-line interface_ (CLI) supplied with it.

The CLI aims to make it easy to use cryptographic technology such as _GNU Privacy Guard_ (GPG) to validate that files within a project have not been tampered with in any way. Currently, GPG is the only supported means of signing and validation.

Automation controller is used to verify the signed content. After a matching public key has been associated with the signed project, automation controller verifies that the files included during signing have not changed, and that files have been added or removed unexpectedly. If the signature is not valid or a file has changed, the project fails to update, and jobs making use of the project will not launch. Verification status of the project ensures that only secure, untampered content can be run in jobs.

If the repository has already been configured for signing and verification, the usual workflow for altering the project becomes the following:

1. You have a project repository set up already and want to make a change to a file.
1. You make the change, and run the following command:


```
ansible-sign project gpg-sign /path/to/project
```

This command updates a checksum manifest and signs it.


1. You commit the change, the updated checksum manifest, and the signature to the repository.


When you synchronize the project, automation controller pulls in the new changes, checks that the public key associated with the project in automation controller matches the private key that the checksum manifest was signed with (this prevents tampering with the checksum manifest itself), then re-calculates the checksums of each file in the manifest to ensure that the checksum matches (and thus that no file has changed). It also ensures that all files are accounted for:

Files must be included in, or excluded from, the `MANIFEST.in` file. For more information on this file, see [Sign a project](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/using_automation_execution/assembly-controller-project-signing#con-controller-signing-your-project) . If files have been added or removed unexpectedly, verification fails

![Content signing proedure](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.6-Using_automation_execution-en-US/images/9c1e44ccc1bfd7e750a47025ad99c0d0/content-sign-diagram.png)


