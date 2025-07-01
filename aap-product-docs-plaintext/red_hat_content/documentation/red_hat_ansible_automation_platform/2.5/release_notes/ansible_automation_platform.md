# 7. Known issues
## 7.1. Ansible Automation Platform




- Added the `    podman_containers_conf_logs_max_size` variable for **containers.conf** to control the max log size for Podman installations. The default value is 10 MiB. (AAP-12295)
- Setting the `    pg_host=` value without any other context no longer results in an empty HOST section of the **settings.py** in the automation controller. As a workaround, delete the `    pg_host=` value or set it to `    pg_host=''` . (AAP-31915)
- Using **Prompt on launch** for variables for job templates, workflow job templates, workflow visualizer nodes, and schedules will not show the default variables when launching the job, or when configuring the workflows and schedules. (AAP-30585)
- The unused **ANSIBLE_BASE_** settings are included as environment variables in the job execution. These variables suffixed with **SECRET** are no longer used in the Ansible Automation Platform and might be ignored until they are removed in a future patch. (AAP-32208)


