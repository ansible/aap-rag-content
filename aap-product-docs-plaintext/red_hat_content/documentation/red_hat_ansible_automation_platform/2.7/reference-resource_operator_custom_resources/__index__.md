# Resource Operator custom resources

The Resource Operator provides custom resources that enable you to manage automation controller resources directly from your Kubernetes cluster using a declarative, GitOps-compatible workflow.

Resource Operator custom resources connect to the platform gateway to create and manage automation resources such as jobs, templates, projects, inventories, credentials, schedules, and workflows. All Resource Operator custom resources require a `connection_secret` that references a Kubernetes secret containing the platform gateway URL and an OAuth2 token.

By defining automation resources as Kubernetes custom resources, you can manage them alongside your other cluster resources using standard Kubernetes tools and practices, including version control and continuous delivery pipelines.

