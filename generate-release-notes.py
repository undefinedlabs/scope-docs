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
    'scope-swift-agent': {
        'first_version': '0.1.13',
        'id': 'swift-release-notes',
        'name': 'Scope Swift Agent'
    },
    'scope-python-agent': {
        'first_version': '0.2.0',
        'id': 'python-release-notes',
        'name': 'Scope Python Agent'
    },
    'scope-dotnet-agent': {
        'first_version': '0.1.0',
        'id': 'dotnet-release-notes',
        'name': 'Scope .NET Agent'
    },
    'scope-java-agent': {
        'first_version': '0.1.0',
        'id': 'java-release-notes',
        'name': 'Scope Java Agent'
    },
    'scope-go-agent': {
        'first_version': '0.1.0',
        'id': 'go-release-notes',
        'name': 'Scope Go Agent'
    },
    'scope-javascript-agent': {
        'first_version': '0.1.3',
        'id': 'javascript-release-notes',
        'name': 'Scope Javascript Agent'
    },
    'scope-for-chrome': {
        'first_version': '0.3.2',
        'id': 'scope-for-chrome-release-notes',
        'name': 'Scope For Chrome'
    },
    'scope-import': {
        'first_version': '0.1.1',
        'id': 'import-release-notes',
        'name': 'Scope Import'
    }
}

GITHUB_ENDPOINT = "https://api.github.com/graphql"
QUERY = '''
query($owner: String!, $name: String!, $after: String) {
  repository(owner: $owner, name: $name) {
    isPrivate
    releases(first: 100, orderBy: {field:CREATED_AT, direction:DESC}, after: $after) {
      pageInfo {
        endCursor
        hasNextPage
      }
      edges {
        node {
          id
          name
          description
          isPrerelease
          isDraft
          createdAt
          url
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

PUBLIC_RELEASE_TEMPLATE = '''
## <a href="{url}" target="_blank">{name} v{version}</a>

*{date}*

{notes}

'''


if __name__ == "__main__":
    if not GITHUB_TOKEN:
        print("Please specify GITHUB_TOKEN")
        exit(1)

    for name, component in COMPONENTS.items():
        releases = []
        has_next_page = True
        end_cursor = None
        while has_next_page:
            response = requests.post(GITHUB_ENDPOINT, json={'query': QUERY, 'variables': {'owner': 'undefinedlabs', 'name': name, 'after': end_cursor}},
                                             headers={'Authorization': 'token %s' % GITHUB_TOKEN})
            response.raise_for_status()
            result = response.json()
            repository = result['data']['repository']
            for node in repository['releases']['edges']:
                release = node['node']
                release_date = datetime.datetime.strptime(release['createdAt'], "%Y-%m-%dT%H:%M:%SZ")
                if not release['name'] or release['isDraft'] or release['isPrerelease'] or semantic_version.Version(release['name']) < semantic_version.Version(component['first_version']):
                    continue
                if repository['isPrivate']:
                    releases.append(
                        RELEASE_TEMPLATE.format(
                            name=component['name'],
                            version=release['name'],
                            date=release_date.strftime("%B %d, %Y"),
                            notes=release['description'],
                        )
                    )
                else:
                    releases.append(
                        PUBLIC_RELEASE_TEMPLATE.format(
                            name=component['name'],
                            version=release['name'],
                            date=release_date.strftime("%B %d, %Y"),
                            notes=release['description'],
                            url=release['url'],
                        )
                    )
            has_next_page = repository['releases']['pageInfo']['hasNextPage']
            end_cursor = repository['releases']['pageInfo']['endCursor']

        with open('docs/%s.md' % component['id'], 'w') as f:
            f.write(PAGE_TEMPLATE.format(id=component['id'], name=component['name'], releases=''.join(releases)))
