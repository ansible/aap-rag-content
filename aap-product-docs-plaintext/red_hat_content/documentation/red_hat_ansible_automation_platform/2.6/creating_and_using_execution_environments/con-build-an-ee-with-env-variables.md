# 2. Using Ansible Builder
## 2.9. Additional custom build steps
### 2.9.1. Build execution environments with environment variables




The following example file specifies environment variables that might be required for the build process.

To achieve this functionality it uses the `ENV` variable definition in the `prepend_base` step of the additional_build_steps section.

```
-
additional_build_steps:
prepend_base:
- ENV FOO=bar
- RUN echo $FOO &gt; /tmp/file1.txt
```


The same environment variables can be used in the later stage of the build process.

