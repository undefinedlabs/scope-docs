---
id: release-notes
title: Scope release notes
sidebar_label: Release notes
---


## Scope v1.6.5

*February 15, 2020*

#### Added
- **New: macOS and tvOS support**. We have renamed the Scope iOS Agent into Scope Swift Agent, and added support for both macOS and tvOS.
- Added support for Buildkite.
- The setup wizard step for creating the GitHub App now links to a prepopulated "create new GitHub App" form (Scope Enterprise only).
- Added ability to configure SSL certificates to authenticate with an SMTP server for notifications (Scope Enterprise only).

#### Changed
- Removed summary section from notification emails.
- Redesigned aggregated tests status chart in Explore sidebar.
- GraphQL API now returns "Forbidden" when the user is authenticated but has no access to the requested resource.
- The agent ingest API will now reject test results that could not be tied to a repository and commit on Scope, helping with troubleshooting agent configuration problems.
- Emails are now sent individually to each user instead of using "blind carbon copy".
- The first untested commits for each branch are now auto expanded on the service explore view.
- Added dedicated worker queue for test results processing for improved responsiveness and robustness (Scope Enterprise only).

#### Fixed
- Improved performance of queries involving commit status calculations.
- Custom database icons now show up in the Test Report Trace view.
- Source tab for logs does not show up anymore if source is not available.
- Hover tooltips are displayed in the right position without flickering in Test Report Performance view.
- Test runs are correctly loaded again in Test Report History tab.
- CORS has been deactivated in the agent ingest API to allow collecting tracing information from browser-based agents.
- Email notifications now parse markdown format in commit messages and respect new lines.
- If a commit fails and passes when the build is retried, a "fixed" notification will be sent now.
- Fixed the "Add new repo" link for non-owners of the organization on GitHub.
- Revoke user access tokens when `github_app_authorization` webhooks are received.
- Improved the reliability of the GitHub checks.
- Tasks are now retried if GitHub API fails with a "rate limit exceeded" message.
- Fix external redirection to test reports with names that include the `/` character.
- All GitHub API calls now use the `Authorization` header when using user tokens instead of the deprecated URL parameter (Scope Enterprise only).


## Scope v1.6.4

*February 13, 2020*

#### Added
- **New: macOS and tvOS support**. We have renamed the Scope iOS Agent into Scope Swift Agent, and added support for both macOS and tvOS.
- Added support for Buildkite.
- The setup wizard step for creating the GitHub App now links to a prepopulated "create new GitHub App" form (Scope Enterprise only).
- Added ability to configure SSL certificates to authenticate with an SMTP server for notifications (Scope Enterprise only).

#### Changed
- Removed summary section from notification emails.
- Redesigned aggregated tests status chart in Explore sidebar.
- GraphQL API now returns "Forbidden" when the user is authenticated but has no access to the requested resource.
- The agent ingest API will now reject test results that could not be tied to a repository and commit on Scope, helping with troubleshooting agent configuration problems.
- Emails are now sent individually to each user instead of using "blind carbon copy".
- The first untested commits for each branch are now auto expanded on the service explore view.

#### Fixed
- Improved performance of queries involving commit status calculations.
- Custom database icons now show up in the Test Report Trace view.
- Source tab for logs does not show up anymore if source is not available.
- Hover tooltips are displayed in the right position without flickering in Test Report Performance view.
- Test runs are correctly loaded again in Test Report History tab.
- CORS has been deactivated in the agent ingest API to allow collecting tracing information from browser-based agents.
- Email notifications now parse markdown format in commit messages and respect new lines.
- If a commit fails and passes when the build is retried, a "fixed" notification will be sent now.
- Fixed the "Add new repo" link for non-owners of the organization on GitHub.
- Revoke user access tokens when `github_app_authorization` webhooks are received.
- Improved the reliability of the GitHub checks.
- Tasks are now retried if GitHub API fails with a "rate limit exceeded" message.
- Fix external redirection to test reports with names that include the `/` character.
- All GitHub API calls now use the `Authorization` header when using user tokens instead of the deprecated URL parameter (Scope Enterprise only).


