# 8. About the installer inventory file
## 8.4. Rules for declaring variables in inventory files




The values of string variables are declared in quotes. For example:

```
pg_database='awx'
pg_username='awx'
pg_password='&lt;password&gt;'
```

When declared in a `:vars` section, INI values are interpreted as strings. For example, `var=FALSE` creates a string equal to `FALSE` . Unlike host lines, `:vars` sections accept only a single entry per line, so everything after the `=` must be the value for the entry. Host lines accept multiple `key=value` parameters per line. Therefore they need a way to indicate that a space is part of a value rather than a separator. Values that contain whitespace can be quoted (single or double). For more information, see [Python shlex parsing rules](https://docs.python.org/3/library/shlex.html#parsing-rules) .

If a variable value set in an INI inventory must be a certain type (for example, a string or a boolean value), always specify the type with a filter in your task. Do not rely on types set in INI inventories when consuming variables.

Note
Consider using YAML format for inventory sources to avoid confusion on the actual type of a variable. The YAML inventory plugin processes variable values consistently and correctly.



If a parameter value in the Ansible inventory file contains special characters, such as #, { or }, you must double-escape the value (that is enclose the value in both single and double quotation marks).

For example, to use `mypasswordwith#hashsigns` as a value for the variable `pg_password` , declare it as `pg_password='"mypasswordwith#hashsigns"'` in the Ansible host inventory file.

**Disclaimer** : Links contained in this information to external website(s) are provided for convenience only. Red Hat has not reviewed the links and is not responsible for the content or its availability. The inclusion of any link to an external website does not imply endorsement by Red Hat of the website or their entities, products or services. You agree that Red Hat is not responsible or liable for any loss or expenses that may result due to your use of (or reliance on) the external site or content.

