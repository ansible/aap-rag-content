+++
title = "Access log information - Red Hat Ansible Automation Platform 2.6"
template = "docs/aem-title.html"
path = "/documentation/en-us/red_hat_ansible_automation_platform/2.6/observe-assembly_controller_log_files"

[extra]
breadcrumbs = [["/", "Home"], ["/products", "Product Documentation"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.7", "Red Hat Ansible Automation Platform"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6", "2.6"], ["/documentation/en-us/red_hat_ansible_automation_platform/2.6/observe-assembly_controller_log_files/", "Access log information"]]
category = "Observe"
category_description = ""
document_kind = "documentation"
html = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/observe-assembly_controller_log_files/aem-page/observe-assembly_controller_log_files.html"
last_crumb = "Access log information"
modified = "2026-05-21T14:12:12.122Z"
multi_page_path = ""
name = "Access log information"
oversized = "false"
page_slug = "observe-assembly_controller_log_files"
portal_content_subtype = "title"
product = "Red Hat Ansible Automation Platform"
product_slug = "red_hat_ansible_automation_platform"
product_version = "2.6"
reference_url = "https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/observe-assembly_controller_log_files"
solr_index = "true"
toc = "data/docs_assets_aem/red_hat_ansible_automation_platform/2.6/observe-assembly_controller_log_files/toc/toc.json"
type = "aem-page"
+++

# Access log information

Automation controller logs are accessed in different ways depending on whether you have an RPM-based or containerized installation of Ansible Automation Platform.

## Access automation controller logs for containerized Ansible Automation Platform

Logs for containerized Ansible Automation Platform are not saved to specific files. The application logs are sent to the container `stdout` and handled by Podman with `journald`.

The three containers associated with automation controller are:

-  `automation-controller-rsyslog`
-  `automation-controller-task`
-  `automation-controller-web`


For more information about the purpose of each of these containers and how to inspect the logs, see [Diagnosing the problem](/documentation/en-us/red_hat_ansible_automation_platform/2.6/troubleshoot-assembly_appendix_troubleshoot_containerized_aap#diagnosing-the-problem "For general container-based troubleshooting, you can inspect the container logs for any running service to help troubleshoot underlying issues.") in *Containerized installation*.

## Access automation controller logs for RPM-based Ansible Automation Platform

Automation controller logfiles can be accessed from two centralized locations:

-  `/var/log/tower/`
-  `/var/log/supervisor/`


In the `/var/log/tower/` directory, you can view logfiles captured by:

- **tower.log:** Captures the log messages such as runtime errors that occur when the job is executed.
- **callback_receiver.log:** Captures callback receiver logs that handles callback events when running ansible jobs.
- **dispatcher.log:** Captures log messages for the automation controller dispatcher worker service.
- **job_lifecycle.log:** Captures details of the job run, whether it is blocked, and what condition is blocking it.
- **management_playbooks.log:** Captures the logs of management playbook runs, and isolated job runs such as copying the metadata.
- **rsyslog.err:** Captures rsyslog errors authenticating with external logging services when sending logs to them.
- **task_system.log:** Captures the logs of tasks that automation controller is running in the background, such as adding cluster instances and logs related to information gathering or processing for analytics.
- **tower_rbac_migrations.log:** Captures the logs for rbac database migration or upgrade.
- **tower_system_tracking_migrations.log:** Captures the logs of the controller system tracking migration or upgrade.
- **wsbroadcast.log:** Captures the logs of WebSocket connections in the controller nodes.


In the `/var/log/supervisor/` directory, you can view logfiles captured by:

- **awx-callback-receiver.log:** Captures the log of callback receiver that handles callback events when running ansible jobs, managed by `supervisord`.
- **awx-daphne.log:** Captures the logs of WebSocket communication of WebUI.
- **awx-dispatcher.log:** Captures the logs that occur when dispatching a task to an automation controller instance, such as when running a job.
- **awx-rsyslog.log:** Captures the logs for the `rsyslog` service.
- **awx-uwsgi.log:** Captures the logs related to uWSGI, which is an application server.
- **awx-wsbroadcast.log:** Captures the logs of the WebSocket service that is used by automation controller.
- **failure-event-handler.stderr.log:** Captures the standard errors for `/usr/bin/failure-event-handler` supervisord’s subprocess.
- **supervisord.log:** Captures the logs related to `supervisord` itself.
- **wsrelay.log:** Captures the communication logs within the WebSocket relay server.
- **ws_heartbeat.log:** Captures the periodic checks on the health of services running on the host.
- **rsyslog_configurer.log:** Captures rsyslog configuration activity associated with authenticating with external logging services.


The `/var/log/supervisor/` directory includes `stdout` files for all services as well.

You can expect the following log paths to be generated by services used by automation controller (and Ansible Automation Platform):

-  **/var/log/nginx/**
-  **/var/lib/pgsql/data/pg_log/**
-  **/var/log/redis/**


 **Troubleshooting**

Error logs can be found in the following locations:

- Automation controller server errors are logged in `/var/log/tower`.
- Supervisors logs can be found in `/var/log/supervisor/`.
- Nginx web server errors are logged in the httpd error log.
- Configure other automation controller logging needs in `/etc/tower/conf.d/`.


Explore client-side issues by using the JavaScript console built into most browsers and report any errors to Ansible through the Red Hat Customer portal at: <https://access.redhat.com/>.
