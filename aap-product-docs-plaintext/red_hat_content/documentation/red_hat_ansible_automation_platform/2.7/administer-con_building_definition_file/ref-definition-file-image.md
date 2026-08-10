# Build a definition file
## Images

The `images` section of the definition file identifies the base image. Verification of signed container images is supported with the `podman` container runtime.

The following table shows a list of values that you can use in `images`:

| Value             | Description                                                                                                                                                                                              |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <br> `base_image` | <br>Specifies the parent image for the automation execution environment which enables a new image to be built that is based on an existing image. This is typically a supported execution environment base image such as *ee-minimal* or *ee-supported*, but it can also be an execution environment image that you have created and want to customize further.<br>A `name` key is required for the container image to use. Specify the `signature _original_name` key if the image is mirrored within your repository, but is signed with the image’s original signature key. Image names must contain a tag, such as `:latest`.<br>Red Hat provides `ee-minimal` and `ee-supported` base images on `registry.redhat.io`. See the [Red Hat ecosystem catalog](https://catalog.redhat.com/en/search?searchType=Containers&build_categories_list=Automation+execution+environment) for available images for your version of Ansible Automation Platform. |
