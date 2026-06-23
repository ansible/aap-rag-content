# Configure a monthly usage report
## Fetch a monthly report on Red Hat Enterprise Linux

Use the following procedure to fetch a monthly report on Red Hat Enterprise Linux:

### Procedure

Run: `scp -r username@controller_host:$METRICS_UTILITY_SHIP_PATH/data/<YYYY>/<MM>/ /local/directory/`

### Results

The system saves the generated report as `CCSP-<YEAR>-<MONTH>.xlsx` in the ship path that you specified.

