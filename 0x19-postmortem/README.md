# 0x19-postmortem: Logic API Infrastructure Outage Incident Report
Friday, Octuber 1, 2021

<p align="center">
  <img src="meme_keepcalm.png" />
</p>

## ISSUE SUMMARY

From 8:15 UTC to 09:50 UTC, requests to most of the Logic APIs resulted in 500 error response messages. Logic applications that rely on these APIs also returned errors or had reduced functionality. At its peak, the issue affected 100% of the traffic to this API infrastructure. The main cause of this outage was an invalid configuration change that exposed a bug in a widely used internal library.

## TIMELINE
- 8:05 UTC: Configuration push begins
- 8:15 UTC: Outage begins
- 8:15 UTC: Pagers alerted teams
- 8:48 UTC: Failed configuration change rollback
- 9:05 UTC: Successful configuration rollback
- 9:12 UTC: Server restarts begin
- 9:50 UTC: 100% of traffic back online

## ROOT CAUSE

At 8:05 UTC, a configuration change was inadvertently released to our production environment without first being released to the testing environment. The change specified an invalid address for the authentication servers in production. This exposed a bug in the authentication libraries which caused them to block permanently while attempting to resolve the invalid address to physical services. In addition, the internal monitoring systems permanently blocked on this call to the authentication library. The combination of the bug and configuration error quickly caused all of the serving threads to be consumed. Traffic was permanently queued waiting for a serving thread to become available. The servers began repeatedly hanging and restarting as they attempted to recover and at 8:15 UTC, the service outage began.

## RESOLUTION AND RECOVERY

At 8:15 UTC, the monitoring systems alerted our engineers who investigated and quickly escalated the issue. By 8:15 UTC, the incident response team identified that the monitoring system was exacerbating the problem caused by this bug.

At 8:48 UTC, we attempted to rollback the problematic configuration change. This rollback failed due to complexity in the configuration system which caused our security checks to reject the rollback. These problems were addressed and we successfully rolled back at 9:05 UTC.

Some jobs started to slowly recover, and we determined that the overall recovery would be faster by a restart of all of the API infrastructure servers globally. To help with the recovery, we turned off some of our monitoring systems which were triggering the bug. As a result, we decided to restart servers gradually (at 9:12 UTC), to avoid possible cascading failures from a wide scale restart. By 9:39 UTC, 25% of traffic was restored and 100% of traffic was routed to the API infrastructure at 09:50 UTC.

## CORRECTIVE AND PREVENTATIVE MEASURES

Following this incident, the team conducted an internal review and analysis of the outage. The following are actions that were taken to help prevent recurrence and improve response time:

- Disable the current configuration release mechanism until safer measures are implemented. (Completed).
- Change rollback process to be quicker and more robust.
- Fix the underlying authentication libraries and monitoring to correctly timeout/interrupt on errors.
- Programmatically enforce staged rollouts of all configuration changes.
- Improve process for auditing all high-risk configuration options.
- Add a faster rollback mechanism and improve the traffic ramp-up process, so any future problems of this type can be corrected quickly.
- Develop better mechanism for quickly delivering status notifications during incidents.

