# Create dynamic groups with constructed inventories
## Filter on environment variables

You can filter hosts in an inventory by using the `ansible_env` variable in a constructed inventory plugin.

```
source_vars:

plugin: constructed
strict: true
groups:
hosts_using_xterm: ansible_env.TERM == "xterm"

limit: hosts_using_xterm
```

