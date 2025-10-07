# 3. Specifying dedicated nodes
## 3.2. Specify nodes for job execution




You can add a node selector to the container group pod specification to ensure they only run against certain nodes. First add a label to the nodes you want to run jobs against.

The following procedure adds a label to a node.

**Procedure**

1. List the nodes in your cluster, along with their labels:


```
kubectl get nodes --show-labels
```

The output is similar to this (shown here in a table):

| Name | Status | Roles | Age | Version | Labels |
| --- | --- | --- | --- | --- | --- |
|  `worker0` | Ready | <none> | 1d | v1.13.0 |  `…​,kubernetes.io/hostname=worker0` |
|  `worker1` | Ready | <none> | 1d | v1.13.0 |  `…​,kubernetes.io/hostname=worker1` |
|  `worker2` | Ready | <none> | 1d | v1.13.0 |  `…​,kubernetes.io/hostname=worker2` |



1. Choose one of your nodes, and add a label to it by using the following command:


```
kubectl label nodes &lt;your-node-name&gt; &lt;aap_node_type&gt;=&lt;execution&gt;
```

For example:


```
kubectl label nodes &lt;your-node-name&gt; disktype=ssd
```

where `    &lt;your-node-name&gt;` is the name of your chosen node.


1. Verify that your chosen node has a `    disktype=ssd` label:


```
kubectl get nodes --show-labels
```


1. The output is similar to this (shown here in a table):

| Name | Status | Roles | Age | Version | Labels |
| --- | --- | --- | --- | --- | --- |
|  `worker0` | Ready | <none> | 1d | v1.13.0 |  `…​disktype=ssd,kubernetes.io/hostname=worker0` |
|  `worker1` | Ready | <none> | 1d | v1.13.0 |  `…​,kubernetes.io/hostname=worker1` |
|  `worker2` | Ready | <none> | 1d | v1.13.0 |  `…​,kubernetes.io/hostname=worker2` |


You can see that the `    worker0` node now has a `    disktype=ssd` label.


1. In the automation controller UI, specify that label in the metadata section of your customized pod specification in the container group.


```
apiVersion: v1    kind: Pod    metadata:      disktype: ssd      namespace: ansible-automation-platform    spec:      serviceAccountName: default      automountServiceAccountToken: false      nodeSelector:        aap_node_type: execution      containers:        - image: &gt;-         registry.redhat.io/ansible-automation-platform-22/ee-supported-rhel8@sha256:d134e198b179d1b21d3f067d745dd1a8e28167235c312cdc233860410ea3ec3e          name: worker          args:            - ansible-runner            - worker            - '--private-data-dir=/runner'          resources:            requests:              cpu: 250m              memory: 100Mi
```




