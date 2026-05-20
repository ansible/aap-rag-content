# 3. Manage containers in private automation hub
## 3.3. Populating your private automation hub container registry
### 3.3.1. Pulling execution environments for use in automation hub

Before you can push execution environments to your private automation hub, you must first pull them from an existing registry and tag them for use. The following example details how to pull an execution environment from the Red Hat Ecosystem Catalog (`registry.redhat.io`).

**Prerequisites**

- You have permissions to pull automation execution environments from `registry.redhat.io`.

**Procedure**

1. Log in to Podman with your `registry.redhat.io` credentials:

$ podman login registry.redhat.io

2. Pull an execution environment:

$ podman pull registry.redhat.io/<ee_name>:<tag>

**Verification**

To verify that the execution environment you pulled is contained in the list, take these steps:

1. List the images in local storage:

$ podman images

2. Check the execution environment name, and verify that the tag is correct.

**Additional resources**

- [Red Hat Ecosystem Catalog Help](https://redhat-connect.gitbook.io/catalog-help/)

