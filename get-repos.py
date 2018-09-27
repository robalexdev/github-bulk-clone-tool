#!/usr/bin/env python

from github import Github

with open('github-access-token', 'r') as f:
    access_token = f.read().strip()

g = Github(access_token)

with open('orgs.list', 'r') as f:
    orgs = [ _.strip() for _ in f.readlines() ]

repos = set([])

for org in orgs:
    git_org = g.get_organization(org)
    repos.update([ org + ' ' + _.name + ' ' + _.ssh_url for _ in git_org.get_repos() ])

with open('repos.list', 'w') as f:
    f.write('\n'.join(sorted(repos)))

