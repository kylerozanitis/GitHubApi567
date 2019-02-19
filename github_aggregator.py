""" This program requests repository and commit information from GitHub using
the requests & json modules and the public GitHub API. """

# Modules
import requests
import json


def gather_repos(github_id):
    """ This function takes a username as input and returns a list of
    repositories found in Github for that user ID. """
    repos_list = []

    url = 'https://api.github.com/users/' + github_id + '/repos'
    response = requests.get(url)
    
    repos = json.loads(response.text)

    for repo in repos:
        if repo['name']:
            repos_list.append(repo['name'])
        elif repo['full_name']:
            repos_list.append(repo['full_name'])
        else:
            repos_list.append(repo['id'])

    return repos_list