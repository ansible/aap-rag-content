# What the aap_snapshot migration artifact contains
## Security considerations

Important:

The artifact contains database credentials, encryption keys, and `SECRET_KEY` values for all exported components. Treat the artifact as sensitive material. Restrict access to the `artifact_dir` directory on the control node, and use secure transfer methods when moving the artifact to the import host.

