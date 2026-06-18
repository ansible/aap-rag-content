# Run playbooks with `ansible-navigator` using the assistant

After you have built a suitable execution environment, you can ask the assistant to generate the correct `ansible-navigator` command to execute your playbook in that particular environment.

## Procedure

1.  Ask the assistant to generate a command that runs the playbook in your execution environment. For example:


```
Generate a command that runs this playbook in the execution environment <your-file-name>
```
The assistant then generates an appropriate `ansible-navigator` command, ensuring the `--execution-environment-image` flag points to your newly built tag.

A generated command might look like the following:

```
ansible-navigator run playbook.yml --execution-environment-image webserver-ee:1.0 --mode stdout
```

2.  In the VS Code terminal, execute the command to run your automation within the custom environment.
