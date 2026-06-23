# Ensure compliance with host-level security controls
## Sudo and NOPASSWD

A compliance profile might require that all users with sudo privileges must provide a password (the `NOPASSWD` directive must not be used in a sudoers file). The installation program runs many tasks as a privileged user, and by default expects to be able to elevate privileges without a password.

To provide a password to the installation program for elevating privileges, append the following options when launching the RPM installer script:

`./setup.sh <setup options> --ask-become-pass`.

For the container-based installation program:

`ansible-playbook ansible.containerized_installer.install --ask-become-pass`

When the installation program is run, you are prompted for the user’s password to elevate privileges.

Note:

Using the `--ask-become-pass` option also applies when running the installation program for day-two operations such as backup and restore.
