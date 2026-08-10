# Back up and restore your containerized deployment
## Skip database restore when using an external database

If your Ansible Automation Platform deployment uses an external database, and you are restoring the database separately through your database provider or a third-party tool, you can skip database restore operations by using the `postgresql_skip_data` variable.

