# Fine-tune Receptor worker backoff strategies for API reliability

Configure the Receptor worker within the Ansible Automation Platform Operator through the`RECEPTOR_KUBE_RETRY_COUNT` environment variable. This variable controls how the worker handles Kubernetes API connection failures.

Note:

The retry mechanism uses an exponential backoff strategy which is capped at 5 minutes to prevent excessive wait times during job execution errors.

*Table 1. RECEPTOR_KUBE_RETRY_COUNT details*

| Variable                    | Description                                                                                                                                                                         | Default value | Valid range |
| --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- | ----------- |
| `RECEPTOR_KUBE_RETRY_COUNT` | Sets the maximum number of retry attempts for Kubernetes API operations within the Receptor worker. Retry delays increase using exponential backoff with a Fibonacci-like sequence. | 5             | 1-100       |
