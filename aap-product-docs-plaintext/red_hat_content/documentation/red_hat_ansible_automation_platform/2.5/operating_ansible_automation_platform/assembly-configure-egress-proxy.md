# Chapter 3. Configuring Ansible Automation Platform to use egress proxy




You can deploy Ansible Automation Platform so that egress from the platform for various purposes functions properly through proxy servers. Egress proxy allows clients to make indirect (through a proxy server) requests to network services. The client first connects to the proxy server and requests some resource, for example, email, located on another server. The proxy server then connects to the specified server and retrieves the resource from it.

