# GitHub Pull Request Analysis

## Introduction
This script generates csv files with the following information about pull requests in a GitHub repository:
- Name of repository
- PR Number
- PR Title
- PR State
- PR User
- PR Created At
- PR Updated At
- PR Closed At
- PR Merged At

## Requirements
- Python 3.6 or higher
- GitHub Personal Access Token 
  - "Metadata" repository permissions (read)
  - "Pull requests" repository permissions (read)
- `pip install -r requirements.txt`

### Usage
For all repositories in an organization<br>
`python pr.py -o <organization> -t <github_token>`

For only one repository<br>
`python pr.py -o <organization> -r <repository> -t <github_token>`

### Reference
https://docs.github.com/en/rest/pulls/pulls?apiVersion=2022-11-28#list-pull-requests
https://docs.github.com/en/enterprise-cloud@latest/rest/repos/repos?apiVersion=2022-11-28

### Samples
- CSV Sample (Microsoft/VSCode) : https://github.com/junkofujiwara/pr-analysis/blob/main/samples/vscode.csv
- Tableau Dashboard Sample: https://public.tableau.com/app/profile/junko.fujiwara.gh/viz/GitHubPullRequestAnalaysis/Dashboard
![image](https://github.com/junkofujiwara/pr-analysis/assets/84257987/fea314ef-ac6e-43db-a92d-5d6ec4d0f52c)
