# Organization Repo Bulk Clone

## Setup
Use the following to get setup

    virtualenv -p /usr/local/bin/python3 .venv
    source .venv/bin/activate
    pip install -r requirements.txt

Create a file called `github-access-token` with your GitHub personal access token

## Select the organizations

List the organizations you want to explore in `orgs.list`

    echo "usds" > orgs.list

## Pull repo list

    ./get-repos.py

A file `repos.list` will be created with the git clone URLs.

## Clone the repos

    ./bulk-git-clone.sh

This will clone repos to `out/<org-name>/<repo-name>`.


