# 2. Automation mesh for operator-based Red Hat Ansible Automation Platform
## 2.10. Upgrading receptors




A software update addresses any issues or bugs to provide a better experience of working with the technology. Anyone with administrative rights can update the receptor on an execution node.

Red Hat recommends performing updates to the receptor after any Ansible Automation Platform control plane updates. This ensures you are using the latest version. The best practice is to perform regular updates outside of any updates to the control plane.

**Procedure**

1. Check the current receptor version:


```
receptor --version
```


1. Update the receptor:


```
sudo dnf update ansible-runner receptor -y
```

Note
To upgrade all packages (not just the receptor), use `    dnf update` , then reboot with `    reboot` .




1. Verify the installation. After the update is complete, check the receptor version again to verify the update:


```
receptor --version
```


1. Restart the receptor service:


```
sudo systemctl restart receptor
```


1. Ensure the receptor is working correctly and is properly connected to the controller or other nodes in the system.



<span id="idm140404608830192"></span>
