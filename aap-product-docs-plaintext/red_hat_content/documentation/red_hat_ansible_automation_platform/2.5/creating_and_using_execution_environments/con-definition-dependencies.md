# 3. Using Ansible Builder
## 3.7. Breakdown of definition file content
### 3.7.2. Definition dependencies




You can include dependencies that must be installed into the final image in the dependencies section of your definition file.

To avoid issues with your automation execution environment image, make sure that the entries for Galaxy, Python, and system point to a valid requirements file, or are valid content for their respective file types.

#### 3.7.2.1. Galaxy




The `galaxy` entry points to a valid requirements file or includes inline content for the `ansible-galaxy collection install -r …​` command.

The entry `requirements.yml` can be a relative path from the directory of the automation execution environment definition’s folder, or an absolute path.

The content might look like the following:

```
collections:
- community.aws
- kubernetes.core
```

#### 3.7.2.2. Python




The `python` entry in the definition file points to a valid requirements file or to an inline list of Python requirements in [PEP508](https://ansible.readthedocs.io/projects/builder/en/latest/porting_guides/porting_guide_v3.1/#pep-508-standard) format for the `pip install -r …​` command.

The entry `requirements.txt` is a file that installs extra Python requirements on top of what the Collections already list as their Python dependencies. It might be listed as a relative path from the directory of the automation execution environment definition’s folder, or an absolute path. The contents of a `requirements.txt` file should be formatted as the following example, similar to the standard output from a `pip freeze` command.

The content might look like the following:

```
boto&gt;=2.49.0
botocore&gt;=1.12.249
pytz
python-dateutil&gt;=2.7.0
awxkit
packaging
requests&gt;=2.4.2
xmltodict
azure-cli-core==2.11.1
openshift&gt;=0.6.2
requests-oauthlib
openstacksdk&gt;=0.13
ovirt-engine-sdk-python&gt;=4.4.10
```

#### 3.7.2.3. System




The `system` entry in the definition points to a [bindep](https://docs.opendev.org/opendev/bindep/latest/readme.html) requirements file or to an inline list of bindep entries, which install system-level dependencies that are outside of what the collections already include as their dependencies. The `system` entry can be listed as a relative path from the directory of the automation execution environment definition’s folder, or as an absolute path. At a minimum, the the collections must specify necessary requirements for `[platform:rpm]` .

To demonstrate this, the following is an example `bindep.txt` file that adds the `libxml2` and `subversion` packages to a container.

The content might look like the following:

```
libxml2-devel [platform:rpm]
subversion [platform:rpm]
```

Entries from multiple collections are combined into a single file. This is processed by `bindep` and then passed to `dnf` . Only requirements with no profiles or no runtime requirements will be installed to the image.

#### 3.7.2.4. Images




The `images` section of the definition file identifies the base image. Verification of signed container images is supported with the `podman` container runtime.

The following table shows a list of values that you can use in `images` :

| Value | Description |
| --- | --- |
|  `base_image` | Specifies the parent image for the automation execution environment which enables a new image to be built that is based on an existing image. This is typically a supported execution environment base image such as _ee-minimal_ or _ee-supported_ , but it can also be an execution environment image that you have created and want to customize further.

A `name` key is required for the container image to use. Specify the `signature _original_name` key if the image is mirrored within your repository, but is signed with the image’s original signature key. Image names must contain a tag, such as `:latest` .

The default image is `registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8:latest` . |


