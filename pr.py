#!/usr/bin/env python3
# -*- coding: utf_8 -*-
'''list-pr.py'''
import csv
import logging
import settings
from util import github as github_util
from util import util

def write_to_csv(pullrequests, filename):
    """write information to csv"""
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['name',
                      'number',
                      'url',
                      'title',
                      'state',
                      'user',
                      'created_at',
                      'updated_at',
                      'closed_at',
                      'merged_at']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for pullrequest in pullrequests:
            writer.writerow(pullrequest)

def main():
    '''main function'''
    # set up logging
    logging.basicConfig(
        level = logging.INFO,
        format = "%(asctime)s [%(levelname)s] %(message)s",
        handlers = [
            logging.FileHandler(settings.LOG_FILE),
            logging.StreamHandler()
        ])

    # initialize
    repos = []
    github_org, github_repo, github_token = util.init()
    github = github_util.Github(settings.API_ENDPOINT, github_org, github_token)

    # get all repos from organization
    if github_repo is None:
        repos = github.list_repos()
        logging.info("Get Pull Request informations for %s repositories", len(repos))
    else: # only get one repo
        repos.append(github.get_repo_info(github_repo))
        logging.info("Get Pull Request informations for %s", github_repo)

    # get all pull requests from all repos
    prs = github.get_prs(repos)
    logging.info("Found %s pull requests", len(prs))
    write_to_csv(prs, settings.OUTPUT_FILE)

if __name__ == "__main__":
    main()
