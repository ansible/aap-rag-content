# Execution environment setup reference
## Images

Use the **images** dictionary to define container images for your execution environment. Each key represents a unique image name, while the corresponding value is a dictionary defining that image's properties.

At a minimum you must specify a source, image, and tag for the base image. The base image provides the operating system and can also provide some packages. Use the standard `host/namespace/container:tag` syntax to specify images. You can use Podman or Docker shortcut syntax instead, but the full definition is more reliable and portable.

Valid keys for this section are:

| <br> **base\_image** | <br>A dictionary defining the parent image for the execution environment.<br>A `name` key must be supplied with the container image to use. Use the `signature_original_name` key if the image is mirrored within your repository, but signed with the original image’s signature key. |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

