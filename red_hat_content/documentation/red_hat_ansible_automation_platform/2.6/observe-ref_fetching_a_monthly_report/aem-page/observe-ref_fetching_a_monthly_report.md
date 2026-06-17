+++
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/observe-ref_fetching_a_monthly_report"
title = "Configure a monthly usage report - Red Hat Ansible Automation Platform 2.6"
template = "docs/aem-title.html"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/observe-assembly_metrics_utility/", "Generate consumption-based billing reports with the metrics-utility"]]
category = "Observe"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/observe-ref_fetching_a_monthly_report/aem-page/observe-ref_fetching_a_monthly_report.html"
last_crumb = "Configure a monthly usage report"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Configure a monthly usage report"
oversized = "false"
page_slug = "observe-ref_fetching_a_monthly_report"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/observe-ref_fetching_a_monthly_report"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/observe-ref_fetching_a_monthly_report/toc/toc.json"
type = "aem-page"
+++

# Configure a monthly usage report

You can fetch a monthly report from Ansible Automation Platform to gather usage metrics and create a consumption-based billing report. To fetch a monthly report on Red Hat Enterprise Linux or on OpenShift Container Platform, use the following procedures:

## Fetch a monthly report on Red Hat Enterprise Linux

Use the following procedure to fetch a monthly report on Red Hat Enterprise Linux:

### Procedure

 Run: `scp -r username@controller_host:$METRICS_UTILITY_SHIP_PATH/data/<YYYY>/<MM>/ /local/directory/`

### Results

The system saves the generated report as `CCSP-<YEAR>-<MONTH>.xlsx` in the ship path that you specified.

## Fetch a monthly report on OpenShift Container Platform from the Ansible Automation Platform Operator

Run a dedicated Ansible Playbook to fetch monthly usage reports directly from the OpenShift Container Platform persistent volume claim. This helps ensure accurate consumption-based billing and compliance.

### Procedure

 Use the following playbook to fetch a monthly consumption report for Ansible Automation Platform on OpenShift Container Platform:

Note:

To use this playbook, you must have the `kubernetes.core.k8s` collection installed on your machine.

```
# Requires Ansible and Kubernetes.core collection
- name: Copy directory from Kubernetes PVC to local machine
  hosts: "{{ host | default(omit) }}"

  vars:
    report_dir_path: "/mnt/metrics/reports/{{ year }}/{{ month }}/"
    data_files_dir_path: "/mnt/metrics/data/{{ year }}/{{ month }}/{{ day }}"

  tasks:
    - name: Create a temporary pod to access PVC data
      kubernetes.core.k8s:
        definition:
          apiVersion: v1
          kind: Pod
          metadata:
            name: temp-pod
            namespace: "{{ namespace_name }}"
          spec:
            containers:
              - name: busybox
                image: busybox
                command: ["/bin/sh"]
                args: ["-c", "sleep 3600"]  # Keeps the container alive for 1 hour
                volumeMounts:
                  - name: "{{ pvc }}"
                    mountPath: "/mnt/metrics"
            volumes:
              - name: "{{ pvc }}"
                persistentVolumeClaim:
                  claimName: automationcontroller-metrics-utility
            restartPolicy: Never
      register: pod_creation

    - name: Wait for both initContainer and main container to be ready
      kubernetes.core.k8s_info:
        kind: Pod
        namespace: "{{ namespace_name }}"
        name: temp-pod
      register: pod_status
      until: >
        pod_status.resources[0].status.containerStatuses[0].ready
      retries: 30
      delay: 10

    - name: Create a tarball of the directory of the report in the container
      kubernetes.core.k8s_exec:
        namespace: "{{ namespace_name }}"
        pod: temp-pod
        container: busybox
        command: tar czf /tmp/metrics.tar.gz -C "{{ report_dir_path }}" .
      register: tarball_creation

    - name: Create a tarball of the directory of the data files in the container
      kubernetes.core.k8s_exec:
        namespace: "{{ namespace_name }}"
        pod: temp-pod
        container: busybox
        command: tar czf /tmp/data_files.tar.gz -C "{{ data_files_dir_path }}" .
      register: tarball_creation_files

    - name: Copy the report tarball from the container to the local machine
      kubernetes.core.k8s_cp:
        namespace: "{{ namespace_name }}"
        pod: temp-pod
        container: busybox
        state: from_pod
        remote_path: /tmp/metrics.tar.gz
        local_path: "{{ local_dir }}/metrics.tar.gz"
      when: tarball_creation is succeeded

    - name: Copy the data files tarball from the container to the local machine
      kubernetes.core.k8s_cp:
        namespace: "{{ namespace_name }}"
        pod: temp-pod
        container: busybox
        state: from_pod
        remote_path: /tmp/data_files.tar.gz
        local_path: "{{ local_dir }}/data_files.tar.gz"
      when: tarball_creation_files is succeeded

    - name: Ensure the local directory exists
      ansible.builtin.file:
        path: "{{ local_dir }}"
        state: directory
        mode: '0755'

    - name: Extract the report tarball on the local machine
      ansible.builtin.unarchive:
        src: "{{ local_dir }}/metrics.tar.gz"
        dest: "{{ local_dir }}"
        remote_src: true
        extra_opts: "--strip-components=1"
      when: tarball_creation is succeeded

    - name: Extract the data files tarball on the local machine
      ansible.builtin.unarchive:
        src: "{{ local_dir }}/data_files.tar.gz"
        dest: "{{ local_dir }}"
        remote_src: true
        extra_opts: "--strip-components=1"
        list_files: true
      register: unarchive_result
      when: tarball_creation_files is succeeded

    - name: Extract the extracted data files tarball on the local machine
      ansible.builtin.unarchive:
        src: "{{ local_dir }}/{{ item }}"
        dest: "{{ local_dir }}"
        remote_src: true
        extra_opts: "--strip-components=1"
      loop: "{{ unarchive_result.files }}"
      when: tarball_creation_files is succeeded
      ignore_errors: true  # noqa ignore-errors

    - name: Delete the temporary pod
      kubernetes.core.k8s:
        api_version: v1
        kind: Pod
        namespace: "{{ namespace_name }}"
        name: temp-pod
        state: absent
```
