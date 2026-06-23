# Create automation runtimes with execution and decision environments
## Use the base automation execution environment

Ansible Automation Platform provides access to some base automation execution environments. You can use a base execution environment as a starting point for creating a customized execution environment.

### Before you begin

- You have a valid Red Hat Ansible Automation Platform subscription.

### About this task

Ansible Automation Platform includes the following execution environments:

- `Minimal` - Includes the latest Ansible-core 2.15 release along with Ansible Runner, but does not include collections or other content
- `EE Supported` - Minimal, plus all Red Hat-supported collections and dependencies


Base images included with Ansible Automation Platform are hosted on the Red Hat Ecosystem Catalog (`registry.redhat.io`).

### Procedure

1.  Log in to `registry.redhat.io`.

```bash
$ podman login registry.redhat.io
```

2.  Pull the base images from the registry:


```bash
$ podman pull registry.redhat.io/aap/<image name>
```

