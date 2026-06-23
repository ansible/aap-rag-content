# Enforce project integrity with signing and verification
## About project signing

Automation controller supports content signing for projects to ensure the integrity and authenticity of project files. This feature helps to prevent tampering with project content by ensuring that any changes to files are detected during project synchronization.

For project maintainers, the supported way to sign content is to use the `ansible-sign` utility, using the *command-line interface* (CLI) supplied with it.

The CLI aims to make it easy to use cryptographic technology such as *GNU Privacy Guard* (GPG) to validate that files within a project have not been tampered with in any way. Currently, GPG is the only supported means of signing and validation.

Automation controller is used to verify the signed content. After a matching public key has been associated with the signed project, automation controller verifies that the files included during signing have not changed, and that files have been added or removed unexpectedly. If the signature is not valid or a file has changed, the project fails to update, and jobs making use of the project will not launch. Verification status of the project ensures that only secure, untampered content can be run in jobs.

If the repository has already been configured for signing and verification, the usual workflow for altering the project becomes the following:

1. You have a project repository set up already and want to make a change to a file.

2. You make the change, and run the following command:

```
ansible-sign project gpg-sign /path/to/project
```
This command updates a checksum manifest and signs it.

3. You commit the change, the updated checksum manifest, and the signature to the repository.

When you synchronize the project, automation controller pulls in the new changes, checks that the public key associated with the project in automation controller matches the private key that the checksum manifest was signed with (this prevents tampering with the checksum manifest itself), then re-calculates the checksums of each file in the manifest to ensure that the checksum matches (and thus that no file has changed). It also ensures that all files are accounted for:

Files must be included in, or excluded from, the `MANIFEST.in` file. For more information on this file, see [Sign a project](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-assembly_controller_project_signing#con-controller-signing-your-project "Signing a project involves an Ansible project directory."). If files have been added or removed unexpectedly, verification fails


![Content signing procedure](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/content-sign-diagram.png)

