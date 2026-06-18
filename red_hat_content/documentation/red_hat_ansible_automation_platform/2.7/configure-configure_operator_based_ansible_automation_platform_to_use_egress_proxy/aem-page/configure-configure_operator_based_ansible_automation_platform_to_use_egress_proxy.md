+++
title = "Configure operator-based Ansible Automation Platform to use egress proxy - Red Hat Ansible Automation Platform 2.7"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/configure-configure_operator_based_ansible_automation_platform_to_use_egress_proxy"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/configure-configure_a_proxy_to_communicate_with_external_systems/", "Configure a proxy to communicate with external systems"]]
category = "Configure"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/configure-configure_operator_based_ansible_automation_platform_to_use_egress_proxy/aem-page/configure-configure_operator_based_ansible_automation_platform_to_use_egress_proxy.html"
last_crumb = "Configure operator-based Ansible Automation Platform to use egress proxy"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Configure operator-based Ansible Automation Platform to use egress proxy"
oversized = "false"
page_slug = "configure-configure_operator_based_ansible_automation_platform_to_use_egress_proxy"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/configure-configure_operator_based_ansible_automation_platform_to_use_egress_proxy"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/configure-configure_operator_based_ansible_automation_platform_to_use_egress_proxy/toc/toc.json"
type = "aem-page"
+++

# Configure operator-based Ansible Automation Platform to use egress proxy

When installing Ansible Automation Platform using the operator-based installation method, you can configure the platform to use an egress proxy.

When creating an automationcontroller instance, select the YAML view and add `extra_settings` in the spec definition as the `AWX_TASK_ENV` parameter for the proxy settings, as follows:

```
apiVersion: automationcontroller.ansible.com/v1beta1
kind: AutomationController
metadata:
  name: example
  namespace: ansible-automation-platform
spec:
  create_preload_data: true
  route_tls_termination_mechanism: Edge
  garbage_collect_secrets: false
  ingress_type: Route
  loadbalancer_port: 80
  no_log: true
  image_pull_policy: IfNotPresent
  projects_storage_size: 8Gi
  auto_upgrade: true
  task_privileged: false
  projects_storage_access_mode: ReadWriteMany
  set_self_labels: true
  projects_persistence: false
  replicas: 1
  admin_user: admin
  loadbalancer_protocol: http
  nodeport_port: 30080
  extra_settings:
    - setting: AWX_TASK_ENV
      value:
        HTTPS_PROXY: 'https://192.168.0.XXX:3128'
        HTTP_PROXY: 'https://192.168.0.XXX:3128'
        NO_PROXY: 10.0.0.0/8
        http_proxy: 'https://192.168.0.XXX:3128'
        https_proxy: 'https://192.168.0.XXX:3128'
        no_proxy: 10.0.0.0/8
```

## Modify a deployed instance

Apply configuration changes to a deployed Automation Controller instance by updating the Operator settings and redeploying the pods to ensure your new environment variables take effect.

The configuration is stored as a ConfigMap resource. See it in the **OCP console > ConfigMaps > <instancename>-automationcontroller-configmap**.

To modify the settings after deployment, use the Operator.

After editing `extra_settings`, perform the deployment again.

Go to **OCP console > Deployments > your instance > Decrease the Pod count > Increase the Pod count**.

You can also redeploy it in the command line utility as follows:

```
oc scale --replicas=0 deployment.apps/<instancename> -n ansible-automation-platform deployment.apps/<instancename> scaled
oc scale --replicas=1 deployment.apps/<instancename> -n ansible-automation-platform deployment.apps/<instancename> scaled
```

**Verify**

See the settings in the Web UI at **Settings > Jobs settings > Extra Environment Variables**.

If you need to set another value, you can define it in the same way. `extra_settings` settings is stored statically in the `/etc/tower/settings.py` file in the`automationcontroller` instance.
