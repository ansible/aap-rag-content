# 1. Red Hat Certified, validated, and Ansible Galaxy content in automation hub
## 1.3. Content signing in private automation hub
### 1.3.4. Configuring Ansible-Galaxy CLI to verify collections




You can configure Ansible-Galaxy CLI to verify collections. This ensures that downloaded collections are approved by your organization and have not been changed after they were uploaded to automation hub.

If a collection has been signed by automation hub, the server provides ASCII armored, GPG-detached signatures to verify the authenticity of `MANIFEST.json` before using it to verify the collection’s contents. You must opt into signature verification by [configuring a keyring](https://docs.ansible.com/ansible/devel/reference_appendices/config.html#galaxy-gpg-keyring) for `ansible-galaxy` or providing the path with the `--keyring` option.

**Prerequisites**

- Signed collections are available in automation hub to verify signature.
- Certified collections can be signed by approved roles within your organization.
- Public key for verification has been added to the local system keyring.


**Procedure**

1. To import a public key into a non-default keyring for use with `    ansible-galaxy` , run the following command.


```
gpg --import --no-default-keyring --keyring ~/.ansible/pubring.kbx my-public-key.asc
```

Note
In addition to any signatures provided by automation hub, signature sources can also be provided in the requirements file and on the command line. Signature sources should be URIs.




1. To verify the collection name provided on the CLI with an additional signature, run the following command:


```
ansible-galaxy collection install namespace.collection    --signature https://examplehost.com/detached_signature.asc    --signature file:///path/to/local/detached_signature.asc --keyring ~/.ansible/pubring.kbx
```

You can use this option multiple times to provide multiple signatures.


1. Confirm that the collections in a requirements file list any additional signature sources following the collection’s signatures key, as in the following example.


```
# requirements.yml    collections:      - name: ns.coll        version: 1.0.0        signatures:          - https://examplehost.com/detached_signature.asc          - file:///path/to/local/detached_signature.asc        ansible-galaxy collection verify -r requirements.yml --keyring ~/.ansible/pubring.kbx
```

When you install a collection from automation hub, the signatures provided by the server are saved along with the installed collections to verify the collection’s authenticity.


1. (Optional) If you need to verify the internal consistency of your collection again without querying the Ansible Galaxy server, run the same command you used previously using the `    --offline` option.


