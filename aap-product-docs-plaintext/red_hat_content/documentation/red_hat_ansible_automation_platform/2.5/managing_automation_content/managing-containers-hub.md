# Chapter 3. Manage containers in private automation hub




Private automation hub functions as an internal container registry for your organization. It allows you to store, manage, and govern the container images, or automation execution environments, that your teams use to run automation.

To effectively manage these containers, first learn the difference between the two types of registries in your workflow:

External registries (Source): Public or third-party registries where you source your initial images. Common examples include the Red Hat Ecosystem Catalog (registry.redhat.io) or Quay.io. You can pull images from these registries to your local environment.

Private automation hub registry, or your "remote" registry (Destination): Your internal, secure registry hosted on private automation hub. You push your curated and approved images here. Your Ansible Automation Platform infrastructure then pulls these images from private automation hub to execute jobs.

