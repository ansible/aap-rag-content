# Enforce project integrity with signing and verification
## Sign content in automation projects
### Automate signing

In environments with highly-trusted *Continuous Integration* (CI) environments such as OpenShift or Jenkins, it is possible to automate the signing process.

For example, you can store your GPG private key in a CI platform of choice as a secret, and import that into GnuPG in the CI environment. You can then run through the signing workflow within the normal CI environment.

When signing a project by using GPG, the environment variable `ANSIBLE_SIGN_GPG_PASSPHRASE` can be set to the passphrase of the signing key. This can be injected and masked or secured in a CI pipeline.

Depending on the scenario, `ansible-sign` returns with a different exit-code, during both signing and verification. This can also be useful in the context of CI and automation, as a CI environment can act differently based on the failure. For example, it can send alerts for some errors, but fail silently for others.

These are the current exit codes used in `ansible-sign`, which can be considered stable:

| Exit code | Approximate meaning                | Example scenarios                                                                                                                                                                                |
| --------- | ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| <br>0     | <br>Success                        | Signing was successfulVerification was successful                                                                                                                                                |
| <br>1     | <br>General failure                | The checksum manifest file contained a syntax error during verificationThe signature file did not exist during verification`MANIFEST.in` did not exist during signing                            |
| <br>2     | <br>Checksum verification failure  | The checksum hashes calculated during verification differed from what was in the signed checksum manifest, for example, a project file was changed but the signing process was not re-completed. |
| <br>3     | <br>Signature verification failure | The signer’s public key was not in the user’s GPG keyringThe wrong GnuPG home directory or keyring file was specifiedThe signed checksum manifest file was modified in some way                  |
| <br>4     | <br>Signing process failure        | The signer’s private key was not found in the GPG keyringThe wrong GnuPG home directory or keyring file was specified                                                                            |
