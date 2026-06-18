+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/ref_self_service_determine_version_tags"
title = "Determine version tags before you install - Red Hat Ansible Automation Platform 2.7"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"]]
category = ""
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/ref_self_service_determine_version_tags/aem-page/ref_self_service_determine_version_tags.html"
last_crumb = "Determine version tags before you install"
modified = "2026-06-05T07:48:10.594Z"
multi_page_path = ""
name = "Determine version tags before you install"
oversized = "false"
page_slug = "ref_self_service_determine_version_tags"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/ref_self_service_determine_version_tags"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/ref_self_service_determine_version_tags/toc/toc.json"
type = "aem-page"
+++

# Determine version tags before you install

Record the version values that you need before you install the Helm chart or mirror images for Ansible automation portal.

| Value                                                                                    | Where to find it                                                                                                                                                                                                                                                              |
| ---------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Supported portal, Ansible Automation Platform, and OpenShift Container Platform versions | Ansible automation portal lifecycle page (for example, portal version `2.1`).                                                                                                                                                                                                 |
| Helm chart version                                                                       | OpenShift **Helm** catalog when you create the release, or run `helm search repo openshift-helm-charts/redhat-rhaap-portal`.                                                                                                                                                  |
| `imageTagInfo` (`<plugin-version>`)                                                      | Default in the chart **YAML** view, or run `helm show values openshift-helm-charts/redhat-rhaap-portal --version <chart-version>` and find the value under `redhat-developer-hub.global.imageTagInfo`.                                                                        |
| `<platform-version>` (application image and catalog index)                               | Run `helm template <release-name> openshift-helm-charts/redhat-rhaap-portal --version <chart-version> -f <values.yaml> | grep CATALOG_INDEX_IMAGE`. Use the tag on `plugin-catalog-index` (for example, `:1.9`) for the hub image, `mirror-plugins.sh`, and `--plugin-index`. |
