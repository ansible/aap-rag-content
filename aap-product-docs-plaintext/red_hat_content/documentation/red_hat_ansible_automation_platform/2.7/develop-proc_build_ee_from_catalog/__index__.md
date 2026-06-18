# Build an execution environment image from the catalog

Trigger a container image build on an existing execution environment definition from the catalog, independent of the creation workflow.

## Before you begin

- The execution environment definition was saved to a GitHub repository.
- You can authenticate with GitHub through OAuth.
- Your AAP administrator has configured GitHub repository secrets for builds.

## Procedure

1.  From the execution environment catalog or definition detail page, click **Build**.
2.  In the build dialog, configure the following settings:

- **Registry** -- private automation hub or a custom registry URL.
- **Image Name** -- in `namespace/name` format.
- **Image Tag**.
- **Verify TLS certificates**.

3.  Click **Build**.
4.  Monitor the build from the **Actions** tab on the GitHub repository where the definition was saved.
