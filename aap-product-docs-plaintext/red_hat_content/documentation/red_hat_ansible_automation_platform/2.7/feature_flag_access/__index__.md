# Feature flag access

Access to the feature flags page is role-based; in other words, access depends on the level of access a user has.

When feature flags are enabled, the following access rules apply.

Superusers (administrators):

- Can view the feature flags section.
- Can toggle runtime feature flags on and off.
- Can access all editable feature flags.

Auditors:

- Can view the feature flags section.
- Can view all flag metadata and current states.
- **Cannot** toggle runtime feature flags, as they have read-only access

Normal users:

- Cannot view the feature flags section.
- Do not see the feature flags menu item in their UI navigation panel.
- Are blocked from direct URL access to the feature flags section.
