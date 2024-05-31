#!/usr/bin/env python3
# -*- coding: utf_8 -*-
'''github.py'''
import logging
import requests

class Github:
    '''Github class'''
    def __init__(self, endpoint, org, token):
        self.endpoint = endpoint
        self.org = org
        self.token = token

    def list_repos(self):
        """list repos"""
        repos = []
        endpoint_url = f'{self.endpoint}/orgs/{self.org}/repos?per_page=100'
        while endpoint_url:
            response = requests.get(endpoint_url, headers={'Authorization': f'bearer {self.token}'})
            if response.status_code == 200:
                response_json = response.json()
                for repo in response_json:
                    repos.append({'name': repo['name'], 'pulls_url': repo['pulls_url'].replace('{/number}', '')})
                if 'next' in response.links:
                    endpoint_url = response.links['next']['url']
                else:
                    endpoint_url = None
            else:
                logging.error("Error: %s", response.status_code)
                endpoint_url = None
        return repos

    def get_repo_info(self, repo):
        """get repo info - only return pr url without using API"""
        return {'name': repo, 'pulls_url': f'{self.endpoint}/repos/{self.org}/{repo}/pulls'}

    def get_prs(self, repos):
        """get pull requests"""
        pullrequests = []
        for repo in repos:
            pulls_url = repo['pulls_url']
            repo_name = repo['name']
            endpoint_url = f'{pulls_url}?state=all&per_page=100'
            while endpoint_url:
                response = requests.get(endpoint_url,
                                        headers={'Authorization': f'bearer {self.token}'})
                if response.status_code == 200:
                    response_json = response.json()
                    for pullrequest in response_json:
                        pullrequests.append({'name': repo_name,
                                    'number': pullrequest['number'],
                                    'url': pullrequest['url'],
                                    'title': pullrequest['title'],
                                    'state': pullrequest['state'],
                                    'user': pullrequest['user']['login'],
                                    'created_at': pullrequest['created_at'],
                                    'updated_at': pullrequest['updated_at'],
                                    'closed_at': pullrequest['closed_at'],
                                    'merged_at': pullrequest['merged_at']})
                    if 'next' in response.links:
                        endpoint_url = response.links['next']['url']
                    else:
                        endpoint_url = None
                elif response.status_code == 204:
                    logging.info("Empty Repository: %s", repo_name)
                    endpoint_url = None
                else:
                    logging.error("Get Pull Request Error: %s", response.status_code)
                    endpoint_url = None
        return pullrequests
