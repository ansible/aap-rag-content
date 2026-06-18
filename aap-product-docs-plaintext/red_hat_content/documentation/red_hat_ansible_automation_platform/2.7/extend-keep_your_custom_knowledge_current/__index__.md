# Keep your custom knowledge current

Administrators can update BYOK images to reflect their organization’s latest documentation changes. You can also remove the BYOK image entirely.

Note:

Updating your custom knowledge is optional.

**Identify the BYOK image in use**

When BYOK is enabled, at the beginning of the chatbot container log file, look for the BYOK logs section similar to the following:

```
BYOK_IMAGE is set: quay.io/<repository>/<byok-image-name>:<label>
Checking BYOK vector DB files...
BYOK FAISS DB file exists: /.llama/data/byok/distributions/ansible-chatbot/faiss_store.db
BYOK FAISS DB file size: 4.50 MB
BYOK FAISS DB file date/time: Apr 22 08:51
BYOK provider vector DB ID file exists:
/.llama/data/byok/distributions/ansible-chatbot/provider_vector_db_id.ind
BYOK provider vector DB ID: vs_88af3cff-aeb2-4159-bc12-cef9e8e8fccd
BYOK_PROVIDER_VECTOR_DB_ID already set: vs_88af3cff-aeb2-4159-bc12-cef9e8e8fccd
```
