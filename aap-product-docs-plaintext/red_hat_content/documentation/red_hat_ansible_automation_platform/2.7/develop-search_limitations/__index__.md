# Search limitations

The search function has the following limitations that affect how queries are processed and combined.

- `OR` queries are not supported. All search terms are combined with `AND` logic.
- Wrap the field name in quotes to search for field names that contain spaces.
- All field searches use `__icontains` matching. For example, `name:localhost` sends `?name__icontains=localhost` to the API.
