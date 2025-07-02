# 3. Reviewing automation execution environments with automation content navigator
## 3.1. Reviewing automation execution environments from automation content navigator




You can review your automation execution environments with the automation content navigator text-based user interface.

**Prerequisites**

- Automation execution environments


**Procedure**

1. Review the automation execution environments included in your automation content navigator configuration.


```
$ ansible-navigator images
```

![List of automation execution environments](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_content_navigator-en-US/images/90e4e02d453e60534c4b15909c8f67d3/navigator-images-list.png)



1. Type the number of the automation execution environment you want to delve into for more details.

![Automation execution environment details](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_content_navigator-en-US/images/843fc84551c92a30484d2056db1c9716/navigator-image-details.png)


You can review the packages and versions of each installed automation execution environment and the Ansible version any included collections.


1. Optional: pass in the automation execution environment that you want to use. This becomes the primary and is the automation execution environment that automation content navigator uses.


```
$ ansible-navigator images --eei registry.example.com/example-enterprise-ee:latest
```




**Verification**

- Review the automation execution environment output.

![Automation execution environment output](https://access.redhat.com/webassets/avalon/d/Red_Hat_Ansible_Automation_Platform-2.5-Using_content_navigator-en-US/images/843fc84551c92a30484d2056db1c9716/navigator-image-details.png)





