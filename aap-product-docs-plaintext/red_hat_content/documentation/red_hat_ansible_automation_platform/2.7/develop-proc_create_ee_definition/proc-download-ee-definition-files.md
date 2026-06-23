# Create an execution environment definition using the UI wizard
## Download definition files without saving to a repository

Create an execution environment definition and download the generated files as a `.tar` archive instead of saving them to a Git repository.

### Procedure

1.  In the wizard, clear the **Publish to a Git repository** checkbox.
2.  Complete the remaining steps and click **Create**.
3.  After creation, click **Download EE files** to download a `.tar` archive containing all generated files.

### Results

The execution environment definition is registered in the catalog. The archive includes `<ee-name>.yml` (with all dependencies declared inline), `<ee-name>-template.yaml`, `ansible.cfg`, and an optional readme.

