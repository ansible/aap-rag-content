# Workload types and access methods
## REST API access and client load

Ansible Automation Platform provides a REST API, offering access to all its functionalities. You can access this API by using various clients, including cURL, Python, Ansible Automation Platform configuration collections, or the Ansible URI module.

You can use the API to automate the following tasks:

- Launching jobs
- Updating inventories
- Checking automation status
- Pushing events into an Event Stream for Event-Driven Ansible
- Automating the upload or publication of collections in automation hub
- Managing automation execution environments in the automation hub container registry using a Podman client that connects to automation hub over its registry API


API clients apply load to the platform gateway proxy, the gRPC service for authentication, the web server of the targeted component, and the database, because most API client queries interact with the database.

To access the API, you can use the following common authentication methods: Basic authentication (using a username and password) and Token authentication (your chosen authentication method). Token authentication is recommended for better performance.

Use the platform gateway to create tokens and link them to an OAuth application or your account. The platform gateway’s gRPC service authenticates each request and directs it to the appropriate application server based on the specified route.
