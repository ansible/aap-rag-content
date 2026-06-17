# Generate Git personal access tokens

If you are linking external Source Control Management (SCM) systems to Ansible automation portal, you must generate a Personal Access Token for authentication.

Ansible automation portal supports GitHub and GitLab SCMs.

## Create a personal access token on GitHub

Create a GitHub personal access token (classic) to authenticate Ansible automation portal with your GitHub SCM.

### Procedure

1.  In a browser, log in to GitHub.
2.  Click your profile picture and select Settings.
3.  Select Developer settings.
4.  Select Personal access tokens.
5.  Click Generate new token> (and then)Generate new token (classic).
6.  In the Select scopes section, enable the following:

- `repo`
- `read:org`
- `workflow` (as needed)

7.  Click Generate token.
8.  Save the personal access token.

## Create a personal access token on GitLab

Create a GitLab personal access token to authenticate Ansible automation portal with your GitLab SCM.

### Procedure

1.  In a browser, log in to GitLab and click your avatar.
2.  Select Edit profile.
3.  Select Access tokens.
4.  Click Add new token.
5.  Provide a name and expiration date for the token.
6.  In the Scopes section, select the following:

- `read_repository`
- `api`

7.  Click Create personal access token.
8.  Save the personal access token.
