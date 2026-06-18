# Known issues

The following release notes detail the known issues for the Ansible Automation Platform general availability released on June 3, 2026

## Execution environment builder

- Git-backed auto-discovery of EE definitions is not implemented; definitions created in EE builder still register in the catalog. Planned for a future release.
- Automated image builds run on GitHub only; GitLab CI/CD builds are planned for a future release.


- Referenced documents are not sorted by relevance when BYOK is enabled. When you use BYOK with the intelligent assistant, document link ordering in the referenced documents list may not reflect query relevance.(AAP-72138)
- Internal file IDs visible in the intelligent assistant's responses. Depending on the LLM you have integrated, the intelligent assistant's responses may expose internal file IDs (identified by a file- prefix).(AAP-72989)
