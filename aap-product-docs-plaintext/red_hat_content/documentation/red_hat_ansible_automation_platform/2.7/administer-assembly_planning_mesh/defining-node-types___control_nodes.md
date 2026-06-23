# Scale automation across your infrastructure with automation mesh
## Define automation mesh node types
### Control nodes

The following inventory consists of a single control node in the control plane:

```
[automationcontroller]
control-plane-1.example.com node_type=control
```
If you set `node_type` to `control` in the `vars` stanza for the control plane nodes, then all of the nodes in control plane are control nodes.

```
[automationcontroller]
control-plane-1.example.com

[automationcontroller:vars]
node_type=control
```