## Scope v1.6.3

*February 11, 2020*

#### Added
- **New: macOS and tvOS support**. We have renamed the Scope iOS Agent into Scope Swift Agent, and added support for both macOS and tvOS.
- Added support for Buildkite.
- The setup wizard step for creating the GitHub App now links to a prepopulated "create new GitHub App" form (Scope Enterprise only).
- Added ability to configure SSL certificates to authenticate with an SMTP server for notifications (Scope Enterprise only).

#### Changed
- Removed summary section from notification emails.
- Redesigned aggregated tests status chart in Explore sidebar.
- GraphQL API now returns "Forbidden" when the user is authenticated but has no access to the requested resource.
- The agent ingest API will now reject test results that could not be tied to a repository and commit on Scope, helping with troubleshooting agent configuration problems.
- Emails are now sent individually to each user instead of using "blind carbon copy".
- The first untested commits for each branch are now auto expanded on the service explore view.

#### Fixed
- Improved performance of queries involving commit status calculations.
- Custom database icons now show up in the Test Report Trace view.
- Source tab for logs does not show up anymore if source is not available.
- Hover tooltips are displayed in the right position without flickering in Test Report Performance view.
- Test runs are correctly loaded again in Test Report History tab.
- CORS has been deactivated in the agent ingest API to allow collecting tracing information from browser-based agents.
- Email notifications now parse markdown format in commit messages and respect new lines.
- If a commit fails and passes when the build is retried, a "fixed" notification will be sent now.
- Fixed the "Add new repo" link for non-owners of the organization on GitHub.
- Revoke user access tokens when `github_app_authorization` webhooks are received.
- Improved the reliability of the GitHub checks.
- Tasks are now retried if GitHub API fails with a "rate limit exceeded" message.
- Fix external redirection to test reports with names that include the `/` character.
- All GitHub API calls now use the `Authorization` header when using user tokens instead of the deprecated URL parameter (Scope Enterprise only).


## Scope v1.6.2

*February 10, 2020*

#### Added
- **New: macOS and tvOS support**. We have renamed the Scope iOS Agent into Scope Swift Agent, and added support for both macOS and tvOS.
- Added support for Buildkite.
- The setup wizard step for creating the GitHub App now links to a prepopulated "create new GitHub App" form (Scope Enterprise only).
- Added ability to configure SSL certificates to authenticate with an SMTP server for notifications (Scope Enterprise only).

#### Changed
- Removed summary section from notification emails.
- Redesigned aggregated tests status chart in Explore sidebar.
- GraphQL API now returns "Forbidden" when the user is authenticated but has no access to the requested resource.
- The agent ingest API will now reject test results that could not be tied to a repository and commit on Scope, helping with troubleshooting agent configuration problems.
- Emails are now sent individually to each user instead of using "blind carbon copy".
- The first untested commits for each branch are now auto expanded on the service explore view.

#### Fixed
- Improved performance of queries involving commit status calculations.
- Custom database icons now show up in the Test Report Trace view.
- Source tab for logs does not show up anymore if source is not available.
- Hover tooltips are displayed in the right position without flickering in Test Report Performance view.
- Test runs are correctly loaded again in Test Report History tab.
- CORS has been deactivated in the agent ingest API to allow collecting tracing information from browser-based agents.
- Email notifications now parse markdown format in commit messages and respect new lines.
- If a commit fails and passes when the build is retried, a "fixed" notification will be sent now.
- Fixed the "Add new repo" link for non-owners of the organization on GitHub.
- Revoke user access tokens when `github_app_authorization` webhooks are received.
- Improved the reliability of the GitHub checks.
- Tasks are now retried if GitHub API fails with a "rate limit exceeded" message.
- Fix external redirection to test reports with names that include the `/` character.
- All GitHub API calls now use the `Authorization` header when using user tokens instead of the deprecated URL parameter (Scope Enterprise only).


