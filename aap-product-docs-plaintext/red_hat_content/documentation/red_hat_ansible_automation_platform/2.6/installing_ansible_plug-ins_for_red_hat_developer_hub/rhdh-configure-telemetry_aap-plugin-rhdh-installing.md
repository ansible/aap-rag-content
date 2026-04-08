# Chapter 8. Red Hat Developer Hub data telemetry capturing




Red Hat Developer Hub (RHDH) sends telemetry data to Red Hat using the `backstage-plugin-analytics-provider-segment` plug-in, which is enabled by default. This includes telemetry data from the Ansible plug-ins.

Red Hat collects and analyzes the following data to improve your experience with Red Hat Developer Hub:

- Events of page visits and clicks on links or buttons.
- System-related information, for example, locale, timezone, user agent including browser and OS details.
- Page-related information, for example, title, category, extension name, URL, path, referrer, and search parameters.
- Anonymized IP addresses, recorded as 0.0.0.0.
- Anonymized username hashes, which are unique identifiers used solely to identify the number of unique users of the RHDH application.
- Feedback and sentiment submitted through the Ansible plug-ins feedback form, including a 1-5 star rating and feedback text. Users must acknowledge that they share the feedback with Red Hat before submitting. The feedback form is disabled by default.


With Red Hat Developer Hub, you can disable or customize the telemetry data collection feature. For more information, refer to the [Telemetry data collection and analysis](https://docs.redhat.com/en/documentation/red_hat_developer_hub/1.6/html/telemetry_data_collection_and_analysis/index) guide in the Red Hat Developer Hub documentation.

