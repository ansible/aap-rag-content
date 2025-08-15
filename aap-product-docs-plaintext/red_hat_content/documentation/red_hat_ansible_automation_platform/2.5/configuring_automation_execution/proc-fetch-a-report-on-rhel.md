# 12. Usage reporting with metrics-utility
## 12.2. Fetching a monthly report
### 12.2.1. Fetching a monthly report on Red Hat Enterprise Linux




Use the following procedure to fetch a monthly report on Red Hat Enterprise Linux:

**Procedure**

- Run: `    scp -r username@controller_host:$METRICS_UTILITY_SHIP_PATH/data/&lt;YYYY&gt;/&lt;MM&gt;/ /local/directory/`


The system saves the generated report as `CCSP-&lt;YEAR&gt;-&lt;MONTH&gt;.xlsx` in the ship path that you specified.