## Scope v1.6.1

*February 08, 2020*

#### Added
- **New: macOS and tvOS support**. We have renamed the Scope iOS Agent into Scope Swift Agent, and added support for both macOS and tvOS.
- Added support for Buildkite.
- The setup wizard step for creating the GitHub App now links to a prepopulated "create new GitHub App" form (Scope Enterprise only).
- Added ability to configure SSL certificates to authenticate with an SMTP server for notifications (Scope Enterprise only).

#### Changed
- Removed summary section from notification emails.
- Redesigned aggregated tests status chart in Explore sidebar.
- GraphQL API now returns "Forbidden" when the user is authenticated but has no access to the requested resource.
- The agent ingest API will now reject test results that could not be tied to a repository and commit on Scope, helping with troubleshooting agent configuration problems.
- Emails are now sent individually to each user instead of using "blind carbon copy".
- The first untested commits for each branch are now auto expanded on the service explore view.

#### Fixed
- Improved performance of queries involving commit status calculations.
- Custom database icons now show up in the Test Report Trace view.
- Source tab for logs does not show up anymore if source is not available.
- Hover tooltips are displayed in the right position without flickering in Test Report Performance view.
- Test runs are correctly loaded again in Test Report History tab.
- CORS has been deactivated in the agent ingest API to allow collecting tracing information from browser-based agents.
- Email notifications now parse markdown format in commit messages and respect new lines.
- If a commit fails and passes when the build is retried, a "fixed" notification will be sent now.
- Fixed the "Add new repo" link for non-owners of the organization on GitHub.
- Revoke user access tokens when `github_app_authorization` webhooks are received.
- Improved the reliability of the GitHub checks.
- Tasks are now retried if GitHub API fails with a "rate limit exceeded" message.
- Fix external redirection to test reports with names that include the `/` character.
- All GitHub API calls now use the `Authorization` header when using user tokens instead of the deprecated URL parameter (Scope Enterprise only).


## Scope v1.6.0

*February 08, 2020*

#### Added
- **New: macOS and tvOS support**. We have renamed the Scope iOS Agent into Scope Swift Agent, and added support for both macOS and tvOS.
- Added support for Buildkite.
- The setup wizard step for creating the GitHub App now links to a prepopulated "create new GitHub App" form (Scope Enterprise only).
- Added ability to configure SSL certificates to authenticate with an SMTP server for notifications (Scope Enterprise only).

#### Changed
- Removed summary section from notification emails.
- Redesigned aggregated tests status chart in Explore sidebar.
- GraphQL API now returns "Forbidden" when the user is authenticated but has no access to the requested resource.
- The agent ingest API will now reject test results that could not be tied to a repository and commit on Scope, helping with troubleshooting agent configuration problems.
- Emails are now sent individually to each user instead of using "blind carbon copy".
- The first untested commits for each branch are now auto expanded on the service explore view.

#### Fixed
- Improved performance of queries involving commit status calculations.
- Custom database icons now show up in the Test Report Trace view.
- Source tab for logs does not show up anymore if source is not available.
- Hover tooltips are displayed in the right position without flickering in Test Report Performance view.
- Test runs are correctly loaded again in Test Report History tab.
- CORS has been deactivated in the agent ingest API to allow collecting tracing information from browser-based agents.
- Email notifications now parse markdown format in commit messages and respect new lines.
- If a commit fails and passes when the build is retried, a "fixed" notification will be sent now.
- Fixed the "Add new repo" link for non-owners of the organization on GitHub.
- Revoke user access tokens when `github_app_authorization` webhooks are received.
- Improved the reliability of the GitHub checks.
- Tasks are now retried if GitHub API fails with a "rate limit exceeded" message.
- Fix external redirection to test reports with names that include the `/` character.
- All GitHub API calls now use the `Authorization` header when using user tokens instead of the deprecated URL parameter (Scope Enterprise only).


## Scope v1.5.1

*February 07, 2020*

