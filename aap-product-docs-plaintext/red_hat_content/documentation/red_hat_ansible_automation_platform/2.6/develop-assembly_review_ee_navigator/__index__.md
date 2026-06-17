# Run a playbook to display execution environment contents

As a content developer, you can review your automation execution environment with automation content navigator and display the packages and collections included in the automation execution environments. Automation content navigator runs a playbook to extract and display the results.

## Review automation execution environments from automation content navigator

Use the automation content navigator text-based interface to review your automation execution environments. This allows you to quickly inspect packages, versions, and collections installed in the environment.

### Before you begin

- Automation execution environments

### Procedure

1.  Review the automation execution environments included in your automation content navigator configuration.

```
$ ansible-navigator images
```

![List of automation execution environments](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/navigator-images-list.png)

2.  Type the number of the automation execution environment you want to delve into for more details.
![Automation execution environment details](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/navigator-image-details.png)
You can review the packages and versions of each installed automation execution environment and the Ansible version any included collections.

3.  Optional: pass in the automation execution environment that you want to use. This becomes the primary and is the automation execution environment that automation content navigator uses.

```
$ ansible-navigator images --eei registry.example.com/example-enterprise-ee:latest
```

### Results

- Review the automation execution environment output.
![Automation execution environment output](/webassets/aem/red_hat_ansible_automation_platform/2.6/images/navigator-image-details.png)
