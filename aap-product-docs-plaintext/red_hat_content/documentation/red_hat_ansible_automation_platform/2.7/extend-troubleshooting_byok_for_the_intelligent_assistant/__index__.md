# Troubleshooting BYOK for the intelligent assistant

Resolve common issues when deploying or using BYOK with the intelligent assistant.

## Procedure

Begin by retrieving and reviewing the chatbot container logs.

For operator-based installations, run the following command to view the chatbot pod logs:

```
oc logs deployment/<aap-instance>-lightspeed-chatbot-api -n <aap_namespace>
```

In the log output, look for the following entries:

- `BYOK_IMAGE` is set: this confirms that the BYOK image is configured.
- `Knowledge_search` tool results indicate that the intelligent assistant is querying the BYOK RAG pipeline.
- Vector database initialization messages confirm that the BYOK database loaded correctly.
- Errors referring to a missing BYOK image indicate a configuration or deployment error.

