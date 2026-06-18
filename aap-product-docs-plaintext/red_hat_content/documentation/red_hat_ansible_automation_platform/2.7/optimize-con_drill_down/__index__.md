# Change your Automation Analytics settings

You can drill down into cluster data to review more detailed information about successful or failed jobs.

The detailed view, presented on the **Job Explorer** page, provides information on the cluster, organization, template, and job type. Filters you select on the **Clusters** view carry over to the **Job Explorer** page.

Details on those job templates will appear in the **Job Explorer** view, modified by any filters you select in the **Clusters** view.

For example, you can drill down to review details for failed jobs in a cluster.

## Example: Review failed jobs

You can view detailed information about failed jobs across your organization by drilling down on a graph in the **Clusters** view and using the **Job Explorer** to refine results. Clicking a segment on the graph opens that information in the **Job Explorer**, preserving filters applied in the **Clusters** view.

### Procedure

1.  From the navigation panel, select Automation Analytics> (and then)Clusters.
2.  Use the filter lists in the toolbar to apply filters for clusters and time range of your choosing.
3.  Click a segment on the graph. You are redirected to the **Job Explorer** view, which displays a list of jobs corresponding to that day on the graph.

4.  To refine the list to show only failed jobs:
1.  Select **Status** from the **Filter by** list.
2.  Select the **Failed** filter. The **Job Explorer** view updates to show only failed jobs run within the selected time range.

### What to do next

- Add additional context to the view by applying more filters and selecting attributes to sort results.
- Review more information for failed jobs on the automation controller job details page.

## View top templates job details for a specific cluster

You can view job instances for top templates in a cluster to learn more about individual job runs associated with that template or to apply filters to further drill down into the data.

### Procedure

1.  From the navigation panel, select Automation Analytics> (and then)Clusters.
2.  Click a template name in **Top Templates**.
3.  Click View all jobs in the modal that is displayed. The **Job Explorer** page displays all jobs on the chosen cluster associated with that template.

The view presented will preserve the contextual information of the template based on the parameters selected in the **Clusters** view.

## Ignore nested workflows and jobs

Ignoring nested workflows and jobs filters out duplicate workflow and job template entries and excludes those items from overall totals.

### Procedure

1.  Select the settings icon on the **Job Explorer** view.
2.  Use the toggle switch to **Ignore nested workflows and jobs**. Note:
**About nested workflows** Nested workflows enable you to create workflow job templates that call other workflow job templates. Nested workflows promotes reuse, as modular components, of workflows that include existing business logic and organizational requirements in automating complex processes and operations. To learn more about nested workflows, see Workflows in automation controller in the [Using automation execution](/documentation/en-us/red_hat_ansible_automation_platform/2.7/develop-assembly_ug_controller_workflows#controller-workflows "Workflows enable you to configure a sequence of disparate job templates (or workflow templates) that might or might not share inventory, playbooks, or permissions.").
