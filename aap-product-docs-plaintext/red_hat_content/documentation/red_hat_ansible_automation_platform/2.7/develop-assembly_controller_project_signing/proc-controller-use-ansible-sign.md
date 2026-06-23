# Enforce project integrity with signing and verification
## Sign content in automation projects
### Install the ansible-sign CLI utility

Use the `ansible-sign` utility to offer options for you to sign and verify whether the project is signed.

#### Procedure

1.  Run the following command to install `ansible-sign`:


```
$ dnf install ansible-sign
```

2.  Verify that `ansible-sign` was successfully installed using the following command:


```
$ ansible-sign --version
```
Output similar to the following indicates that you have successfully installed `ansible-sign`:

```
ansible-sign 0.1
```

