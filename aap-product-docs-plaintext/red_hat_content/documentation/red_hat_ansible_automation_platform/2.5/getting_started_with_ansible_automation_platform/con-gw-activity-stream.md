# 1. Key functionality and concepts
## 1.1. Activity stream




The platform gateway includes an activity stream that captures changes to platform gateway resources, including the creation or modification of organizations, users, and service clusters, among others.

For each change, the activity stream records the timestamp, the user that initiated the change, the action performed, and the changes made to the object, when possible.

The information gathered varies depending on the type of change.

You can access the details captured by the activity stream from the API:

```
/api/gateway/v1/activitystream/
```

