import re
import requests
from collections import Counter
from math import sqrt
from time import sleep

def scoreRepo(owner, name):
    """
    Returns a score for a repo that depends on the number of contributors
    and the number of commits
    
    :param owner: name of Github repo owner
    :type owner: str
    :param name: name of Github repo
    :type name: str
    """

    # Get stats on contributions
    api_url = "https://api.github.com/repos/%s/%s/stats/contributors" % (
                owner, name)
    response = requests.get(api_url)
    info = response.json()
    
    # Calculate score
    commit_counts_per_user = [i['total'] for i in info]
    score = sum(map(sqrt, commit_counts_per_user))
    return score

 
def getRepoCommitInfo(url, csv_writer, github_user, github_password):
    """Writes info on all commits for a Github project to a CSV file
    File headers: (commit_id, user_email, project_name, timestamp)
    
    :param url: url for Github repo
    :type url: str
    :param csv_writer: csv file writer
    :type csv_writer: csv.csvwriter
    :param github_user: github username
    :type github_user: str
    :param github_password: github password
    :type github_password: str
    """
    
    # write csv headers
    headers = ('commit_id', 'user_email', 'project_name', 'timestamp')
    csv_writer.writerow(headers)
    
    # Get api url (w/o params)
    pattern = "github.com/(\w+)/(\w+)/?"
    owner, name = re.search(pattern, url).groups()
    api_url = "https://api.github.com/repos/%s/%s/commits" % (owner, name)
    
    # Get data on all commits
    # break when last_sha == next_sha in the response
    last_sha = ""
    
    while True:
        response = requests.get(
                    ''.join([api_url, "?per_page=100", last_sha]),
                    auth=(github_user, github_password))
        sleep(1) # so the rate limit is never exceeded
        info = response.json()
        next_sha = "&sha=%s" % info[-1]['sha']
        if last_sha == next_sha:
            break
        if last_sha != "":
            info.pop(0) # first commit will be the last commit from
                        # the previous request
        
        def makeRow(obj):
            try:
                commit = obj['commit']
                row = (obj['sha'], commit['author']['email'], name,
                    commit['author']['date'])
                return row
            except KeyError as exc:
                return (exc, obj)
        
        def printEntry(entry):
            if len(entry) == 2:
                # this could be better
                entry = ("error", "error", "error", "error")
            csv_writer.writerow(entry)
        
        rows = (makeRow(obj) for obj in info)
        map(printEntry, rows)
        last_sha = next_sha