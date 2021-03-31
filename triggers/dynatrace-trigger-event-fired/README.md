# dynatrace-trigger-event-fired

This [Dynatrace](https://www.dynatrace.com/) trigger fires when a Dynatrace Problem notification webhook is sent to relay.
For more information check out the [Dynatrace Problem Notifications webhook documentation](https://www.dynatrace.com/support/help/setup-and-configuration/integrations/third-party-integrations/problem-notification-systems/webhook-integration/)

## Data Emitted 

Dynatrace gives you the flexiblity to define which problem details you want to pass to Relay. See an example below. The most common data points are listed here

| Name | Data type | Description | 
|------|-----------|-------------|
| State | string | Problem state. Possible values are OPEN or RESOLVED or in some cases MERGED when the problem has been merged into another problem | 
| ProblemID | string | Display number of the reported problem | 
| PID | string | Unique system identifier of the reported problem | 
| ProblemTitle | string | Short description of the problem | 
| ProblemURL | string | URL of the problem within Dynatrace | 
| ProblemSeverity | string | Severity level of the problem. Possible values are AVAILABILITY, ERROR, PERFORMANCE, RESOURCE_CONTENTION, or CUSTOM_ALERT |  
| ProblemImpact | string |  Impact level of the problem. Possible values are APPLICATION, SERVICE, or INFRASTRUCTURE |  
| Tags | string | Comma separated list of tags that are defined for all impacted entities.  |  
| ProblemDetailsText | string | All problem event details including root cause as a text-formatted string |
| ProblemDetailsJSON | string | All problem event details including root cause in form of a json object |  

## Example Trigger

To use this in your workflow, add a `triggers` section as below. For a complete example, see the [../../workflows/dynatrace-respond-to-problem/README.md](dynatrace-respond-to-problem) workflow.

```yaml
triggers:
- name: dynatrace-problem-event
  source:
    type: webhook
    image: relaysh/dynatrace-trigger-event-fired:latest
  binding:
    parameters:
      state: !Data State
      problemid: !Data ProblemId
      pid: !Data PID
      problemtitle: !Data ProblemTitle
      problemurl: !Data ProblemUrl 
      problemseverity: !Data ProblemSeverity
      problemimpact: !Data ProblemImpact
      problemdetailstext: !Data ProblemDetailsText
      tags: !Data Tags
```
