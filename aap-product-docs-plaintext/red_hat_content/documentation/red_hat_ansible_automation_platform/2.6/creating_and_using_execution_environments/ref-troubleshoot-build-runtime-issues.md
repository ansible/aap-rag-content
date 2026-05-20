# 6. Create and integrate custom MCP Servers in execution environments
## 6.11. Troubleshoot build and runtime errors

Diagnose and resolve common issues encountered when building, configuring, and integrating custom or built-in Model Context Protocol (MCP) servers within your execution environments.

**Build failures**

Common causes of build failures include:

| <br>  Error | <br>  Reason |
| --- | --- |
| <br>  Unable to find collection artifact file | <br>  This error occurs when the collection tarball path in `requirements.yml` does not match the path inside the container. Ensure that: * The tarball is listed in `additional_build_files` with a dest value. * The source path in `requirements.yml` uses `/build/ configs/<filename>` (not the host filesystem path). |
| <br>  Package download fails during build | <br>  The execution environment build environment requires network access to download packages from PyPI, npm, or Git repositories. If building behind a proxy, configure proxy settings in your container build environment. If building in an air-gapped environment, you must pre-download packages and include them using `additional_build_files`. |
| <br>  Go build fails with "module not found" | <br>  For Go-based MCP servers, ensure the`build_repo` URL and `build_repo_branch` are correct and accessible. The framework clones the repository and runs go mod download before building. |

**Runtime failures**

If your MCP server builds successfully but encounters errors at runtime, consider the following troubleshooting steps:

| <br>  Error | <br>  Reason |
| --- | --- |
| <br>  mcp_manage : command not found | <br>  The mcp_manage script is installed at /opt/mcp/mcp_manage with a symlink at /usr/local/bin/mcp_manage. If it is missing, the common role’s generate_management task might have been skipped. <br>  Ensure your playbook includes `ansible.mcp_builder.common` with `public: true` as the first task. |
| <br>  MCP server fails with permission errors | <br>  The execution environment runs as user 1000 (non-root). Ensure your playbook includes the ownership fix task:        - name: Fix ownership of all MCP installations for runtime user       ansible.builtin.file:         path: "{{ common_mcp_base_path }}"         state: directory         recurse: true         owner: "{{ common_runtime_user }}"         group: "{{ common_runtime_user }}" |
| <br>  Server listed but not executing | <br>  If mcp_manage list shows your server but mcp_manage run fails, check:    <br>  The binary exists at the path shown in the manifest.   Required runtime dependencies are present (for example, Node.js for npm-based servers).   Environment variables required by the server are passed at container runtime. |

**Variable validation errors**

If your server fails due to missing or invalid variables, check the following:

| <br>  Error | <br>  Reason |
| --- | --- |
| <br>  Missing registry variables | <br>  The common role expects a registry variable named `<role_name>_registry`. Ensure your `defaults/main.yml` follows the naming convention. For a role named `cfn_mcp`, the variable in `defaults/main.yml` must be `cfn_mcp_registry`. |
| <br>  Invalid language type | <br>  The lang field in the registry must be one of: pypi, npm, or go. Any other value causes the install manager to skip installation. |

**Understanding support boundaries**

The MCP Builder framework provides the tools and structure to build and integrate MCP servers, but you are responsible for ensuring the correctness of your server’s code, its dependencies, and its configuration.

Red Hat provides and supports the following components:

- The `ansible.mcp_builder` collection, including the common role and its installation framework.
- The ansible-builder tool for creating execution environments.
- The execution environment runtime within Ansible Automation Platform.

The following are the customer’s responsibility:

- Individual MCP server implementations. Red Hat does not support any specific MCP server, including the reference examples (AWS, Azure, GitHub) provided in the `ansible.mcp_builder` collection. These examples are Dev Preview.
- Custom MCP roles and collections. Your organization owns the creation, testing, and maintenance of custom roles.
- MCP server security. Your organization is responsible for evaluating, auditing, and securing the MCP servers you deploy.
- MCP server credentials and access controls. Configuring and securing access to external services is your responsibility.

If you encounter issues:

- For problems with ansible-builder, the common role, or the execution environment build process, contact Red Hat support.
- For problems with a specific MCP server, contact the MCP server vendor or community.

# Appendix A. Automation execution environments precedence

Identify and control the exact automation execution environment applied to your jobs by tracing the precedence hierarchy, ensuring you can troubleshoot environment mismatches or configure accurate defaults across your templates, projects, and organizations.

Project updates always use the control plane automation execution environments by default.

However, jobs use the first available automation execution environments as follows:

1. The `execution_environment` defined on the template (job template or inventory source) that created the job.
2. The `default_environment` defined on the project that the job uses.
3. The `default_environment` defined on the organization of the job.
4. The `default_environment` defined on the organization of the inventory the job uses.
5. The current `DEFAULT_EXECUTION_ENVIRONMENT` setting (configurable at `api/v2/settings/system/`)
6. Any image from the `GLOBAL_JOB_EXECUTION_ENVIRONMENTS` setting.
7. Any other global execution environment.

