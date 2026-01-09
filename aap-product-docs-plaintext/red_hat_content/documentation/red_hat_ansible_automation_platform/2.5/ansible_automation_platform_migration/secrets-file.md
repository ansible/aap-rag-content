# 5. Migration artifact structure and verification
## 5.3. Secrets file




The `secrets.yml` file in the migration artifact includes essential Django `SECRET_KEY` values required for authentication between services.

Structure the secrets file as follows:

```
controller_pg_database: &lt;redacted&gt;
controller_secret_key: &lt;redacted&gt;
gateway_pg_database: &lt;redacted&gt;
gateway_secret_key: &lt;redacted&gt;
hub_pg_database: &lt;redacted&gt;
hub_secret_key: &lt;redacted&gt;
hub_db_fields_encryption_key: &lt;redacted&gt;
```

Note
Ensure the `secrets.yml` file is encrypted and kept in a secure location.



