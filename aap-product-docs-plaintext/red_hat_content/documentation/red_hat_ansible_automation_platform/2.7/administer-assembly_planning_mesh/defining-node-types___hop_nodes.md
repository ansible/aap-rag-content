# Scale automation across your infrastructure with automation mesh
## Define automation mesh node types
### Hop nodes

The following stanza defines a single hop node and an execution node in the execution plane. The `node_type` variable is set for every individual node.

```
[execution_nodes]
execution-plane-1.example.com node_type=hop
execution-plane-2.example.com
```
If you want to set the `node_type` at the group level, you must create separate groups for the execution nodes and the hop nodes.

```
[execution_nodes]
execution-plane-1.example.com
execution-plane-2.example.com

[execution_group]
execution-plane-2.example.com

[execution_group:vars]
node_type=execution

[hop_group]
execution-plane-1.example.com

[hop_group:vars]
node_type=hop
```

