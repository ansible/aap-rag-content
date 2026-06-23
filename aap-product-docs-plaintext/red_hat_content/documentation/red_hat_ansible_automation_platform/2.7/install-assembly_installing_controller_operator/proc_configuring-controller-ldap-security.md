# Configure automation controller
## Configure your LDAP for automation controller

You can configure your LDAP SSL configuration for automation controller through any of the following options:

### About this task

- The automation controller user interface. The platform gateway user interface. See [Configure LDAP authentication](/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-proc_controller_set_up_ldap#controller-set-up-LDAP "As a platform administrator, you can configure LDAP as the source for account authentication information for Ansible Automation Platform users.") for additional steps.

- The following procedure steps.

### Procedure

1.  Create a secret in your Ansible Automation Platform namespace for the `bundle-ca.crt` file (the filename must be `bundle-ca.crt`):


```
$ oc create secret -n aap generic bundle-ca-secret --from-file=bundle-ca.crt
```
Note:
The target filename for this operation must be `bundle-ca.crt` and the secret name should be `bundle-ca-secret`.

2.  Add the `bundle_cacert_secret` to the Ansible Automation Platform customer resource:


```
...
spec:
bundle_cacert_secret: bundle-ca-secret
...
```

### Results

You can verify the expected certificate by running:

```
oc get deployments -l 'app.kubernetes.io/component=aap-gateway'
```
Followed by:

```
oc exec -it deployment.apps/<gateway-deployment-name-from-above> -- openssl x509 -in /etc/pki/tls/certs/ca-bundle.crt -noout -text
```

