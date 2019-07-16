---
id: release-notes
title: Scope release notes
sidebar_label: Release notes
---


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



