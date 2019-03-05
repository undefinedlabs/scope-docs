#!/usr/bin/env python
import datetime
import os

import requests

GITHUB_AUTH = os.getenv("GITHUB_AUTH")
FROM_DATE = datetime.datetime(year=2019, month=3, day=4)

GITHUB_ENDPOINT = "https://api.github.com/graphql"
QUERY = '''
query {
  repository(owner: "undefinedlabs", name: "core") {
    releases(last:100, orderBy:{field:CREATED_AT, direction:DESC}) {
      edges {
        node {
          id
          name
          description
          isPrerelease
          isDraft
          createdAt
        }
      }
    }
  }
}
'''

PAGE_TEMPLATE = '''
---
id: release-notes
title: Release notes
sidebar_label: Release notes
---

{releases}

'''

RELEASE_TEMPLATE = '''
## Scope v{version}

*{date}*

{notes}

'''


if __name__ == "__main__":
    if not GITHUB_AUTH:
        print("Please specify GITHUB_AUTH (in the format 'user:token')")
        exit(1)

    response = requests.post(GITHUB_ENDPOINT, json={'query': QUERY, 'variables': []},
                             auth=tuple(GITHUB_AUTH.split(':')))
    response.raise_for_status()
    result = response.json()
    releases = []
    for node in result['data']['repository']['releases']['edges']:
        release = node['node']
        release_date = datetime.datetime.strptime(release['createdAt'], "%Y-%m-%dT%H:%M:%SZ")
        if release['isDraft'] or release['isPrerelease'] or FROM_DATE > release_date:
            continue
        releases.append(
            RELEASE_TEMPLATE.format(
                version=release['name'],
                date=release_date.strftime("%B %d, %Y"),
                notes=release['description']
            )
        )

    print(PAGE_TEMPLATE.format(releases=''.join(releases)))
