# 6. Job templates
## 6.15. Custom fact scans




A playbook for a custom fact scan is similar to the example in the [Fact scan playbooks](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html-single/using_automation_execution/index#controller-fact-scan-playbooks) section. For example, a playbook that only uses a custom `scan_foo` Ansible fact module looks similar to this:

```
scan_foo.py:
def main():
module = AnsibleModule(
argument_spec = dict())


foo = [
{
"hello": "world"
},
{
"foo": "bar"
}
]
results = dict(ansible_facts=dict(foo=foo))
module.exit_json(**results)


main()
```

To use a custom fact module, ensure that it lives in the `/library/` subdirectory of the Ansible project used in the scan job template. This fact scan module returns a hard-coded set of facts:

```
[
{
"hello": "world"
},
{
"foo": "bar"
}
]
```

For more information, see the [Developing modules](https://docs.ansible.com/ansible/latest/dev_guide/developing_modules_general.html#developing-modules) section of the Ansible documentation.

