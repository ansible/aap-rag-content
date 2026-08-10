# Remove the automation intelligent assistant from a containerized deployment
## What to do next

To verify:

1. Confirm that the chatbot containers are no longer present on the host:

```
podman ps -a --filter name=ansible-lightspeed
```

No containers with the name `ansible-lightspeed`should be listed.

2. Access the Ansible Automation Platform web interface and confirm that the chat icon is no longer displayed in the top navigation bar.
