# 5. Configuring Red Hat Ansible Automation Platform components on Red Hat Ansible Automation Platform Operator
## 5.3. Configuring automation hub on Red Hat OpenShift Container Platform web console
### 5.3.7. Configuring content signing for Ansible Automation Platform Hub Operator




As an automation administrator for your organization, you can configure Ansible Automation Platform Hub Operator for signing and publishing Ansible content collections from different groups within your organization.

For additional security, automation creators can configure Ansible-Galaxy CLI to verify these collections to ensure that they have not been changed after they were uploaded to automation hub.

To successfully sign and publish Ansible Certified Content Collections, you must configure private automation hub for signing.

**Prerequisites**

- A GPG key pair. If you do not have one, you can generate one using the `    gpg --full-generate-key` command.
- Your public-private key pair has proper access for configuring content signing on Ansible Automation Platform Hub Operator.


**Procedure**

1. Create a ConfigMap for signing scripts. The ConfigMap you create contains the scripts used by the signing service for collections and container images.

Note
This script is used as part of the signing service and must generate an ascii-armored detached `    gpg` signature for that file using the key specified through the `    PULP_SIGNING_KEY_FINGERPRINT` environment variable.



The script prints out a JSON structure with the following format.


```
{"file": "filename", "signature": "filename.asc"}
```

All the file names are relative paths inside the current working directory. The file name must remain the same for the detached signature.

**Example:** The following script produces signatures for content:


```
apiVersion: v1    kind: ConfigMap    metadata:      name: signing-scripts    data:      collection_sign.sh: |-          #!/usr/bin/env bash              FILE_PATH=$1          SIGNATURE_PATH=$1.asc              ADMIN_ID="$PULP_SIGNING_KEY_FINGERPRINT"          PASSWORD="password"              # Create a detached signature          gpg --quiet --batch --pinentry-mode loopback --yes --passphrase \            $PASSWORD --homedir /var/lib/pulp/.gnupg --detach-sign --default-key $ADMIN_ID \            --armor --output $SIGNATURE_PATH $FILE_PATH              # Check the exit status          STATUS=$?          if [ $STATUS -eq 0 ]; then            echo {\"file\": \"$FILE_PATH\", \"signature\": \"$SIGNATURE_PATH\"}          else            exit $STATUS          fi      container_sign.sh: |-        #!/usr/bin/env bash            # galaxy_container SigningService will pass the next 4 variables to the script.        MANIFEST_PATH=$1        FINGERPRINT="$PULP_SIGNING_KEY_FINGERPRINT"        IMAGE_REFERENCE="$REFERENCE"        SIGNATURE_PATH="$SIG_PATH"            # Create container signature using skopeo        skopeo standalone-sign \          $MANIFEST_PATH \          $IMAGE_REFERENCE \          $FINGERPRINT \          --output $SIGNATURE_PATH            # Optionally pass the passphrase to the key if password protected.        # --passphrase-file /path/to/key_password.txt            # Check the exit status        STATUS=$?        if [ $STATUS -eq 0 ]; then          echo {\"signature_path\": \"$SIGNATURE_PATH\"}        else          exit $STATUS        fi
```


1. Create a secret for your GnuPG private key. This secret securely stores the GnuPG private key you use for signing.


```
gpg --export --armor &lt;your-gpg-key-id&gt; &gt; signing_service.gpg        oc create secret generic signing-galaxy --from-file=signing_service.gpg
```

The secret must have a key named `    signing_service.gpg` .


1. Configure the AnsibleAutomationPlatform CR.


```
apiVersion: aap.ansible.com/v1alpha1    kind: AnsibleAutomationPlatform    metadata:      name: aap-hub-signing-sample    spec:      hub:        signing_secret: "signing-galaxy"        signing_scripts_configmap: "signing-scripts"
```

**Next steps**

[Using content signing services in private automation hub](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/managing_automation_content/managing-cert-valid-content#proc-using-content-signing-services-in-pah)





