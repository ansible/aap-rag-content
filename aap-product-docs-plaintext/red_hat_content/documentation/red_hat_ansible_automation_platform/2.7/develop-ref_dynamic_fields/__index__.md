# Dynamic fields

Dynamic fields appear or disappear based on user selections. Use the `dependencies` keyword with `allOf` and `if`/`then` to define conditional field visibility.

This lets you build forms where selecting a value in one field reveals additional fields relevant to that selection.

Dynamic fields are useful for:

- Showing advanced options only when the user enables them.
- Displaying different configuration fields based on a resource type or category selection.
- Requesting a reason or justification when the user selects a specific option.
