# Import your inventory file from source control
## Inventory file fields for source control
### Supported file syntax

Automation controller uses the `ansible-inventory` module from Ansible to process inventory files, and supports all valid inventory syntax that automation controller requires.

Important:

You do not need to write inventory scripts in Python. You can enter any executable file in the source field and must run `chmod +x` for that file and check it into Git.

The following is a working example of JSON output that automation controller can read for the import:

```
{
"_meta": {
"hostvars": {
"host1": {
"fly_rod": true
}
}
},
"all": {
"children": [
"groupA",
"ungrouped"
]
},
"groupA": {
"hosts": [
"host1",
"host10",
"host11",
"host12",
"host13",
"host14",
"host15",
"host16",
"host17",
"host18",
"host19",
"host2",
"host20",
"host21",
"host22",
"host23",
"host24",
"host25",
"host3",
"host4",
"host5",
"host6",
"host7",
"host8",
"host9"
]
}
}
```