#### Added
- **New: Code Path**. The Scope agents for iOS, Java and .NET now support collecting per-test code coverage information that is accessible in the UI, in a new tab named "Code Path".
- **New: Email notifications**. Users can now subscribe to email notifications on a per-service basis, to receive emails every time a branch is "broken" or "fixed".
- **New: Test differential states**. Tests are now marked as "added" if they were seen for the first time and as "broken" or "fixed" if they changed status between commits.
- **New: Benchmark test support**. The test performance tab can now show performance historical information for benchmark tests, based on operations per second instead of test duration.
- **New: Manual testing support**. Tests performed using the Scope for Chrome extension are now shown in a separate section under "Local development".
- **New: Scope agent for Node.js**. The Scope agent for Javascript can now be used to instrument Node.js tests and applications.
- When tests are parametrized, their parameters now show on the UI.
- SQL statements are now syntax highlighted.

#### Changed
- Agents are now configured using a single parameter, Scope DSN, instead of API key and endpoint separately.
- The test status "ERROR" has been removed, and tests will show up as "FAIL" instead.
- Removed the test execution count column from the inspect view and replaced it with a small badge.
- Updates to Scope are now only available through the Helm CLI.
- Built-in TLS termination has been deprecated in favor of using ingress TLS.
- Sessions are now kept active for up to one week.
- Updated the Scope logo.

#### Fixed
- Fixed an issue when trying to ingest binary data.
- Several other small bug fixes.


## Scope v1.5.0

*December 23, 2019*

#### Added
- **New: Code Path**. The Scope agents for iOS, Java and .NET now support collecting per-test code coverage information that is accessible in the UI, in a new tab named "Code Path".
- **New: Email notifications**. Users can now subscribe to email notifications on a per-service basis, to receive emails every time a branch is "broken" or "fixed".
- **New: Test differential states**. Tests are now marked as "added" if they were seen for the first time and as "broken" or "fixed" if they changed status between commits.
- **New: Benchmark test support**. The test performance tab can now show performance historical information for benchmark tests, based on operations per second instead of test duration.
- **New: Manual testing support**. Tests performed using the Scope for Chrome extension are now shown in a separate section under "Local development".
- **New: Scope agent for Node.js**. The Scope agent for Javascript can now be used to instrument Node.js tests and applications.
- When tests are parametrized, their parameters now show on the UI.
- SQL statements are now syntax highlighted.

#### Changed
- Agents are now configured using a single parameter, Scope DSN, instead of API key and endpoint separately.
- The test status "ERROR" has been removed, and tests will show up as "FAIL" instead.
- Removed the test execution count column from the inspect view and replaced it with a small badge.
- Updates to Scope are now only available through the Helm CLI.
- Built-in TLS termination has been deprecated in favor of using ingress TLS.
- Sessions are now kept active for up to one week.
- Updated the Scope logo.

#### Fixed
- Fixed an issue when trying to ingest binary data.
- Several other small bug fixes.


## Scope v1.4.0

*November 06, 2019*

#### Added
- **New**: you can now open issues on GitHub with all the debugging information available directly from the test detail page.
- Source code snippets have now syntax highlighting.
- The test trace view now displays events on top of the spans.
- HTTP client and server spans now show payload data (if enabled in the agent).
- New onboarding design that includes getting started projects.

#### Changed
- Selecting a new branch on the Explore View resets any filter on the UI.
- Increased the density of commits on the performance tab of tests.
- Stacktrace frames are now expanded by default.
- Local development test report list now includes more information.

#### Fixed
- Bug that showed a blank page after deleting a namespace.
- Fixed the commits order on the Test Performance Tab.
- Several other minor bug fixes and enhancements


## Scope v1.3.3

*October 09, 2019*

#### Added
- New syntax highlighting for viewing source code.

#### Changed
- Selecting a new branch on the Explore View resets any filter on the UI.

#### Fixed
- Fixed a bug that showed a blank page after deleting a namespace.
- Fixed the commits order on the Test Performance Tab.
- Several other minor bug fixes and enhancements


