# New features and enhancements
## Event sources transitioning from ansible.eda to community.eda

The following list of event sources is being removed from the certified ansible.eda collection, will not be supported by Red Hat engineering, but they will have community maintenance, and are available as part of the community.eda collection. If you are using any of these filters, make sure to update your ansible-rulebooks to use the community.eda namespace, and you will need a custom decision environment in order to keep running your rulebooks.

You can also keep your existing rulebooks with an older version of DE-supported or DE-minimal, while you update your rulebooks.

'ansible.eda.file to community.eda.file' 'ansible.eda.file_watch to community.eda.file_watch' 'ansible.eda.journald to community.eda.journald' 'ansible.eda.tick to use either eda.builtin.generic or eda.builtin.range' 'ansible.eda.url_check to community.eda.url_check'