Note

- Where an execution environment is not available, the Default execution environment can be used. However, you must select this, as the system does not automatically provide a default environment.
- If more than one execution environment fits a criteria (applies for 6 and 7), the most recently created one is used.

## A.1. If no default execution environment is provided

Troubleshoot why a job bypasses the Default Execution Environment by verifying overrides in template, project, organization, or global settings, and checking environment array orders in configuration files and the database.

When the "Default Execution Environment" is not used for a job, double-check the following:

**Procedure**

1. Check if a different execution environment EE has been defined for the template, project, or organization of the job.

2. Check if the `GLOBAL_JOB_EXECUTION_ENVIRONMENTS` setting is configured with any execution environments, as these take precedence over the Default execution environment.


Note
This setting is not configured by default.

3. Check the order of the GLOBAL_JOB_EXECUTION_ENVIRONMENTS in `/etc/tower/conf.d/execution_environments.py`. "Default Execution Environment" should be the first item in the array.

4. Check the order of the execution environment defined in the database.

5. Run the following command as root on the controller node to output the `main_executionenvironment` table:

`# echo "select id, name, created from main_executionenvironment where organization_id is null and managed = False order by created desc;" | awx-manage dbshell`

To ensure that the "Default Execution Environment" is used regardless of the `GLOBAL_JOB_EXECUTION_ENVIRONMENTS`mm setting and database order, set the "Global default execution environment" in Settings → Automation Execution → System to "Default Execution Environment".

# Chapter 7. Open Source license

**Apache license**

Version 2.0, January 2004

<http://www.apache.org/licenses/>

TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

**1. Definitions.**

**"License"** shall mean the terms and conditions for use, reproduction, and distribution as defined by Sections 1 through 9 of this document.

**"Licensor"** shall mean the copyright owner or entity authorized by the copyright owner that is granting the License.

**"Legal Entity"** shall mean the union of the acting entity and all other entities that control, are controlled by, or are under common control with that entity. For the purposes of this definition, **"control"** means (i) the power, direct or indirect, to cause the direction or management of such entity, whether by contract or otherwise, or (ii) ownership of fifty percent (50%) or more of the outstanding shares, or (iii) beneficial ownership of such entity.

**"You"** (or **"Your"**) shall mean an individual or Legal Entity exercising permissions granted by this License.

**"Source"** form shall mean the preferred form for making modifications, including but not limited to software source code, documentation source, and configuration files.

**"Object"** form shall mean any form resulting from mechanical transformation or translation of a Source form, including but not limited to compiled object code, generated documentation, and conversions to other media types.

**"Work"** shall mean the work of authorship, whether in Source or Object form, made available under the License, as indicated by a copyright notice that is included in or attached to the work (an example is provided in the Appendix below).

**"Derivative Works"** shall mean any work, whether in Source or Object form, that is based on (or derived from) the Work and for which the editorial revisions, annotations, elaborations, or other modifications represent, as a whole, an original work of authorship. For the purposes of this License, Derivative Works shall not include works that remain separable from, or merely link (or bind by name) to the interfaces of, the Work and Derivative Works thereof.

**"Contribution"** shall mean any work of authorship, including the original version of the Work and any modifications or additions to that Work or Derivative Works thereof, that is intentionally submitted to Licensor for inclusion in the Work by the copyright owner or by an individual or Legal Entity authorized to submit on behalf of the copyright owner. For the purposes of this definition, **"submitted"** means any form of electronic, verbal, or written communication sent to the Licensor or its representatives, including but not limited to communication on electronic mailing lists, source code control systems, and issue tracking systems that are managed by, or on behalf of, the Licensor for the purpose of discussing and improving the Work, but excluding communication that is conspicuously marked or otherwise designated in writing by the copyright owner as **"Not a Contribution."**

**"Contributor"** shall mean Licensor and any individual or Legal Entity on behalf of whom a Contribution has been received by Licensor and subsequently incorporated within the Work.

**2. Grant of Copyright License.** Subject to the terms and conditions of this License, each Contributor hereby grants to You a perpetual, worldwide, non-exclusive, no-charge, royalty-free, irrevocable copyright license to reproduce, prepare Derivative Works of, publicly display, publicly perform, sublicense, and distribute the Work and such Derivative Works in Source or Object form.

