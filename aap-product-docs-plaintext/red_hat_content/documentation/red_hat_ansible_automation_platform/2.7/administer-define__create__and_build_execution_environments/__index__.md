# Define, create, and build execution environments

Run automation consistently across nodes with execution environments, which are container images that contain everything you need to run your automation.

An execution environment is a containerized runtime that provides the following benefits:

- A consistent environment in which to run automation jobs
- Portability and scalability, as you can run automation jobs on any node, including controller and execution nodes
- Security and governance, as you can control what's inside the runtime environment; and you can have approved, signed, and verified container images
- Improved efficiency, as developers need not spend time troubleshooting environment dependencies

An automation execution environment should contain the following::

- Ansible Core 2.16 or later
- Python 3.12 or later
- Ansible Runner
- System dependencies

Ansible Builder is a command line tool that automates the process of building automation execution environments by using metadata defined in various Ansible Collections or created by the user. You build an execution environment before you can create it using automation controller. After building it, you push it to a repository (such as quay) and then, when creating an execution environment in the UI with automation controller, you must point to that repository to use it in Ansible Automation Platform to use it, for example, in a job template.

With Ansible Builder, you can easily create a customizable automation execution environments definition file that specifies the content you want included in your automation execution environments such as Ansible Core, Python, Collections, third-party Python requirements, and system level packages. This enables you to fulfill all of the necessary requirements and dependencies to get jobs running.

Red Hat provides the following pre-built execution environment images:

**ee-minimal**

Contains ansible-core and Ansible Runner, but does not include collections or other content beyond the minimum required dependencies. Use ee-minimal as the base image when you build custom execution environments. This gives you full control over which collections and dependencies are included. ee-minimal images are available for ansible-core 2.16 and 2.20.

Ansible-core 2.18 is available through version-less images only.

**ee-supported**

Contains ansible-core 2.16 and a curated set of Red Hat Certified Ansible Content Collections and their dependencies. Red Hat recommends that you build your own custom execution environments with only the collections you need. You can use ee-supported when you want a ready-to-use execution environment that covers common automation use cases without building a custom image.

ee-supported is available for ansible-core 2.16 only.

For most custom execution environment builds, use ee-minimal as the base image. This approach keeps the image size small and gives you explicit control over every collection, Python package, and system dependency.

