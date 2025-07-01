# 5. Red Hat Ansible Automation Platform Service on AWS Service Definition
## 5.3. Execution plane
### 5.3.5. Networking with overlapping CIDR blocks




Automation mesh connects the control plane to multiple networks that share the same Classless Inter-Domain Routing (CIDR) block (that is, the same class A address space repeated across different clouds or data centers). Execution nodes regard their deployment network as the local network. You must have at least one execution node instance paired with an instance group to target automation in each network.

