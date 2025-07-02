# 5. Administering the Ansible Lightspeed Service
## 5.3. Configuring custom models
### 5.3.2. Creating a training data set by using the content parser tool




Use the content parser tool, a command-line interface (CLI) tool, to scan your existing Ansible files and generate a custom model training data set. The training data set includes a list of Ansible files and their paths relative to the project root. You can then upload this data set to IBM watsonx Code Assistant, and use it to create a custom model that is trained on your organization’s existing Ansible content.

#### 5.3.2.1. Methods of creating training data sets




You can generate a training data set by using one of the following methods:

-  **With ansible-lint preprocessing**

By default, the content parser tool generates training data sets by using ansible-lint preprocessing. The content parser tool uses ansible-lint rules to scan your Ansible files and ensure that the content adheres to Ansible best practices. If rule violations are found, the content parser tool excludes these files from the generated output. In such scenarios, you must resolve the rule violations, and run the content parser tool once again so that the generated output includes all your Ansible files.


-  **Without ansible-lint preprocessing**

You can generate a training data set without ansible-lint preprocessing. In this method, the content parser tool does not scan your Ansible files for ansible-lint rule violations; therefore, the training data set includes all files. Although the training data set includes all files, it might not adhere to Ansible best practices and could affect the quality of your code recommendation experience.




#### 5.3.2.2. Supported data sources




The content parser tool scans the following directories and file formats:

- Local directories
- Archived files, such as `    .zip` , `    .tar` , `    .tar.gz` , `    .tar.bz2` , and `    .tar.xz` files
- Git repository URLs (includes both private and public repositories)


#### 5.3.2.3. Process of creating a training data set




To create a custom model training data set, perform the following tasks:

