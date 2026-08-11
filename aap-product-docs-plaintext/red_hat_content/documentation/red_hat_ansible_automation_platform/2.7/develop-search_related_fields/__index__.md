# Search related fields

You can search across related resources, such as organizations or projects, by prefixing the query with the related field name.

## Procedure

In the search bar, type the related field name followed by a colon and the search value.

You can add secondary fields separated by periods to narrow the search.

| Query                                   | Behavior                                                                     |
| --------------------------------------- | ---------------------------------------------------------------------------- |
| `organization:Default`                  | Searches the name and description of the related organization for`Default`.  |
| `job_template.project.name:"A Project"` | Searches for job templates that use a project whose name matches`A Project`. |

Note:

The required prefix depends on the endpoint. The query `job_template.project.name` applies to the `unified_job_templates` endpoint. If you search from the `job_templates` endpoint directly, omit the `job_template` prefix and use `project.name` instead.
