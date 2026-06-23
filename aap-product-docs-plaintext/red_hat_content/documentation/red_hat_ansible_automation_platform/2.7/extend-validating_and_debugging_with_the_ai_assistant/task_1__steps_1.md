# Validate and debug with the AI assistant
## Auto-fix errors
### Procedure

1.  In the GitHub Copilot chat window, enter the following prompt:


```
Run ansible_lint on my webserver playbook and apply automatic fixes.
```
The assistant triggers the `ansible_lint`tool wiht the `fix:true` parameter.

2.  The tool then processes the file and applies corrections for issues such as:
1.  FQCN (Fully Qualified Collection Name): Converting short module names to fully qualified ones.
2.  Formatting: Correcting YAML indentation and Jinja2 expression spacing.
3.  Ordering: Fixing key ordering within tasks.

