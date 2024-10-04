# Red Hat Ansible Automation Platform Documentation

Welcome to the source for Ansible Automation Platform technical content.
This repository contains technical content synchronized from various repositories and then converted into asciidoc.
This repository also contains content from the former AAP repository in the RedHatInsights org: https://github.com/RedHatInsights/red-hat-ansible-automation-platform-documentation

# Contributing

We welcome contributions to the Red Hat Ansible Automation Platform documentation. You can either open an issue for discussion, or submit an update using the steps below. This section describes the workflow and provides resources for Red Hat style and documentation architecture conventions.

## Authoring modularly structured documentation

Documentation follows a modular-based content model, providing a structure for writing and presenting user-story-based documentation. User-story-based documentation attempts to address the reader&#8217;s needs more than focusing on feature-based documentation. This is accomplished using a set of templates for concepts, references, procedures and assemblies. Templates can be found here.

 Repository Organization

.
|
├── downstream
│   ├── aap-common
│   │   ├── assembly-aap-common.adoc
│   │   ├── external-site-disclaimer.adoc
│   │   ├── making-open-source-more-inclusive.adoc
│   │   └── providing-feedback.adoc
│   ├── archive
│   │   ├── archived-aap-common
│   │   ├── archived-assemblies
│   │   ├── archived-images
│   │   ├── archived-modules
│   │   └── archived-titles
│   ├── assemblies
│   │   ├── platform-component1
│   │   └── platform-component2
│   │       ├── assembly-title-1.adoc
│   │       └── assembly-title-2.adoc
│   ├── attributes
│   │   └── attributes.adoc
│   ├── images
│   │   ├── image-1.png
│   │   └── image-2.png
│   ├── modules
│   │   ├── platform-component1
│   │   └── platform-component2
│   │       ├── module-title-1.adoc
│   │       └── module-title-2.adoc
|   ├── snippets
|   ├── templates
|   ├── titles
│   │   ├── platform-component1
│   │   └── platform-component2
│   │        ├── title-1.adoc
│   │        └── title-2.adoc
├── titles/release-notes-gcp
├── LICENSE.txt
└── README.adoc

The top-level directories are:

* downstream: Contains Red Hat Ansible Automation Platform modules, assemblies, and titles in these sub-folders:
* aap-common: Contains modules and attributes that are shared across Red Hat Ansible Automation branches.
You should modify content in the common folder on the main branch only.
* archive: A directory for archived files and images.
* assemblies: A directory for all assemblies, each in its own AsciiDoc file.
Assemblies are collections of modules linked together.
Platform assemblies are grouped by component.
* attributes: A common directory for attribute files.
* images: A directory for all images and other digital content.
* modules: A directory for all modules, each one in its own AsciiDoc file.
Platform modules are grouped by component.
* snippets: A directory for all snippets created.
* templates: A directory for templates used by controller, hub, and operator.
* titles: A directory for titles (information units, e.g, install guide, user guide).
Contains master.adoc files and symbolic links to the assemblies and modules directories.
Platform titles are grouped by component or feature.
* release-notes: Contains release note content.

## Red Hat Documentation Asciidoc Mark-up Conventions

Red Hat Ansible Automation Platform documentation is written in Asciidoc. See Red Hat Documentation Asciidoc Mark-up Conventions to learn more about implementing Asciidoc in your writing.

## Red Hat product documentation style conventions

The Red Hat Customer Content Services team uses the Red Hat supplementary style guide for product documentation and The IBM Style Guide as its primary sources for technical writing conventions and style guidelines. Refer first to the Red Hat supplementary style guide for product documentation for style guidance and conventions. If a topic is not included there, it means we follow the convention as established in the IBM Style Guide.

## Submitting an update

These instructions show how to submit an update using the command line. You may also use the GitHub web interface for the update. Whichever method you choose, the update should be submitted as a pull request.

Before you begin:

* You must have a GitHub account.
* You must have set up an SSH key for your GitHub account.

The first time you contribute:

1. Fork the repository.

From the main page of the link:https://github.com/ansible/aap-docs[GitHub repository], click btn[Fork] in the upper right corner.
2. Clone the forked repository locally.


```
$ git clone git@github.com:<username>/red-hat-ansible-automation-platform-documentation.git
```


If this command fails, be sure that you have link:https://docs.github.com/en/github/authenticating-to-github/adding-a-new-ssh-key-to-your-github-account[set up an SSH key for GitHub].

1. Navigate to the red-hat-ansible-automation-platform-documentation directory.
2. Set the upstream remote repository.

-----
$ git remote add -f upstream git@github.com:ansible/aap-docs.git
-----

To submit an update:

1. Fetch the latest changes.

-----
$ git fetch upstream
-----
2. Check out a branch from upstream/main


```
$ git checkout -b <new-branch> upstream/main
```


1. Make your edits.

Add or edit files as needed.
2. Stage the changes for each file.


```
 $ git add <file-name>
```


1. Commit the changes.

-----
  $ git commit -m "<descriptive-commit-message>"
-----
2. Push the changes to your forked repository.


```
$ git push origin HEAD
```


1. Open a pull request.

Typically the previous command gives the URL to open a pull request. If not, you can open one from the link:https://github.com/ansible/aap-docs/pulls[Pull requests] tab of the GitHub UI.

After you submit a pull request, it will be reviewed by members of this project.

## Building the guide

You must have asciidoctor installed. See the Asciibinder documentation for more information on installing Asciibinder.

1. Navigate to the red-hat-ansible-automation-platform-documentation directory.
2. Use the following command to build the guide:


```
$ asciidoctor master.adoc
```


This generates a master.html file that you can now view in a browser.

# Contacts

For questions or comments about Red Hat Ansible Automation Platform Documentation documentation, please contact:

ccs-ansible-docs@redhat.com

# License

This work is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License.