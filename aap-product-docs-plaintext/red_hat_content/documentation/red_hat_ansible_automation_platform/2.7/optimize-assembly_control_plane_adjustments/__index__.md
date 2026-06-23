# Adjust the control plane to tune performance

The control plane refers to the automation controller pods which contain the web and task containers that, among other things, provide the user interface and handle the scheduling and launching of jobs.

On the automation controller custom resource, the number of *replicas* determines the number of automation controller pods in the automation controller deployment.

