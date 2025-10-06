# 2. Ansible Automation Platform containerized installation
## 2.7. Advanced configuration options
### 2.7.5. Enabling automation content collection and container signing




Automation content signing is disabled by default. To enable it, the following installation variables are required in the inventory file:

```
# Collection signing
hub_collection_signing=true
hub_collection_signing_key=&lt;full_path_to_collection_gpg_key&gt;

# Container signing
hub_container_signing=true
hub_container_signing_key=&lt;full_path_to_container_gpg_key&gt;
```

The following variables are required if the keys are protected by a passphrase:

```
# Collection signing
hub_collection_signing_pass=&lt;gpg_key_passphrase&gt;

# Container signing
hub_container_signing_pass=&lt;gpg_key_passphrase&gt;
```

The `hub_collection_signing_key` and `hub_container_signing_key` variables require the set up of keys before running an installation.

Automation content signing currently only supports GnuPG (GPG) based signature keys. For more information about GPG, see the [GnuPG man page](https://www.gnupg.org/documentation/manpage.html) .

Note
The algorithm and cipher used is the responsibility of the customer.



**Procedure**

1. On a RHEL server run the following command to create a new key pair for collection signing:


```
gpg --gen-key
```


1. Enter your information for "Real name" and "Email address":

Example output:


```
gpg --gen-key    gpg (GnuPG) 2.3.3; Copyright (C) 2021 Free Software Foundation, Inc.    This is free software: you are free to change and redistribute it.    There is NO WARRANTY, to the extent permitted by law.        Note: Use "gpg --full-generate-key" for a full featured key generation dialog.        GnuPG needs to construct a user ID to identify your key.        Real name: Joe Bloggs    Email address: jbloggs@example.com    You selected this USER-ID:        "Joe Bloggs &lt;jbloggs@example.com&gt;"        Change (N)ame, (E)mail, or (O)kay/(Q)uit? O
```

If this fails, your environment does not have the necessary prerequisite packages installed for GPG. Install the necessary packages to proceed.


1. A dialog box will appear and ask you for a passphrase. This is optional but recommended.
1. The keys are then generated, and produce output similar to the following:


```
We need to generate a lot of random bytes. It is a good idea to perform    some other action (type on the keyboard, move the mouse, utilize the    disks) during the prime generation; this gives the random number    generator a better chance to gain enough entropy.    gpg: key 022E4FBFB650F1C4 marked as ultimately trusted    gpg: revocation certificate stored as '/home/aapuser/.gnupg/openpgp-revocs.d/F001B037976969DD3E17A829022E4FBFB650F1C4.rev'    public and secret key created and signed.        pub   rsa3072 2024-10-25 [SC] [expires: 2026-10-25]          F001B037976969DD3E17A829022E4FBFB650F1C4    uid                      Joe Bloggs &lt;jbloggs@example.com&gt;    sub   rsa3072 2024-10-25 [E] [expires: 2026-10-25]
```

Note the expiry date that you can set based on company standards and needs.


1. You can view all of your GPG keys by running the following command:


```
gpg --list-secret-keys --keyid-format=long
```


1. To export the public key run the following command:


```
gpg --export -a --output collection-signing-key.pub &lt;email_address_used_to_generate_key&gt;
```


1. To export the private key run the following command:


```
gpg -a --export-secret-keys &lt;email_address_used_to_generate_key&gt; &gt; collection-signing-key.priv
```


1. If a passphrase is detected, you will be prompted to enter the passphrase.
1. To view the private key file contents, run the following command:


```
cat collection-signing-key.priv
```

Example output:


```
-----BEGIN PGP PRIVATE KEY BLOCK-----        lQWFBGcbN14BDADTg5BsZGbSGMHypUJMuzmIffzzz4LULrZA8L/I616lzpBHJvEs    sSN6KuKY1TcIwIDCCa/U5Obm46kurpP2Y+vNA1YSEtMJoSeHeamWMDd99f49ItBp        &lt;snippet&gt;        j920hRy/3wJGRDBMFa4mlQg=    =uYEF    -----END PGP PRIVATE KEY BLOCK-----
```


1. Repeat steps 1 to 9 to create a key pair for container signing.
1. Add the following variables to the inventory file and run the installation to create the signing services:


```
# Collection signing    hub_collection_signing=true    hub_collection_signing_key=/home/aapuser/aap/ansible-automation-platform-containerized-setup-&lt;version_number&gt;/collection-signing-key.priv    # This variable is required if the key is protected by a passphrase    hub_collection_signing_pass=&lt;password&gt;        # Container signing    hub_container_signing=true    hub_container_signing_key=/home/aapuser/aap/ansible-automation-platform-containerized-setup-&lt;version_number&gt;/container-signing-key.priv    # This variable is required if the key is protected by a passphrase    hub_container_signing_pass=&lt;password&gt;
```




**Additional resources**

-  [Working with signed containers](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/managing_automation_content/managing-containers-hub#working-with-signed-containers)


