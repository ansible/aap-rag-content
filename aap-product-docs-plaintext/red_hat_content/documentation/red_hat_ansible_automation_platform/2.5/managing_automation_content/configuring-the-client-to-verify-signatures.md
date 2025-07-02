# 3. Manage containers in private automation hub
## 3.6. Working with signed containers
### 3.6.7. Configuring the client to verify signatures




To ensure an execution environment pulled from the remote registry is properly signed, you must first configure the execution environment with the proper public key in a policy file.

**Prerequisites**

- The client must have sudo privileges configured to verify signatures.


**Procedure**

1. Open your terminal and use the following command:


```
&gt;  sudo &lt;name of editor&gt; /etc/containers/policy.json
```

The file that is displayed is similar to this:


```
{      "default": [{"type": "reject"}],      "transports": {      	"docker": {        	"quay.io": [{"type": "insecureAcceptAnything"}],        	"docker.io": [{"type": "insecureAcceptAnything"}],        	"&lt;server-address&gt;": [          	{              	    "type": "signedBy",              	    "keyType": "GPGKeys",              	    "keyPath": "/tmp/containersig.txt"          	}]      	}      }    }
```

This file shows that neither `    quay.io` , or `    docker.io` will perform the verification, because the type is `    insecureAcceptAnything` which overrides the default type of `    reject` . However, `    <span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">&lt;server-address&gt;</span></em></span>` will perform the verification, because the parameter `    type` is set to `    "signedBy"` .

Note
The only `    keyType` currently supported is GPG keys.




1. Under the `    <span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">&lt;server-address&gt;</span></em></span>` entry, modify the `    keyPath` <1> to include the name of your key file.


```
{        	"default": [{"type": "reject"}],        	"transports": {            	"docker": {              	  "quay.io": [{"type": "insecureAcceptAnything"}],              	  "docker.io": [{"type": "insecureAcceptAnything"}],              	  "&lt;server-address&gt;": [{                    	"type": "signedBy",                    	"keyType": "GPGKeys",                    	"keyPath": "/tmp/&lt;key file name&gt;",                    	"signedIdentity": {                      	  "type": "matchExact"                        }                	  }]                }        	}    }
```


1. Save and close the file.


**Verification**

- Pull the file using Podman, or your client of choice:


```
&gt; podman pull &lt;server-address&gt;/&lt;container-name&gt;:&lt;tag name&gt; --tls-verify=false
```

This response verifies the execution environment has been signed with no errors. If the execution environment is not signed, the command fails.

**Additional resources**

- For more information about policy.json, see [documentation for containers-policy.json](https://github.com/containers/image/blob/main/docs/containers-policy.json.5.md#signedby) .


