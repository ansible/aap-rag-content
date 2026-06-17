# Understanding the platform gateway OpenAPI specification

Platform gateway serves as the single entry point for Ansible Automation Platform, unifying the user interface and routing all API traffic to services such as automation controller, Event-Driven Ansible, and automation hub.

The OpenAPI specification provides a standardized, machine-readable definition of the unified API endpoints available through platform gateway. It is essential for external developers and automation engineers building reliable custom integrations.

**Key roles of the specification**

The OpenAPI specification ensures successful integration by fulfilling the following roles:

- **Enables custom integrations**: Developers use the specification to understand endpoint structures, required parameters, and response schemas, which is needed for building custom applications and third-party tools.
- **Ensures API longevity**: Integration with the platform gateway API future-proofs custom applications against disruptions that might occur when legacy, direct-access component APIs are retired.
- **Defines core functions**: The specification details endpoints that support fundamental operational and administrative functions, including:
* Platform health, such as `/api/gateway/v1/status/`.
* Activity monitoring, such as `/api/gateway/v1/activitystream/`.
* Configuration management, such as authentication configuration and role-based access control assignments.

## Download the platform gateway OpenAPI specification

You can download the OpenAPI specification by using the `curl` command from the schema endpoint.

### Before you begin

Token authentication is the recommended method for programmatic API use.

1. Create a Personal Access Token (PAT): From the navigation panel, select Access Management> (and then)Users, select your user, go to the **Tokens** tab, and click Create token.
2. Copy the generated token value. Use this value as the `<OAUTH2_TOKEN_VALUE>` in the following commands.

### Procedure

Retrieve the OpenAPI specification from the schema endpoint located at `<https://$AAP_INSTANCE/api/gateway/v1/docs/schema/>`, using one of the following methods:

- Get the YAML specification (Default format): To download the specification as a YAML file, run the following command:

```
curl -o "gateway_openapi_spec.yaml" "https://$AAP_INSTANCE/api/gateway/v1/docs/schema/"
```

- Get the JSON specification (Optional format): To explicitly request the specification in JSON format, append `?format=json` to the URL path and run the following command:

```
curl -o "gateway_openapi_spec.json" "https://$AAP_INSTANCE/api/gateway/v1/docs/schema/?format=json"
```
Important:
Replace `$AAP_INSTANCE` with your Ansible Automation Platform hostname in the commands.
