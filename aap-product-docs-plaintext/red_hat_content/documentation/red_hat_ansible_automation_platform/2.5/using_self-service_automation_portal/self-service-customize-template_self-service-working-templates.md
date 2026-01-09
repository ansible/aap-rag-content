# 3. Working with templates
## 3.1. Customized self-service templates




Custom self-service templates are stored as YAML files in repositories in GitHub or Gitlab. When a user launches a software template from self-service automation portal, they must fill in a form with the values needed to run the associated job template in Ansible Automation Platform.

The custom self-service template YAML file must have a `token:` section that includes a `ui:field:` key for the authentication token for Ansible Automation Platform. This generates a field for the token in the form that appears when the user launches the template in self-service automation portal. The user enters the token: it is used to authenticate job template execution in Ansible Automation Platform.

The following example shows the `token:` section in a template. For security reasons, set the value of `token.ui:backstage.review.show` to `false` to ensure that the token is not visible to the user.

```
spec:
...
parameters:
...
properties:
token:
title: Token
type: string
description: Oauth2 token
ui:field: AAPTokenField
ui:widget: hidden
ui:backstage:
review:
show: false
```

Note
Setting the `ui:widget: hidden` field hides the Red Hat Ansible Automation Platform token input in the form.



