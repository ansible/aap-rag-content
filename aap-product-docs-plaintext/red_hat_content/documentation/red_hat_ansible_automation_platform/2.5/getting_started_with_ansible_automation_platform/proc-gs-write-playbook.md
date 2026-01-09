# 3. Getting started as an automation developer
## 3.3. Writing a playbook




Create a playbook that pings your hosts and prints a "Hello world" message.

Ansible uses the YAML syntax. YAML is a human-readable language that enables you to create playbooks without having to learn a complicated coding language.

**Procedure**

1. Create a file named `    playbook.yaml` in your `    ansible_quickstart` directory, with the following content:


```
- name: My first play      hosts: myhosts      tasks:        - name: Ping my hosts        ansible.builtin.ping:            - name: Print message        ansible.builtin.debug:          msg: Hello world
```


1. Run your playbook:


```
$ ansible-playbook -i inventory.ini playbook.yaml
```

Ansible returns the following output:




```
PLAY [My first play] ********************************************************

TASK [Gathering Facts] ******************************************************
ok: [192.0.2.50]
ok: [192.0.2.51]
ok: [192.0.2.52]

TASK [Ping my hosts] ********************************************************
ok: [192.0.2.50]
ok: [192.0.2.51]
ok: [192.0.2.52]

TASK [Print message] ********************************************************
ok: [192.0.2.50] =&gt; {
"msg": "Hello world"
}
ok: [192.0.2.51] =&gt; {

"msg": "Hello world"
}
ok: [192.0.2.52] =&gt; {
"msg": "Hello world"
}

PLAY RECAP ******************************************************************
192.0.2.50: ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
192.0.2.51: ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
192.0.2.52: ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

**Additional resources**

-  [Getting started with playbooks](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/getting_started_with_playbooks)
-  [Red Hat Ansible Lightspeed with IBM watsonx Code Assistant](https://developers.redhat.com/products/ansible/lightspeed?source=sso)