1.  [Install the content parser tool on your computer](https://docs.redhat.com/en/documentation/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant/2.x_latest/html-single/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant_user_guide/index#install-content-parser_administering-ansible-lightspeed)
1.  [Generate a custom model training data set](https://docs.redhat.com/en/documentation/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant/2.x_latest/html-single/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant_user_guide/index#generate-training-data-set_administering-ansible-lightspeed)
1.  [View the generated training data set](https://docs.redhat.com/en/documentation/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant/2.x_latest/html-single/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant_user_guide/index#view-content-parser-output_administering-ansible-lightspeed)
1. (Optional: If you generated a training data set with ansible-lint preprocessing and detected ansible-lint rule violations) [Resolve ansible-lint rule violations](https://docs.redhat.com/en/documentation/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant/2.x_latest/html-single/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant_user_guide/index#resolve-ansible-lint-rule-violations_administering-ansible-lightspeed)
1. (Optional: If you generated multiple training data sets) [Merge multiple training data sets into a single JSONL file](https://docs.redhat.com/en/documentation/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant/2.x_latest/html-single/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant_user_guide/index#merge-multiple-jsonl-files_administering-ansible-lightspeed)


#### 5.3.2.4. Installing the content parser tool




Install the content parser tool, a command-line interface (CLI) tool, on your computer.

**Prerequisites**

Ensure that your computer has one of the following supported OS:


- Python version 3.10 or later.
- UNIX OS, such as Linux or Mac OS.

Note
Installation of the content parser tool on Microsoft Windows OS is not supported.



**Procedure**


1. Create a working directory and set up `        venv` Python virtual environment:

`        $ python -m venv ./venv`

`        $ source ./venv/bin/activate`


1. Install the latest version of the content parser tool from the `        pip` repository:

`        $ pip install --upgrade pip`

`        $ pip install --upgrade ansible-content-parser`


1. Perform one of the following tasks:


- To generate a training data set without ansible-lint preprocessing, see section [Generating a custom model training data set](https://docs.redhat.com/en/documentation/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant/2.x_latest/html-single/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant_user_guide/index#generate-training-data-set_administering-ansible-lightspeed) .
- To generate a training data set with ansible-lint preprocessing, ensure that you have the latest version of ansible-lint installed on your computer:


1. View the ansible-lint versions that are installed on your computer.

`                $ ansible-content-parser --version`

`                $ ansible-lint --version`

A list of application versions and their dependencies are displayed.


1. In the output, verify that the version of ansible-lint that was installed with the content parser tool is the same as that of the previously-installed ansible-lint. A mismatch in the installed ansible-lint versions causes inconsistent results from the content parser tool and ansible-lint.

For example, in the following output, the content parser tool installation includes ansible-lint version 6.20.0 which is a mismatch from previously-installed ansible-lint version 6.13.1:


```
$ ansible-content-parser --version                ansible-content-parser 0.0.1 using ansible-lint:6.20.0 ansible-core:2.15.4                $ ansible-lint --version                ansible-lint 6.13.1 using ansible 2.15.4                A new release of ansible-lint is available: 6.13.1 → 6.20.0
```


1. If there is a mismatch in the ansible-lint versions, deactivate and reactivate `                venv` Python virtual environment:

`                $ deactivate`

`                $ source ./venv/bin/activate`


1. Verify that the version of ansible-lint that is installed with the content parser tool is the same as that of the previously-installed ansible-lint:

`                $ ansible-content-parser --version`

`                $ ansible-lint --version`

For example, the following output shows that both ansible-lint installations on your computer are of version 6.20.0:


```
$ ansible-content-parser --version                ansible-content-parser 0.0.1 using ansible-lint:6.20.0 ansible-core:2.15.4                $ ansible-lint --version                ansible-lint 6.20.0 using ansible-core:2.15.4                ansible-compat:4.1.10 ruamel-yaml:0.17.32 ruamel-yaml-clib:0.2.7
```







#### 5.3.2.5. Generating a custom model training data set




After installing the content parser tool, run it to scan your custom Ansible files and generate a custom model training data set. You can then upload the training data set to IBM watsonx Code Assistant and create a custom model for your organization. If you used ansible-lint preprocessing and encountered rule violations, you must [resolve the rule violations](https://docs.redhat.com/en/documentation/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant/2.x_latest/html-single/red_hat_ansible_lightspeed_with_ibm_watsonx_code_assistant_user_guide/index#resolve-ansible-lint-rule-violations_administering-ansible-lightspeed) before uploading the training data set to IBM watsonx Code Assistant.

##### 5.3.2.5.1. Methods of generating a training data set




You can generate a training data set by using one of the following methods:

-  **With ansible-lint preprocessing**

By default, the content parser tool generates training data sets by using ansible-lint preprocessing. The content parser tool uses ansible-lint rules to scan your Ansible files and ensure that the content adheres to Ansible best practices. If rule violations are found, the content parser tool excludes these files from the generated output. In such scenarios, you must resolve the rule violations, and run the content parser tool once again so that the generated output includes all your Ansible files.


-  **Without ansible-lint preprocessing**

You can generate a training data set without ansible-lint preprocessing. In this method, the content parser tool does not scan your Ansible files for ansible-lint rule violations; therefore, the training data set includes all files. Although the training data set includes all files, it might not adhere to Ansible best practices and could affect the quality of your code recommendation experience.




**Prerequisites**

- You must have installed the content parser tool on your computer.
- You must have verified that the version of ansible-lint that is installed with the content parser tool is the same as that of the previously-installed ansible-lint.


**Procedure**

1. Run the content parser tool to generate a training data set:


- With ansible-lint preprocessing: `        $ ansible-content-parser<span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">source</span></em></span><span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">output</span></em></span>`
- Without ansible-lint preprocessing: `        $ ansible-content-parser<span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">source</span></em></span><span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">output</span></em></span><span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">-S</span></em></span>`

The following table lists the required parameters.

| Parameter | Description |
| --- | --- |
|  `<span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">source</span></em></span>` | Specifies the source of the training data set. |
|  `<span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">output</span></em></span>` | Specifies the output of the training data set. |
|  `<span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">-S</span></em></span>` or `<span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">--skip-ansible-lint</span></em></span>` | Specifies to skip ansible-lint preprocessing while generating the training data set. |



For example: If the source is a Github URL [https://github.com/ansible/ansible-tower-samples.git](https://github.com/ansible/ansible-tower-samples.git) , and the output directory is `    /tmp/out` , the command prompt is as follows:
`    $ ansible-content-parser<a class="link" href="https://github.com/ansible/ansible-tower-samples.git">https://github.com/ansible/ansible-tower-samples.git</a>/tmp/out`


1. Optional: To generate a training data set with additional information, specify the following parameters while running the content parser tool.

| Parameter | Description |
| --- | --- |
|  `--source-license` | Specifies to include the licensing information of the source directory in the training data set. |
|  `--source-description` | Specifies to include the descriptions of the source directory in the training data set. |
|  `--repo-name` | Specifies to include the repository name in the training data set. If you do not specify the repository name, the content parser tool automatically generates it from the source name. |
|  `--repo-url` | Specifies to include the repository URL in the training data set. If you do not specify the repository URL, the content parser tool automatically generates it from the source URL. |
|  `-v` or `--verbose` | Displays the console logging information. |


**Example of a command prompt for Github repository **ansible-tower-samples** **


```
$ ansible-content-parser --profile min \    --source-license undefined \    --source-description Samples \    --repo-name ansible-tower-samples \    --repo-url 'https://github.com/ansible/ansible-tower-samples' \    git@github.com:ansible/ansible-tower-samples.git /var/tmp/out_dir
```


**Example of a generated training data set for Github repository **ansible-tower-samples** **

The training data set is formatted with Jeff Goldblum (jg), a command-line JSON processing tool.



```
$ cat out_dir/ftdata.jsonl| jq    {    "data_source_description": "Samples",    "input": "---\n- name: Hello World Sample\n hosts: all\n tasks:\n - name: Hello Message",    "license": "undefined",    "module": "debug",    "output": " debug:\n msg: Hello World!",    "path": "hello_world.yml",    "repo_name": "ansible-tower-samples",    "repo_url": "https://github.com/ansible/ansible-tower-samples"    }
```




#### 5.3.2.6. Viewing the generated training data set




After the content parser tool scans your Ansible files, it generates the training data set in an output directory. The training data set includes a **ftdata.jsonl** file, which is the main output of the content parser tool. The file is available in JSON Lines file format, where each line entry represents a JSON object. You must upload this JSONL file to IBM watsonx Code Assistant to create a custom model.

##### 5.3.2.6.1. Structure of custom model training data set




The following is the file structure of an output directory:

```
output/
|-- ftdata.jsonl  # Training dataset<span id="CO1-2"><!--Empty--></span><span class="callout">1</span>|-- report.txt   # A human-readable report<span id="CO1-3"><!--Empty--></span><span class="callout">2</span>|
|-- repository/<span id="CO1-4"><!--Empty--></span><span class="callout">3</span>|     |-- (files copied from the source repository)
|
|-- metadata/<span id="CO1-5"><!--Empty--></span><span class="callout">4</span>|-- (metadata files generated during the execution)
```

**Where:**


###### 5.3.2.6.1.1. Using report.txt file to resolve ansible-lint rule violations




The **report.txt** file, that can be used to resolve ansible-lint rule violations, contains the following information:

- File counts per type: A list of files according to their file types, such as playbooks, tasks, handlers, and jinja2.
- List of Ansible files that were identified: A list of files identified by ansible-lint with a file name, a file type, and whether the file was excluded from further processing, or automatically fixed by ansible-lint.
- List of Ansible modules found in tasks: A list of modules identified by ansible-lint with a module name, a module type, and whether the file was excluded from further processing, or automatically fixed by ansible-lint.
- Issues found by ansible-lint: A list of issues along with a brief summary of ansible-lint execution results. If ansible-lint encounters files with syntax-check errors in the first execution, then it initiates a second execution and excludes the files with errors from the scan. You can use this information to resolve ansible-lint rule violations.


#### 5.3.2.7. Resolving ansible-lint rule violations




By default, the content parser tool uses ansible-lint rules to scan your Ansible files and ensure that the content adheres to Ansible best practices. If rule violations are found, the content parser tool excludes these files from the generated output. In such scenarios, it is recommended that you fix the files with rule violations before uploading the training data set to IBM watsonx Code Assistant.

By default, ansible-lint applies the rules that are configured in `ansible-lint/src/ansiblelint/rules` while scanning your Ansible files. For more information about ansible-lint rules, see the [Ansible Lint documentation](https://ansible.readthedocs.io/projects/lint/) .

##### 5.3.2.7.1. How does the content parser tool handle rule violations?




-  **Using autofixes**

The content parser tool runs ansible-lint with the `    --fix=all` option to perform autofixes, which can fix or simplify fixing issues identified by that rule.

If ansible-lint identifies rule violations that have an associated autofix, it automatically fixes or simplifies the issues that violate the rules. If ansible-lint identifies rule violations that do not have an associated autofix, it reports these instances as rule violations which you must fix manually. For more information about autofixes, see [Autofix](https://ansible.readthedocs.io/projects/lint/autofix/) in Ansible Lint Documentation.


-  **Using syntax-checks**

Ansible-lint also performs syntax checks while scanning your Ansible files. If any syntax-check errors are found, ansible-lint stops processing the files. For more information about syntax-check errors, see [syntax-check](https://ansible.readthedocs.io/projects/lint/rules/syntax-check/) in Ansible Lint Documentation.

The content parser tool handles syntax-check rule violations in the following manner:


- If `        syntax-check` errors are found in the first execution of ansible-lint, the content parser tool generates a list of files that contain the rule violations.
- If one or more `        syntax-check` errors are found in the first execution of ansible-lint, the content parser tool runs ansible-lint again but excludes the files with syntax-check errors. After the scan is completed, the content parser tool generates a list of files that contain rule violations. The list includes all files that caused syntax-check errors as well as other rule violations. The content parser tool excludes files with rule violations in all future scans, and the final training data set does not include data from the excluded files.



**Procedure**

Use one of the following methods to resolve ansible-lint rule violations:


- Run the content parser tool with the `    --no-exclude` option

If any rule violations, including syntax-check errors, are found, the execution is aborted with an error and no training data set is created.


- Limit the set of rules that ansible-lint uses to scan your data with the `    --profile` option

It is recommended that you fix the files with rule violations. However, if you do not want to modify the source files, you can limit the set of rules that ansible-lint uses to scan your data. To limit the set of rules that ansible-lint uses to scan your data, specify the `    --profile` option with a predefined profile (for example, `    min` , `    basic` , `    moderate` , `    safety` , `    shared` , or `    production` profiles) or by using ansible-lint configuration files. For more information, see the [Ansible Lint documentation](https://ansible.readthedocs.io/projects/lint/) .


- Run the content parser tool by skipping ansible-lint preprocessing

You can run the content parser without ansible-lint preprocessing. The content parser tool generates a training data set without scanning for ansible-lint rule violations.

To run the content parser tool without ansible-lint preprocessing, execute the following command:
`    $ ansible-content-parser<span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">source</span></em></span><span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">output</span></em></span><span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">-S</span></em></span>`

Where:


-  `        <span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">source</span></em></span>` : Specifies the source of the training data set.
-  `        <span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">output</span></em></span>` : Specifies the output of the training data set.
-  `        <span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">-S</span></em></span>` or `        <span class="emphasis"><em><span class="Role ARG Spec Role ARG Spec">--skip-ansible-lint</span></em></span>` : Specifies to skip ansible-lint preprocessing while generating the training data set.



#### 5.3.2.8. Merging multiple training data sets into a single file




For every execution, the content parser tool creates a training data set JSONL file named **ftdata.jsonl** that you upload to IBM watsonx Code Assistant for creating a custom model. If the content parser tool runs multiple times, multiple JSONL files are created. IBM watsonx Code Assistant supports a single JSONL file upload only; therefore, if you have multiple JSONL files, you must merge them into a single, concatenated file. You can also merge the multiple JSONL files that are generated in multiple subdirectories within a parent directory into a single file.

**Procedure**

1. Using the command prompt, go to the parent directory.
1. Run the following command to create a single, concatenated file:
`    find . -name ftdata.json | xargs cat &gt; concatenated.json`
1. Optional: Rename the concatenated file for easy identification.


You can now upload the merged JSONL file to IBM watsonx Code Assistant and create a custom model.

