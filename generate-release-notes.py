#!/usr/bin/env python
import datetime
import os

import requests
import semantic_version

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
COMPONENTS = {
    'core': {
        'first_version': '0.2.10',
        'id': 'release-notes',
        'name': 'Scope'
    },
    'ios-agent': {
        'first_version': '0.1.13',
        'id': 'ios-release-notes',
        'name': 'Scope iOS Agent'
    },
    'python-agent': {
        'first_version': '0.2.0',
        'id': 'python-release-notes',
        'name': 'Scope Python Agent'
    },
    'csharp-agent': {
        'first_version': '0.1.0',
        'id': 'dotnet-release-notes',
        'name': 'Scope .NET Agent'
    },
    'java-agent': {
        'first_version': '0.1.0',
        'id': 'java-release-notes',
        'name': 'Scope Java Agent'
    },
    'go-agent': {
        'first_version': '0.1.0',
        'id': 'go-release-notes',
        'name': 'Scope Go Agent'
    },
}

GITHUB_ENDPOINT = "https://api.github.com/graphql"
QUERY = '''
query($owner: String!, $name: String!) {
  repository(owner: $owner, name: $name) {
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

PAGE_TEMPLATE = '''---
id: {id}
title: {name} release notes
sidebar_label: Release notes
---

{releases}

'''

RELEASE_TEMPLATE = '''
## {name} v{version}

*{date}*

{notes}

'''


if __name__ == "__main__":
    if not GITHUB_TOKEN:
        print("Please specify GITHUB_TOKEN")
        exit(1)

    for name, component in COMPONENTS.items():
        response = requests.post(GITHUB_ENDPOINT, json={'query': QUERY, 'variables': {'owner': 'undefinedlabs', 'name': name}},
                                 headers={'Authorization': 'token %s' % GITHUB_TOKEN})
        response.raise_for_status()
        result = response.json()
        releases = []
        for node in result['data']['repository']['releases']['edges']:
            release = node['node']
            release_date = datetime.datetime.strptime(release['createdAt'], "%Y-%m-%dT%H:%M:%SZ")
            if not release['name'] or release['isDraft'] or release['isPrerelease'] or semantic_version.Version(release['name']) < semantic_version.Version(component['first_version']):
                continue
            releases.append(
                RELEASE_TEMPLATE.format(
                    name=component['name'],
                    version=release['name'],
                    date=release_date.strftime("%B %d, %Y"),
                    notes=release['description']
                )
            )

        with open('docs/%s.md' % component['id'], 'w') as f:
            f.write(PAGE_TEMPLATE.format(id=component['id'], name=component['name'], releases=''.join(releases)))
