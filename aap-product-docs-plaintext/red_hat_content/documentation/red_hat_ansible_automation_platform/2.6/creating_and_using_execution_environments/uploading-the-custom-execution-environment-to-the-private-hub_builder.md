# 5. Populating your private automation hub container registry
## 5.1. Uploading the custom execution environment to the private hub




Before the new execution environment image can be used for automation jobs, it must be uploaded to the private automation hub.

**Procedure**

1. First, verify that the execution environment image can be seen in the local Podman cache:


```
$ podman images --format "table {{.ID}} {{.Repository}} {{.Tag}}"    IMAGE ID	    REPOSITORY					              TAG    b38e3299a65e	private-hub.example.com/custom-ee     	  latest    8e38be53b486	private-hub.example.com/ee-minimal-rhel8  latest
```


1. Then log in to the private automation hub’s container registry and push the image to make it available for use with job templates and workflows:


```
$ podman login private-hub.example.com -u admin    Password:    Login Succeeded!    $ podman push private-hub.example.com/custom-ee:latest
```




Use the following workflow to populate your private automation hub remote registry:

1.  [Pull execution environments for use in automation hub](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/managing_automation_content/managing-containers-hub#obtain-images)
1.  [Tag execution environment for use in automation hub](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/managing_automation_content/managing-containers-hub#tag-pulled-images)
1.  [Push an execution environment to private automation hub](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/managing_automation_content/managing-containers-hub#push-containers)
1.  [Set up your container repository](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/managing_automation_content/managing-containers-hub#setting-up-container-repository)
1.  [Add a README to your container repository](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/managing_automation_content/managing-containers-hub#proc-doing-one-procedure_assembly-keyword)
1.  [Provide access to your automation execution environmentss](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/managing_automation_content/managing-containers-hub#providing-access-to-containers)
1.  [Tag container images](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/managing_automation_content/managing-containers-hub#proc-tag-image)
1.  [Create a credential](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/managing_automation_content/managing-containers-hub#proc-create-credential)
1.  [Pulling images from a container repository](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/managing_automation_content/managing-containers-hub#pulling-images-container-repository)
1.  [Pull an image](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/managing_automation_content/managing-containers-hub#pulling-image)
1.  [Sync images from a container repository](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/html/managing_automation_content/managing-containers-hub#proc-sync-image-adoc_pulling-images-container-repository)


**Additional resources**

-  [Red Hat Container Registry Authentication](https://access.redhat.com/articles/RegistryAuthentication)


