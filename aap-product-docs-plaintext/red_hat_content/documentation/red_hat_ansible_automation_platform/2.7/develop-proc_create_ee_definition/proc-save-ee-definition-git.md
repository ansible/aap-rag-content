# Create an execution environment definition using the UI wizard
## Save definition files to a Git repository and build

Save execution environment definition files to a GitHub or GitLab repository and optionally trigger an automated container image build.

### Before you begin

- Your AAP administrator has configured GitHub or GitLab OAuth. See [Configure a GitHub OAuth App for saving definitions](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-proc_configure_github_oauth_ee_builder "Configure a GitHub OAuth App so that users can save execution environment definition files to a GitHub repository and trigger automated image builds.") or [Configure a GitLab OAuth App for saving definitions](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-proc_configure_gitlab_ee_builder "Configure a GitLab OAuth App so that users can save execution environment definition files to a GitLab repository.").
- For automated builds: your AAP administrator has configured GitHub repository secrets or GitLab CI/CD variables.

### About this task

When you select **Publish to a Git repository** in the wizard, the definition files are saved to a GitHub or GitLab repository and can optionally trigger an automated container image build.

### Procedure

1.  In the final step of the wizard, select **Publish to a Git repository**.
2.  Authenticate with your Git provider through OAuth when prompted.
3.  Select the target repository or allow the wizard to create a new one.
4.  Optional: Select **Build Execution Environment** to trigger an automated image build after saving.
5.  Configure the target registry (private automation hub or custom), image name, tag, and TLS settings.
6.  Click **Create**.

### Results

The following files are saved to the repository:

- `<ee-name>.yml` -- EE definition with all dependencies inline. The file name matches the name you entered in the form.
- `<ee-name>-template.yaml` -- reusable template file that administrators can register in the catalog.
- `ansible.cfg` -- galaxy server configuration.
- `ee-build.yml` (GitHub) or `.gitlab-ci.yml` (GitLab) -- CI/CD pipeline workflow for automated builds.

After saving, check the build status from the GitHub Actions tab or the GitLab CI/CD Pipelines page on the target repository.

Note:

If the target repository does not exist, it is created automatically. If it exists, a pull request is created instead.

