# Execution environment definition detail page

The execution environment definition detail page displays metadata, defined content, and available actions for a registered definition in the catalog.

## Detail page sections

Open an execution environment definition from the catalog to view its detail page. The detail page includes the following sections:

| Section             | Description                                                                 |
| ------------------- | --------------------------------------------------------------------------- |
| **About**           | Metadata, owner, tags, and lifecycle status.                                |
| **Defined Content** | Parsed YAML showing the base image, collections, packages, and build steps. |
| **Readme**          | Documentation for the execution environment definition.                     |
| **Resources**       | Links to related documentation.                                             |

## Available actions

The following actions are available from the detail page:

| Action                | Description                                                                                        |
| --------------------- | -------------------------------------------------------------------------------------------------- |
| **Build**             | Trigger a new container image build from the definition.                                           |
| **Edit definition**   | Open the source in your Git provider.                                                              |
| **View in source**    | Navigate to the source repository.                                                                 |
| **Download EE files** | Download the definition as a `.tar` archive (available for definitions not saved to a repository). |
| **Delete**            | Unregister the definition from the catalog.                                                        |