**3. Grant of Patent License.** Subject to the terms and conditions of this License, each Contributor hereby grants to You a perpetual, worldwide, non-exclusive, no-charge, royalty-free, irrevocable (except as stated in this section) patent license to make, have made, use, offer to sell, sell, import, and otherwise transfer the Work, where such license applies only to those patent claims licensable by such Contributor that are necessarily infringed by their Contribution(s) alone or by combination of their Contribution(s) with the Work to which such Contribution(s) was submitted. If You institute patent litigation against any entity (including a cross-claim or counterclaim in a lawsuit) alleging that the Work or a Contribution incorporated within the Work constitutes direct or contributory patent infringement, then any patent licenses granted to You under this License for that Work shall terminate as of the date such litigation is filed.

**4. Redistribution.** You may reproduce and distribute copies of the Work or Derivative Works thereof in any medium, with or without modifications, and in Source or Object form, provided that You meet the following conditions:

1. You must give any other recipients of the Work or Derivative Works a copy of this License; and
2. You must cause any modified files to carry prominent notices stating that You changed the files; and
3. You must retain, in the Source form of any Derivative Works that You distribute, all copyright, patent, trademark, and attribution notices from the Source form of the Work, excluding those notices that do not pertain to any part of the Derivative Works; and
4. If the Work includes a **"NOTICE"** text file as part of its distribution, then any Derivative Works that You distribute must include a readable copy of the attribution notices contained within such NOTICE file, excluding those notices that do not pertain to any part of the Derivative Works, in at least one of the following places: within a NOTICE text file distributed as part of the Derivative Works; within the Source form or documentation, if provided along with the Derivative Works; or, within a display generated by the Derivative Works, if and wherever such third-party notices normally appear. The contents of the NOTICE file are for informational purposes only and do not modify the License. You may add Your own attribution notices within Derivative Works that You distribute, alongside or as an addendum to the NOTICE text from the Work, provided that such additional attribution notices cannot be construed as modifying the License.

You may add Your own copyright statement to Your modifications and may provide additional or different license terms and conditions for use, reproduction, or distribution of Your modifications, or for any such Derivative Works as a whole, provided Your use, reproduction, and distribution of the Work otherwise complies with the conditions stated in this License.

**5. Submission of Contributions.** Unless You explicitly state otherwise, any Contribution intentionally submitted for inclusion in the Work by You to the Licensor shall be under the terms and conditions of this License, without any additional terms or conditions. Notwithstanding the above, nothing herein shall supersede or modify the terms of any separate license agreement you may have executed with Licensor regarding such Contributions.

**6. Trademarks.** This License does not grant permission to use the trade names, trademarks, service marks, or product names of the Licensor, except as required for reasonable and customary use in describing the origin of the Work and reproducing the content of the NOTICE file.

**7. Disclaimer of Warranty.** Unless required by applicable law or agreed to in writing, Licensor provides the Work (and each Contributor provides its Contributions) on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied, including, without limitation, any warranties or conditions of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A PARTICULAR PURPOSE. You are solely responsible for determining the appropriateness of using or redistributing the Work and assume any risks associated with Your exercise of permissions under this License.

**8. Limitation of Liability.** In no event and under no legal theory, whether in tort (including negligence), contract, or otherwise, unless required by applicable law (such as deliberate and grossly negligent acts) or agreed to in writing, shall any Contributor be liable to You for damages, including any direct, indirect, special, incidental, or consequential damages of any character arising as a result of this License or out of the use or inability to use the Work (including but not limited to damages for loss of goodwill, work stoppage, computer failure or malfunction, or any and all other commercial damages or losses), even if such Contributor has been advised of the possibility of such damages.

**9. Accepting Warranty or Additional Liability.** While redistributing the Work or Derivative Works thereof, You may choose to offer, and charge a fee for, acceptance of support, warranty, indemnity, or other liability obligations and/or rights consistent with this License. However, in accepting such obligations, You may act only on Your own behalf and on Your sole responsibility, not on behalf of any other Contributor, and only if You agree to indemnify, defend, and hold each Contributor harmless for any liability incurred by, or claims asserted against, such Contributor by reason of your accepting any such warranty or additional liability.

END OF TERMS AND CONDITIONS

# Legal Notice

Copyright © Red Hat.

Except as otherwise noted below, the text of and illustrations in this documentation are licensed by Red Hat under the Creative Commons Attribution–Share Alike 3.0 Unported license . If you distribute this document or an adaptation of it, you must provide the URL for the original version.

Red Hat, as the licensor of this document, waives the right to enforce, and agrees not to assert, Section 4d of CC-BY-SA to the fullest extent permitted by applicable law.

Red Hat, the Red Hat logo, JBoss, Hibernate, and RHCE are trademarks or registered trademarks of Red Hat, LLC. or its subsidiaries in the United States and other countries.

Linux® is the registered trademark of Linus Torvalds in the United States and other countries.

XFS is a trademark or registered trademark of Hewlett Packard Enterprise Development LP or its subsidiaries in the United States and other countries.

The OpenStack® Word Mark and OpenStack logo are trademarks or registered trademarks of the Linux Foundation, used under license.

All other trademarks are the property of their respective owners.
