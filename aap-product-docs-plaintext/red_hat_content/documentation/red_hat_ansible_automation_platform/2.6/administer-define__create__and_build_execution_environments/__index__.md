# Define, create, and build execution environments

Run automation consistently across nodes with execution environments, which are container images that contain everything you need to run your automation.

An execution environment is a containerized runtime that provides the following benefits:

- A consistent environment in which to run automation jobs
- Portability and scalability, as you can run automation jobs on any node, including controller and execution nodes
- Security and governance, as you can control what's inside the runtime environment; and you can have approved, signed, and verified container images
- Improved efficiency, as developers need not spend time troubleshooting environment dependencies

Execution environments contain:

- Ansible core
- Required collections
- Python and other system dependencies
- Other libraries that your automation may require

Ansible Builder is a command line tool that automates the process of building automation execution environments by using metadata defined in various Ansible Collections or created by the user. You build an execution environment before you can create it using automation controller. After building it, you push it to a repository (such as quay) and then, when creating an execution environment in the UI with automation controller, you must point to that repository to use it in Ansible Automation Platform to use it, for example, in a job template.

With Ansible Builder, you can easily create a customizable automation execution environments definition file that specifies the content you want included in your automation execution environments such as Ansible Core, Python, Collections, third-party Python requirements, and system level packages. This enables you to fulfill all of the necessary requirements and dependencies to get jobs running.
