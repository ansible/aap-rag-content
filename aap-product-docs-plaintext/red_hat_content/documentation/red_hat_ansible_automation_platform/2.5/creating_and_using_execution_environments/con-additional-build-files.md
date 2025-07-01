# 3. Using Ansible Builder
## 3.8. Additional build files




You can add any external file to the build context directory by referring or copying them to the `additional_build_files` section of the definition file. The format is a list of dictionary values, each with a `src` and `dest` key and value.

Each list item must be a dictionary containing the following required keys:

Note
Absolute paths can not include a regular expression. If `src` is a directory, the entire contents of that directory are copied to `dest` .



