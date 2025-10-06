# 1. Diagnosing the problem
## 1.1. Troubleshooting Ansible Automation Platform on OpenShift Container Platform by using the must-gather command




The `oc adm must-gather` command line interface (CLI) command collects information from your Ansible Automation Platform installation deployed on OpenShift Container Platform. It gathers information that is often needed for debugging issues, including resource definitions and service logs.

Running the `oc adm must-gather` CLI command creates a new directory containing the collected data that you can use to troubleshoot or attach to your support case.

If your OpenShift environment does not have access to `registry.redhat.io` and you cannot run the `must-gather` command, then run the `oc adm inspect` command instead.

**Prerequisites**

- The OpenShift CLI ( `    oc` ) is installed.


**Procedure**

1. Log in to your cluster:


```
oc login<span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">&lt;openshift_url&gt;</span></em></span>
```


1. Run one of the following commands based on your level of access in the cluster:


- Run `        must-gather` across the entire cluster:


```
oc adm must-gather --image=registry.redhat.io/ansible-automation-platform-25/aap-must-gather-rhel8 --dest-dir<span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">&lt;dest_dir&gt;</span></em></span>
```


-  `            --image` specifies the image that gathers data
-  `            --dest-dir` specifies the directory for the output

- Run `        must-gather` for a specific namespace in the cluster:


```
oc adm must-gather --image=registry.redhat.io/ansible-automation-platform-25/aap-must-gather-rhel8 --dest-dir<span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">&lt;dest_dir&gt;</span></em></span>– /usr/bin/ns-gather<span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">&lt;namespace&gt;</span></em></span>
```


-  `            – /usr/bin/ns-gather` limits the `            must-gather` data collection to a specified namespace


1. To attach the `    must-gather` archive to your support case, create a compressed file from the `    must-gather` directory created before and attach it to your support case.


- For example, on a computer that uses a Linux operating system, run the following command, replacing `        <span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">&lt;must-gather-local.5421342344627712289/&gt;</span></em></span>` with the `        must-gather` directory name:


```
$ tar cvaf must-gather.tar.gz<span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">&lt;must-gather.local.5421342344627712289/&gt;</span></em></span>
```





**Additional resources**

-  [Installing the OpenShift CLI](https://docs.openshift.com/container-platform/4.15/cli_reference/openshift_cli/getting-started-cli.html)
-  [ocm adm inspect](https://docs.openshift.com/container-platform/4.15/cli_reference/openshift_cli/administrator-cli-commands.html#oc-adm-inspect)


