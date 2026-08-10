+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.7/upgrade-ref_migrate_tarball_to_oci_troubleshoot"
template = "docs/aem-title.html"
title = "Troubleshoot the migration - Red Hat Ansible Automation Platform 2.7"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "2.7"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7/upgrade-assembly_self_service_upgrading/", "Upgrade Ansible automation portal"]]
category = "Upgrade"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/upgrade-ref_migrate_tarball_to_oci_troubleshoot/aem-page/upgrade-ref_migrate_tarball_to_oci_troubleshoot.html"
last_crumb = "Troubleshoot the migration"
modified = "2026-07-30T17:12:56.473Z"
multi_page_path = ""
name = "Troubleshoot the migration"
oversized = "false"
page_slug = "upgrade-ref_migrate_tarball_to_oci_troubleshoot"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.7"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.7/upgrade-ref_migrate_tarball_to_oci_troubleshoot"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.7/upgrade-ref_migrate_tarball_to_oci_troubleshoot/toc/toc.json"
type = "aem-page"
+++

# Troubleshoot the migration

Diagnose and resolve common errors during the migration from HTTP plug-in registry to OCI container delivery.

## Authentication failures

**Symptom:** Init container logs show `authentication required` or `unauthorized: access denied`.

**Cause:** The `<release-name>-dynamic-plugins-registry-auth` secret is missing, malformed, or has incorrect credentials.

**Resolution:**

1. Verify the secret exists:

```
$ oc get secret <release-name>-dynamic-plugins-registry-auth -n <namespace>
```

2. Check the secret contents:

```
$ oc get secret <release-name>-dynamic-plugins-registry-auth \
  -o jsonpath='{.data.auth\.json}' -n <namespace> | base64 -d
```

     The output should be valid JSON with your credentials.

3. Ensure the secret name matches your Helm release name exactly. For example, if your release is `redhat-rhaap-portal`, the secret must be `redhat-rhaap-portal-dynamic-plugins-registry-auth`.

4. Recreate the secret with correct credentials if needed:

```
$ oc delete secret <release-name>-dynamic-plugins-registry-auth -n <namespace>
$ oc create secret generic <release-name>-dynamic-plugins-registry-auth \
  --from-file=auth.json=./auth.json -n <namespace>
```

## Duplicate registry path in OCI URLs

**Symptom:** Init container logs or Helm values show duplicate paths, for example: `oci://yb-artifactory/ansible-automation-platform/ansible-automation-platform/automation-portal:2.2`.

**Cause:** The `imageRegistry` value includes a repository path instead of being the registry host only.

**Resolution:** Edit your `backup-values.yaml` and set `imageRegistry` to the registry host only, without the repository path:

```yaml
# Incorrect (includes repository path):
imageRegistry: "yb-artifactory/ansible-automation-platform"

# Correct (host only):
imageRegistry: "yb-artifactory"
```

Then re-run `helm upgrade` with the corrected values file.

## x509 certificate errors for private registries

**Symptom:** Init container logs show `x509: certificate signed by unknown authority` or `x509: certificate has expired`.

**Cause:** Your mirror registry uses a self-signed or internal CA certificate that the `skopeo` utility cannot verify.

**Resolution:** Mount your CA certificate into the init container at the per-registry trust path. Obtain your CA certificate bundle (including the full chain), create a ConfigMap, and update your Helm values to mount it. For detailed instructions, see the RHDH documentation: [Install plugins from OCI registries by using custom certificates](https://redhat-developer.github.io/red-hat-developers-documentation-rhdh/main/plugins-rhdh-install/#rinstall-plugins-from-oci-registries-by-using-custom-certificates).

## No such image error

**Symptom:** Init container logs show `Error: no such image` or `manifest not found`.

**Cause:** The OCI image does not exist in the specified registry, or the `imageTagInfo` version does not match what is available.

**Resolution:**

1. Verify the `imageTagInfo` value in your Helm release matches an available version. Check the [Ansible automation portal lifecycle](https://access.redhat.com/page/ansible-automation-platform-self-service-automation-portal-lifecycle) page.
2. If using a mirror registry, ensure the image was mirrored to the correct path. Run:

```
$ podman search <your-mirror-registry>/ansible-automation-platform/automation-portal
```

3. Confirm that `imageRegistry` is set correctly and does not include a duplicate repository path (see the Duplicate registry path section above).

## Integrity check errors

**Symptom:** Init container logs show `integrity check failed` or `digest mismatch`.

**Cause:** The OCI image in your registry does not match the expected digest, or the image was corrupted during mirroring.

**Resolution:**

1. Re-mirror the image from `registry.redhat.io` using `skopeo copy` instead of `podman tag/push`. The `skopeo copy` command preserves the original manifest digest:

```
$ skopeo copy \
  docker://registry.redhat.io/ansible-automation-platform/automation-portal:<plugin-version> \
  docker://<your-mirror-registry>/ansible-automation-platform/automation-portal:<plugin-version>
```

2. If the error persists, verify the image in your mirror registry:

```
$ skopeo inspect docker://<your-mirror-registry>/ansible-automation-platform/automation-portal:<plugin-version>
```

3. Ensure you are not using a stale local image cache. Delete and re-pull if needed.

## Accessing init container logs

To view the logs of the `install-dynamic-plugins` init container:

```
$ oc get pods -n <namespace> -l app.kubernetes.io/component=backstage
$ oc logs <pod-name> -c install-dynamic-plugins -n <namespace>
```

If the pod has already completed (e.g., if the init container succeeded), you can view the previous logs:

```
$ oc logs <pod-name> -c install-dynamic-plugins --previous -n <namespace>
```

If the pod is still running, stream logs in real time:

```
$ oc logs -f <pod-name> -c install-dynamic-plugins -n <namespace>
```
