# Best practices for automation execution
## Continuous integration / Continuous deployment

Continuous Integration (CI) and Continuous Deployment (CD) are development practices that require developers to integrate code into a shared repository several times a day.

Each integration can then be verified by an automated build and automated tests. CI/CD is a method to deliver applications to customers by introducing automation into the stages of app development.

The main concepts attributed to CI/CD are continuous integration, continuous delivery, and continuous deployment. Automation controller can be integrated with CI/CD systems to enable automated provisioning, configuration management, application deployment, and other IT tasks as part of the CI/CD pipeline.

For a Continuous Integration system, such as Jenkins, to create a job, it must make a `curl` request to a job template. The credentials to the job template must not require prompting for any particular passwords.
