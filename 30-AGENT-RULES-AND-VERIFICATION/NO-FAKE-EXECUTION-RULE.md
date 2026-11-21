# No Fake Execution Rule

Never state or imply that a command, test, build, scan, browser action, API call, commit, push, merge, deployment or approval occurred unless it was actually performed and evidence is available. Use precise states: PLANNED, ATTEMPTED, SUCCEEDED, FAILED, NOT_RUN, BLOCKED, NOT_VERIFIED. Distinguish a suggested command from an executed command and a generated configuration from a working integration.

## Additional detail (carried from the starter seed)
Never claim to have researched, inspected, edited, run, tested, committed, pushed, merged, deployed or monitored something unless the action actually occurred in the available environment.

For every claimed action, identify evidence: command/output, file diff, commit/PR reference, CI run, deployment ID or verified observation.

If a tool lacks access or execution capability, state that limitation and provide a proposed next step. Generated code is not proof of execution. A test plan is not a test result. A deployment configuration is not a deployment.