## Scope v1.3.2

*October 08, 2019*

#### Added
- New syntax highlighting for viewing source code.

#### Changed
- Selecting a new branch on the Explore View resets any filter on the UI.

#### Fixed
- Bug that showed a blank page after deleting a namespace.
- Fixed the commits order on the Test Performance Tab.
- Several other minor bug fixes and enhancements


## Scope v1.3.1

*September 30, 2019*

#### Added
 - **New**: Test Report Performance tab, to visualize test duration over time for a specific test.
 - **New**: Javascript Agent, with initial support for Jest and Cypress.
 - **New**: Redesigned Test Report trace view.
- Added infinite scroll pagination to log views.

#### Changed
- After the Scope GitHub app is installed on a namespace, repositories are loaded asynchronously and in parallel.

#### Fixed
- Fixed a bug where removed repositories would not be reactivated after re-adding them.
- When applying the "flaky tests" filter on the Insights matrix, non-flaky results will still be shown.
- Fixed a bug where commits from other branches would show up on the history tab.
- Fixed GitHub checks when test names had spaces.
- Minor fixes on Go agent instructions.
- Tags now render correctly when the value is an object or an array.
- Various other performance enhancement and bug fixes.
- Branch name is now properly calculated when there is only a single commit in a branch


## Scope v1.3.0

*September 24, 2019*

#### Added
 - **New**: Test Report Performance tab, to visualize test duration over time for a specific test.
 - **New**: Javascript Agent, with initial support for Jest and Cypress.
 - **New**: Redesigned Test Report trace view.
- Added infinite scroll pagination to log views.

#### Changed
- After the Scope GitHub app is installed on a namespace, repositories are loaded asynchronously and in parallel.

#### Fixed
- Fixed a bug where removed repositories would not be reactivated after re-adding them.
- When applying the "flaky tests" filter on the Insights matrix, non-flaky results will still be shown.
- Fixed a bug where commits from other branches would show up on the history tab.
- Fixed GitHub checks when test names had spaces.
- Minor fixes on Go agent instructions.
- Tags now render correctly when the value is an object or an array.
- Various other performance enhancement and bug fixes.


## Scope v1.2.0

*September 05, 2019*

#### Added

* **New**: Service Insights page. We have added a test history matrix, where you can easily check each test status across commits.
* Added record counts to multiple tabs inside the test detail view.
* Added build information to the test detail view header.

#### Changed

* Redesigned namespace onboarding page.
* "Go To" buttons on the service list are now less prominent visually.

#### Fixed

* Fixed various bugs affecting GitHub checks.
* Fixed iOS instructions for local development.
* Fixed a bug that caused a backend crash when uploading certain iOS symbol files.
* Minor fixes on local development.
* Minor fixes on the explore view.


## Scope v1.1.1

*August 19, 2019*

#### Fixed
* Performance issues when loading commits for repositories with longer commit histories


## Scope v1.1.0

*August 09, 2019*

#### Added
- Explore page now includes an interactive test execution duration histogram, and a duration filter facet.
- Services and repositories in the service list can now be marked as favorite to pin them to the top.

