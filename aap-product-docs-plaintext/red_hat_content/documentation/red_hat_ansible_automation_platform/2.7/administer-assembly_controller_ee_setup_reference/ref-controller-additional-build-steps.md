# Execution environment setup reference
## Additional_build_steps

The build steps specify custom build commands for any build phase. These commands are inserted directly into the build instruction file for the container runtime, for example, Containerfile or Dockerfile. The commands must conform to any rules required by the containerization tool.

You can add build steps before or after any stage of the image creation process. For example, if you need `git` to be installed before you install your dependencies, you can add a build step at the end of the base build stage.

The following are the valid keys. Each supports either a multi-line string, or a list of strings.

| <br> **append\_base**     | <br>Commands to insert after building of the base image.     |
| ------------------------- | ------------------------------------------------------------ |
| <br> **append\_builder**  | <br>Commands to insert after building of the builder image.  |
| <br> **append\_final**    | <br>Commands to insert after building of the final image.    |
| <br> **append\_galaxy**   | <br>Commands to insert after building of the galaxy image.   |
| <br> **prepend\_base**    | <br>Commands to insert before building of the base image.    |
| <br> **prepend\_builder** | <br>Commands to insert before building of the builder image. |
| <br> **prepend\_final**   | <br>Commands to insert before building of the final image.   |
| <br> **prepend\_galaxy**  | <br>Commands to insert before building of the galaxy image.  |

