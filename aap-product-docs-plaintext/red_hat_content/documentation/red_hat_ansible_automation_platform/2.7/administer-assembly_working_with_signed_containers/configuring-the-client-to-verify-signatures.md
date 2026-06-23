# Secure your automation with container signing
## Configure a client to verify signatures

To ensure an execution environment pulled from the remote registry is properly signed, first configure the execution environment with the proper public key in a policy file.

### Before you begin

- The client must have sudo privileges configured to verify signatures.

### Procedure

1.  Open your terminal and use the following command:


```
sudo <name of editor> /etc/containers/policy.json
```
The file that is displayed is similar to this:

```
{
"default": [{"type": "reject"}],
"transports": {
"docker": {
"quay.io": [{"type": "insecureAcceptAnything"}],
"docker.io": [{"type": "insecureAcceptAnything"}],
"<server-address>": [
{
"type": "signedBy",
"keyType": "GPGKeys",
"keyPath": "/tmp/containersig.txt"
}]
}
}
}
```
This file shows that neither `quay.io`, or `docker.io` will perform the verification, because the type is `insecureAcceptAnything` which overrides the default type of `reject`. However, `<server-address>` will perform the verification, because the parameter `type` is set to `"signedBy"`.

Note:
The only `keyType` currently supported is GPG keys.

2.  Under the `<server-address>` entry, modify the `keyPath` <1> to include the name of your key file.

```
{
"default": [{"type": "reject"}],
"transports": {
"docker": {
"quay.io": [{"type": "insecureAcceptAnything"}],
"docker.io": [{"type": "insecureAcceptAnything"}],
"<server-address>": [{
"type": "signedBy",
"keyType": "GPGKeys",
"keyPath": "/tmp/<key file name>",
"signedIdentity": {
"type": "matchExact"
}
}]
}
}
}
```

3.  Save and close the file.

### Results

- Pull the file using Podman, or your client of choice:

```
podman pull <server-address>/<container-name>:<tag name> --tls-verify=false
```
This response verifies the execution environment has been signed with no errors. If the execution environment is not signed, the command fails.
