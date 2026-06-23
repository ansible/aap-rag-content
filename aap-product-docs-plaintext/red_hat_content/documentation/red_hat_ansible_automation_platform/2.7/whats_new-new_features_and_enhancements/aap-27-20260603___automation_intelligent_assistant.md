# New features and enhancements
## Automation intelligent assistant

- BYOK (bring-your-own-knowledge) to automation intelligent assistant RAG pipeline
* Customers can inject their own documentation into the automation intelligent assistant RAG pipeline
* The intelligent assistant can now reference a 2nd RAG image/repo when producing answers to the end-user
* The BYOK RAG image is the highest priority data to utilize as context, where the Ansible-documentation-based RAG image is the second priority data.
* The BYOK RAG image is built outside of the AAP deployment (build tool supports text and markdown files)
* Admins can manage BYOK images over time (update, replace, or remove)