#### Changed
- Installation and upgrades are now done using [Helm](https://helm.sh/). Please refer to Scope's documentation for more details.
- Agent metadata now appears in its own tab in event and span details.
- Tests in the explore view are now ordered by descending average execution time.

#### Fixed
- Fixed an issue when ingesting lots of test data from the same GitHub repository in a small amount of time
- Commit message should now be correctly formatted in service dashboard
- Stack trace should now appear in non-exception event reports
- Minor improvements in explore and test execution detail pages


## Scope v1.0.0

*July 16, 2019*

**Notes:**
* After the upgrade process finishes, administrators and users will be asked to login again.
* The GitHub app needs to be updated with "read" access to "Commit statuses", and a subscription to the "Check run", "Check suite" and "Status" events.

#### Added
- **New**: Test exceptions. Tests now have a new tab listing all exceptions that happened as part of its execution, with full page reports.
- **New**: Service dashboard. Now you can see a dashboard for each service, with a list of branches and commits, alongside aggregated test status and pull request status.
- **New**:  Redesigned Explore view, filtered by commit, with aggregated tests and filters by test name or suite.
- **New**: Test history. Now tests have a new tab "History" where results of the test in older and newer commits are shown to quickly identify where tests break.
- Events now have a full page report view.
- You are now able to choose a thread involved in an exception and see its stacktrace.
- When you are asked to login, the URL you were trying to access is preserved.
- Updated the 'Code' section on test executions, with the possibility of navigating the test source code.
- Tag and branch information is now visible on the test execution view.
- Added the ability to see the agent instructions on a namespace where all repositories have test results.
- Breadcrumbs now show the namespace and service being shown.
- Exceptions are now marked with an exclamation icon on the logs tab.
- Events now show the source code context of the line that generated the event (where possible).

#### Changed
- Users can now only see repositories which they have read access to on GitHub.
- Service list will show all branches in the repo and not just 5.
- Minor styling improvements in events list in test execution detail.
- Explore's status filter facet now keeps the counts when a status filter is applied.
- Scope core logs are now formatted in JSON.

#### Fixed
- Fixed minor style issues in stack trace visualization.
- Navigation of admin sections should be preserved on refresh. 
- Fixed a bug where the event search in test execution details would freeze when no results were found.
- Fixed GitHub annotations on Windows projects, or with more than 50 annotations.
- Fixed a possible deadlock when processing GitHub webhooks.
- Navigation of admin sections is now preserved on refresh. 
- Compatibility with Universal Naming Convention (UNC) paths on tracing metadata.
- Requests to GitHub are retried automatically on temporary server errors.
- Fixed several bugs on the "updates" section of the admin panel.


## Scope v0.4.0

*May 07, 2019*

**Added**
- **NEW: [GitHub checks](https://help.github.com/en/articles/about-status-checks#checks) support**. Now, Scope will create a [GitHub check](https://help.github.com/en/articles/about-status-checks#checks) for each commit with test results, including a summary table, list of failed, errored and flaky tests, and inline annotations for test failures and exceptions that include event metadata and stacktraces.
  - **Please note** that in order for this new feature to work, [the GitHub app needs read/write access to "Checks"](https://developer.github.com/apps/managing-github-apps/editing-a-github-app-s-permissions/).
- **NEW:** **Java and .NET agents**. The UI now includes instructions to install and use the new agents.
- **NEW:** event message search functionality.
- Now commits can be in a "running" state in the dashboard while tests are being executed.
- Namespaces now show their avatar on the left sidebar.
- Spans now include total and self time information.
- Added new interactive visualization for metadata fields of type `object`.
- Added search by test FQN in the explore view.
- Added new icons on the top right corner: a shortcut to the documentation site, and a prompt with information about new releases.

**Changed**
- Service colors for spans and events have changed for better visualization.

**Fixed**
- The backend data ingestion API now admits duplicate events from agents.
- GitHub stored metadata is now updated every time a webhook is received (to support, for example, repository name changes).
- Allow using `X-Forwarded-Proto` header from an external proxy.
- Various visual design fixes and enhancements.
- Minor bug fixes in the explore, test detail and service list views.


## Scope v0.3.0

*April 17, 2019*

**Added**

- iOS stacktrace symbolication support. **Please note that this requires iOS Agent version 0.2.0 or greater.**
  - Now `.dSYM` files can be uploaded to Scope and will be used to symbolicate stacktraces where possible.
  - The event detail UI now shows a `Stacktrace` tab if the event carries stack trace information.
  - This tab will show each of the frames in the stacktrace, along with a raw version of the stacktrace as reported by the application.
  - Symbolicated frames (with file and line information) will show their source code context inline.
- Add possibility to "Go to span" and "Go to event" in "Logs" and "Trace" tabs respectively
in test execution detail page.

**Changed**

- Span detail view has been redesigned from the ground up.
- The test execution header now includes commit information.
- Span and agent tags and event field values are now JSON strings on the GraphQL API. Span tags now support any numeric, boolean and string values, and event fields support numeric, boolean, string and nested object values.
- API access logging for the health check endpoint (`/_health`) has been disabled, and the format has been improved to show user and timing information.

**Fixed**

- The `Back` button in test execution detail page and the `Explore` link in the top bar breadcrumbs now preserve previously applied filters.
- Code tab should now syntax highlight supported languages properly.
- Fixed some issues when displaying very short spans in the trace view.
- Added `UNKNOWN` test status to the GraphQL API.
- Malformed agent payloads are not handled properly and result in a HTTP status code of 400.
- Other small bug fixes and enhancements.


## Scope v0.2.15

*April 03, 2019*

**Added**

* If an update fails, we now show an error message explaining the reason.
* Service cards now expand to fit the entire width of the browser viewport.
* Repositories added without test results are now shown on the UI.
* Links to source code files are now automatically detected and are linked to GitHub.
* Take repository name into account for calculating the color of spans and logs.
* Add number of services to trace view.

**Changed**

* Services are now ordered by most recent activity.
* The event detail view has been redesigned.
* We now show a button instead of a card to add a new repo to the service list.
* Service column in the event list now shows the repository name if there are events from multiple repos.
* Service cards do not show the namespace name substring in their title anymore.

**Fixed**

* Events are now ordered properly even if they have less than a millisecond difference in timestamp.
* Fixed a race condition when loading the cache in the UI that caused a blank screen on some cases.
* Fixed a problem where certain repositories could not be added to Scope.
* Other minor bug fixes and enhancements.


## Scope v0.2.14

*March 25, 2019*

**Added**

* Added an installation option `--secure-proxy-ssl-header` to specify the header used by a SSL-terminating proxy to forward the protocol used by the client.
* If updates fail, now they are rolled back automatically to the previous known working state.
* Implemented a "Add new repo" link in the service list view to quickly configure GitHub's installation and add a repository to Scope.

**Changed**

* The service list has been redesigned to show service cards with the latest active branches status.
* GitHub app now needs read/write permissions to "Checks".
* GitHub app no longer needs "Create" events, but now needs "Delete" events.
* Improved updates section on admin panel.

**Fixed**

* Now filter facets are still shown on the "Explore" view even if there are no results that match the filters.
* The left sidebar is now sticky, so the logout button is always visible.
* Infinite scrolling on the "Explore" view now works as expected.
* When logged in as an admin, going to `/dashboard` now redirects the user to `/admin` automatically.
* In the trace view, spans have now different colors if they come from different services.
* Events now show the correct service name.
* Branch and tag information is now automatically populated when a repository is added.
* Other minor bug fixes and enhancements.


## Scope v0.2.13

*March 10, 2019*

**Added**

* Agent instructions are now always shown on the service list view
* A new 'about' section in the admin panel now includes links to open source licenses reports
* The latest release notes are now always shown in the 'updates' section of the admin panel

**Fixed**

* Fixed a bug when linking Scope to GitHub.com
* Fixed performance issues when ingesting large payloads from agents

**Changed**

* The test detail view has been refactored
* Updated python agent instructions with new version


## Scope v0.2.12

*March 05, 2019*

**Fixed**

* Fixed bug when displaying commit authored times on service list

**Changed**

* Commits are now ordered by descending commit time instead of authored time on service list


## Scope v0.2.11

*March 05, 2019*

**Fixed**

* Fix bug when pushing the same commit more than once to the same repository

**Added**

* Installation is now idempotent, so it can be run more than once on the same namespace

**Changed**

* Kubernetes operations timeout has been increased from 2 minutes to 10.


## Scope v0.2.10

*March 04, 2019*

**Fixed**

* Fixed graceful shutdown of router component when being upgraded
* Fixed adding empty repositories
* Fixed handling of ping GitHub webhooks
* Other minor bug fixes and enhancements



