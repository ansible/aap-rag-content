# Manage containers in your private automation hub
## Pull execution environments for use in automation hub

Before you can push execution environments to your private automation hub, you must first pull them from an existing registry and tag them for use.

### Before you begin

- You have permissions to pull automation execution environments from `registry.redhat.io`.

### About this task

The following example details how to pull an execution environment from the Red Hat Ecosystem Catalog (`registry.redhat.io`).

### Procedure

1.  Log in to Podman with your `registry.redhat.io` credentials:


```
$ podman login registry.redhat.io
```

2.  Pull an execution environment:


```
$ podman pull registry.redhat.io/<ee_name>:<tag>
```

### Results

To verify that the execution environment you pulled is contained in the list, take these steps:

1. List the images in local storage:

```
$ podman images
```

2. Check the execution environment name, and verify that the tag is correct.

