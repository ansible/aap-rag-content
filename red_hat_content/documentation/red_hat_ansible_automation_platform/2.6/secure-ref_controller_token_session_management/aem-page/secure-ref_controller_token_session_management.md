+++
template = "docs/aem-title.html"
title = "Create, revoke, or clear tokens - Red Hat Ansible Automation Platform 2.6"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-ref_controller_token_session_management"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-assembly_gw_configure_authentication/", "Configure central authentication for Ansible Automation Platform"]]
category = "Secure"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/secure-ref_controller_token_session_management/aem-page/secure-ref_controller_token_session_management.html"
last_crumb = "Create, revoke, or clear tokens"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Create, revoke, or clear tokens"
oversized = "false"
page_slug = "secure-ref_controller_token_session_management"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/secure-ref_controller_token_session_management"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/secure-ref_controller_token_session_management/toc/toc.json"
type = "aem-page"
+++

# Create, revoke, or clear tokens

Ansible Automation Platform supports the following commands for OAuth2 token management:

-  [`create_oauth2_token`](/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-ref_controller_token_session_management#ref-controller-create-oauth2-token "Use the following command to create OAuth2 tokens (specify the username for example_user):")
-  [`revoke_oauth2_tokens`](/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-ref_controller_token_session_management#ref-controller-revoke-oauth2-token "Use this command to revoke OAuth2 tokens, both application tokens and personal access tokens (PAT). It revokes all application tokens (but not their associated refresh tokens), and revokes all personal access tokens. However, you can also specify a user for whom to revoke all tokens.")
-  [`cleartokens`](/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-ref_controller_token_session_management#ref-controller-clear-sessions "Use the cleartokens command to delete all sessions that have expired.")


-  [`clearsessions`](/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-ref_controller_token_session_management#ref-controller-clear-sessions "Use the cleartokens command to delete all sessions that have expired.")

## `create_oauth2_token`

Use the following command to create OAuth2 tokens (specify the username for `example_user`):

```
$ aap-gateway-manage create_oauth2_token --user example_user
  
  New OAuth2 token for example_user: j89ia8OO79te6IAZ97L7E8bMgXCON2
```
Ensure that you give a valid user when creating tokens. Otherwise, an error message that you attempted to issue the command without specifying a user, or supplied a username that does not exist, is displayed.

## `revoke_oauth2_tokens`

Use this command to revoke OAuth2 tokens, both application tokens and personal access tokens (PAT). It revokes all application tokens (but not their associated refresh tokens), and revokes all personal access tokens. However, you can also specify a user for whom to revoke all tokens.

To revoke all existing OAuth2 tokens use the following command:

```
$ aap-gateway-manage revoke_oauth2_tokens
```
To revoke all OAuth2 tokens and their refresh tokens use the following command:

```
$ aap-gateway-manage revoke_oauth2_tokens --revoke_refresh
```
To revoke all OAuth2 tokens for the user with `id=example_user` (specify the username for `example_user`):

```
$ aap-gateway-manage revoke_oauth2_tokens --user example_user
```
To revoke all OAuth2 tokens and refresh token for the user with `id=example_user`:

```
$ aap-gateway-manage revoke_oauth2_tokens --user example_user --revoke_refresh
```

## `cleartokens`

Use the cleartokens command to delete all sessions that have expired.

For more information, see [cleartokens](https://django-oauth-toolkit.readthedocs.io/en/latest/management_commands.html) in Django’s Oauth Toolkit documentation.

## `clearsessions`

Use the `cleartokens` command to delete all sessions that have expired.

For more information, see [Clearing the session store](https://docs.djangoproject.com/en/4.2/topics/http/sessions/#clearing-the-session-store) in Django’s Oauth Toolkit documentation.

For more information about OAuth2 token management in the UI, see the [Applications](/documentation/en-us/red_hat_ansible_automation_platform/2.6/secure-assembly_gw_token_based_authentication#assembly-controller-applications "Create and configure token-based authentication for external applications such as ServiceNow and Jenkins. With token-based authentication, external applications can easily integrate with Ansible Automation Platform.").
