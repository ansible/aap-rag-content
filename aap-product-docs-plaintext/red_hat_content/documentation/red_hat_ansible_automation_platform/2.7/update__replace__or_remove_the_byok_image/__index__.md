# Update or replace the BYOK image

When your organization's documentation changes, you can update or replace the deployed BYOK image with the latest image, or remove it entirely.

## Before you begin

You have deployed a BYOK RAG image on a container-based or operator-based AAP 2.7 installation.

## Procedure

1.  Rebuild the BYOK RAG image using the latest version of your documentation by following the steps in [Build a searchable knowledge base image from your documentation](/documentation/en-us/red_hat_ansible_automation_platform/2.7/extend-build_a_searchable_knowledge_base_image_from_your_documentation "The rag-content tool converts your documentation into a vector database that the intelligent assistant uses to retrieve relevant content when responding to queries. Use this procedure to download the tool version best suited to your system's hardware.").
2.  Publish the new version to your registry.
3.  Update the BYOK image reference in your Ansible configuration.
4.  Restart the intelligent assistant service (rerun the installer) to pick up the new image. The BYOK configuration persists and does not require reconfiguration after restarting.

## Remove the BYOK image

An administrator can remove the deployed BYOK RAG image. With this removal, the intelligent assistant reverts to using the default Ansible Automation Platform 2.7 documentation.

### Procedure

1.  Remove the BYOK image configuration from your installation variables.
2.  Re-run the installer, which restarts the service with the new configuration. The intelligent assistant resumes operating with only the default Ansible Automation Platform 2.7 documentation RAG pipeline.
