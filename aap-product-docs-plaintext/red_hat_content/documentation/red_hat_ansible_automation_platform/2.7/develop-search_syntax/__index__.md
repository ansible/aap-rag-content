# Search syntax

A search query consists of a field name, a colon, and a value. If you omit the colon, the platform treats the input as a simple string search.

## Syntax rules

- Use `field:value` to search a specific field.
- Use a plain string without a colon to run an `icontains` search against the name and description fields.
- Separate multiple terms with a space to return results that match all terms. Wrap terms in quotes to match the exact phrase.

Note:

Job template searches accept alphanumeric characters only.

## Examples

| Query                       | Behavior                                                                                                                                                                                                 |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name:localhost`            | Searches for`localhost` in the`name` field. If the field name does not match a known field or related field, the query is treated as a string search.                                                    |
| `organization.name:Default` | Related field search. The period separates the related model from the field. You can chain multiple periods for deeper lookups.                                                                          |
| `foobar`                    | Simple string search. Runs`?search=foobar`, which performs an`icontains` lookup against name and description. Note that API field names might differ from the UI labels, for example,`Management job` in the UI is`system_job` in the API. |
| `organization:Default`      | Related field search without specifying a sub-field. Runs an`icontains` search against both the name and description of the related organization.                                                        |
