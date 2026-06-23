# Best practices for automation execution
## Use dynamic inventory sources

Define an inventory synchronization process by using dynamic sources, such as a cloud provider or CMDB, to help ensure your infrastructure inventory in automation controller stays consistently up-to-date.

Note:

Edits and additions to Inventory host variables persist beyond an inventory synchronization as long as `--overwrite_vars` is **not** set.

