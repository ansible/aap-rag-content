# 12. Usage reporting with metrics-utility
## 12.4. Supported storage
### 12.4.1. Local disk




For an installation of Ansible Automation Platform on Red Hat Enterprise Linux, the default storage option is a local disk. Using an OpenShift deployment of OpenShift Container Platform, default storage is a path inside the attached Persistent Volume Claim.

```
# Set needed ENV VARs for gathering data and generating reports
export METRICS_UTILITY_SHIP_TARGET=directory
# Your path on the local disk
export METRICS_UTILITY_SHIP_PATH=/path_to_data_and_reports/...
```

