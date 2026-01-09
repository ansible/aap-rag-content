# Chapter 2. Use a playbook to establish a connection to a managed node




Learn how to create and run a simple Ansible Playbook that connects to a network device, gathers facts, and displays them.

To confirm your credentials, you can connect to a network device manually and retrieve its configuration. Replace the sample user and device name with your real credentials.

For example, for a VyOS router:

```
ssh my_vyos_user@vyos.example.net
show config
exit
```

