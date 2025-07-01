# 12. Usage reporting with metrics-utility
## 12.1. Configuring metrics-utility
### 12.1.2. Configuring metrics-utility on OpenShift Container Platform from the Ansible Automation Platform operator




`metrics-utility` is included in the OpenShift Container Platform image beginning with version 4.12, 4.512, and 4.6. If your system does not have `metrics-utility` installed, update your OpenShift image to the latest version.

Complete the following steps to configure the run schedule for `metrics-utility` on OpenShift Container Platform using the Ansible Automation Platform operator:

#### 12.1.2.1. Create a ConfigMap in the OpenShift UI YAML view




To inject the `metrics-utility` cronjobs with configuration data, use the following procedure to create a ConfigMap in the OpenShift UI YAML view:

**Prerequisites:**

- A running OpenShift cluster
- An operator-based installation of Ansible Automation Platform on OpenShift Container Platform.


Note
Metrics-utility runs as indicated by the parameters you set in the configuration file. You cannot run the utility cannot manually on OpenShift Container Platform.



**Procedure**

1. From the navigation panel, selectConfigMaps.
1. ClickCreate ConfigMap.
1. On the next screen, select the YAML view tab.
1. In the YAML field, enter the following parameters with the appropriate variables set:


```
apiVersion: v1    kind: ConfigMap    metadata:      name: automationcontroller-metrics-utility-configmap    data:      METRICS_UTILITY_SHIP_TARGET: directory      METRICS_UTILITY_SHIP_PATH: /metrics-utility      METRICS_UTILITY_REPORT_TYPE: CCSP      METRICS_UTILITY_PRICE_PER_NODE: '11' # in USD      METRICS_UTILITY_REPORT_SKU: MCT3752MO      METRICS_UTILITY_REPORT_SKU_DESCRIPTION: "EX: Red Hat Ansible Automation Platform, Full Support (1 Managed Node, Dedicated, Monthly)"      METRICS_UTILITY_REPORT_H1_HEADING: "CCSP Reporting &lt;Company&gt;: ANSIBLE Consumption"      METRICS_UTILITY_REPORT_COMPANY_NAME: "Company Name"      METRICS_UTILITY_REPORT_EMAIL: "email@email.com"      METRICS_UTILITY_REPORT_RHN_LOGIN: "test_login"      METRICS_UTILITY_REPORT_COMPANY_BUSINESS_LEADER: "BUSINESS LEADER"      METRICS_UTILITY_REPORT_COMPANY_PROCUREMENT_LEADER: "PROCUREMENT LEADER"
```


1. ClickCreate.


**Verification**

- To verify that you created the ConfigMap and the metric utility is installed, select **ConfigMap** from the navigation panel and look for your ConfigMap in the list.


#### 12.1.2.2. Deploy automation controller




To deploy automation controller and specify variables for how often metrics-utility gathers usage information and generates a report, use the following procedure:

**Procedure**

1. From the navigation panel, select **Installed Operators** .
1. Select **Ansible Automation Platform** .
1. In the Operator details, select the automation controller tab.
1. ClickCreate automation controller.
1. Select the YAML view option. The YAML now shows the default parameters for automation controller. The relevant parameters for `    metrics-utility` are the following:

|  **Parameter** |  **Variable** |
| --- | --- |
|  ** `metrics_utility_enabled` ** | True. |
|  ** `metrics_utility_cronjob_gather_schedule` ** |  `@hourly` or `@daily` . |
|  ** `metrics_utility_cronjob_report_schedule` ** |  `@daily` or `@monthly` . |



1. Find the `    metrics_utility_enabled` parameter and change the variable to true.
1. Find the `    metrics_utility_cronjob_gather_schedule` parameter and enter a variable for how often the utility should gather usage information (for example, `    @hourly` or `    @daily` ).
1. Find the `    metrics_utility_cronjob_report_schedule` parameter and enter a variable for how often the utility generates a report (for example, `    @daily` or `    @monthly` ).
1. ClickCreate.


