# What the aap_snapshot migration artifact contains
## Artifact naming

The playbook creates one file in `artifact_dir`:

- `aap-snapshot-<aap-version>-<timestamp>.tar` — timestamped artifact, where the timestamp uses the format `YYYYMMDD-HHMMSS` (UTC).

A `.sha256` checksum file is created alongside it. Pass the full timestamped filename to the import playbook.

