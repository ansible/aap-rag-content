+++
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_idps"
title = "Automate network intrusion detection and prevention systems - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/secure-assembly_idps/", "Automate network intrusion detection and prevention systems"]]
category = "Secure"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-assembly_idps/aem-page/secure-assembly_idps.html"
last_crumb = "Automate network intrusion detection and prevention systems"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Automate network intrusion detection and prevention systems"
oversized = "false"
page_slug = "secure-assembly_idps"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/secure-assembly_idps"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/secure-assembly_idps/toc/toc.json"
type = "aem-page"
+++

# Automate network intrusion detection and prevention systems

You can use Ansible Automation Platform to automate your *Intrusion Detection and Prevention System* (IDPS). In this section, we use Snort as the IDPS. Use automation hub to consume content collections, such as tasks, roles, and modules to create automated workflows.

## Requirements and prerequisites

Before you begin automating your IDPS with Ansible Automation Platform, ensure that you have the proper installations and configurations necessary to successfully manage your IDPS.

- You have installed Ansible-core 2.15 or later.
- SSH connection and keys are configured.
- IDPS software (Snort) is installed and configured.
- You have access to the IDPS server (Snort) to enforce new policies.

## Verify your IDPS installation

Use the following procedure to verify that Snort has been configured successfully:

### Procedure

1.  Call snort using `sudo` and ask for the version:
  

```
$ sudo snort --version

    ,,_     -*> Snort! <*-
  o"  )~   Version 2.9.13 GRE (Build 15013)
  ""    By Martin Roesch & The Snort Team: http://www.snort.org/contact#team
        Copyright (C) 2014-2019 Cisco and/or its affiliates. All rights reserved.
        Copyright (C) 1998-2013 Sourcefire, Inc., et al.
        Using libpcap version 1.5.3
        Using PCRE version: 8.32 2012-11-30
        Using ZLIB version: 1.2.7
```

2.  Verify that the service is actively running using the following command:
      `sudo systemctl`:

```
$ sudo systemctl status snort
● snort.service - Snort service
   Loaded: loaded (/etc/systemd/system/snort.service; enabled; vendor preset: disabled)
   Active: active (running) since Mon 2019-08-26 17:06:10 UTC; 1s ago
  Main PID: 17217 (snort)
   CGroup: /system.slice/snort.service
           └─17217 /usr/sbin/snort -u root -g root -c /etc/snort/snort.conf -i eth0 -p -R 1 --pid-path=/var/run/snort --no-interface-pidfile --nolock-pidfile
[...]
```

3.  If the Snort service is not actively running, restart it with `systemctl restart snort` and recheck the status.
4.  When you confirm that the service is actively running, exit the Snort server by simultaneously pressing `CTRL` and `D`, or by typing `exit` on the command line. All further interaction will be done through Ansible Automation Platform from the Ansible control host.

## Automate your IDPS rules with Ansible Automation Platform

To automate your IDPS, use the `ids_rule` role to create and change Snort rules. Snort uses rule-based language that analyzes your network traffic and compares it against the given rule set.

The following lab environment demonstrates what an Ansible security automation integration would look like. A machine called “Attacker” simulates a potential attack pattern on the target machine on which the IDPS is running.

Keep in mind that a real world setup will feature other vendors and technologies.


![Sample Ansible security automation integration](/webassets/aem/red_hat_ansible_automation_platform/2.7/images/security-ids-sample-demo.png)  

## Create a new IDPS rule

Use the `ids_rule` role to manage your rules and signatures for IDPS.

### Before you begin

- You need `root` privileges to make any changes on the Snort server.

### About this task

For example, you can set a new rule that looks for a certain pattern aligning with a previous attack on your firewall.

 Note:

Currently, the `ids_rule` role only supports Snort IDPS.

### Procedure

1.  Install the `ids_rule` role using the ansible-galaxy command:
       `$ ansible-galaxy install ansible_security.ids_rule`

2.  Create a new playbook file titled `add_snort_rule.yml`. Set the following parameters:
  

```
- name: Add Snort rule
  hosts: snort
```

3.  Add the `become` flag to ensure that Ansible handles privilege escalation.

```
- name: Add Snort rule
  hosts: snort
  become: true
```

4.  Specify the name of your IDPS provider by adding the following variables:
  

```
- name: Add Snort rule
  hosts: snort
  become: true

    vars:
    ids_provider: snort
```

5.  Add the following tasks and task-specific variables, for example, rules, Snort rules file, and the state of the rule - present or absent, to the playbook:
  

```
- name: Add Snort rule
  hosts: snort
  become: true

    vars:
    ids_provider: snort

    tasks:
    -  name: Add snort password attack rule
       include_role:
         name: "ansible_security.ids_rule"
       vars:
         ids_rule: 'alert tcp any any -> any any (msg:"Attempted /etc/passwd Attack"; uricontent:"/etc/passwd"; classtype:attempted-user; sid:99000004; priority:1; rev:1;)'
         ids_rules_file: '/etc/snort/rules/local.rules'
         ids_rule_state: present
```
    Tasks are components that make changes on the target machine. Since you are using a role that defines these tasks, the `include_role` is the only entry you need.

    The `ids_rules_file` variable specifies a defined location for the `local.rules` file, while the `ids_rule_state` variable indicates that the rule should be created if it does not already exist.

6.  Run the playbook by executing the following command:
       `$ ansible-navigator run add_snort_rule.ym --mode stdout`

    When the playbook runs, all of your tasks will be executed in addition to your newly created rules. Your playbook output confirms your PLAY, TASK, RUNNING HANDLER, and PLAY RECAP.

### Results

To verify that your IDPS rules were successfully created, SSH to the Snort server and view the content of the `/etc/snort/rules/local.rules` file.
