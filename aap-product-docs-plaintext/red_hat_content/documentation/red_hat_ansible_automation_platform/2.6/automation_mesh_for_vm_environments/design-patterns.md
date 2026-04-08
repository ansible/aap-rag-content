# Chapter 3. Automation mesh design patterns




The automation mesh topologies in this section provide examples you can use to design a mesh deployment in your environment. Examples range from a simple, hydrid node deployment to a complex pattern that deploys numerous automation controller instances, employing several execution and hop nodes.

Important
If you are creating a mesh similar to the following in a containerized environment:

- Replace the `    node_type` variable with `    receptor_type`
- Replace the `    peers` variable with `    receptor_peers`
- Replace inventory group names with explicit comma-separated lists of hostnames


The value of `receptor_peers` must be a comma-separated list of hostnames. Do not use inventory group names. For more information, see [Adding execution nodes](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/containerized_installation/advanced-configuration-containerized#adding-execution-nodes) .



**Prerequisites**

- You reviewed conceptual information on node types and relationships.


Note
The following examples include images that illustrate the mesh topology. The arrows in the images indicate the direction of peering. After peering is established, the connection between the nodes allows bidirectional communication.



