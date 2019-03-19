---
id: release-notes
title: Release notes
sidebar_label: Release notes
---


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



