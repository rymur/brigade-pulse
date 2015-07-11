import re
import requests
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


def scoreEvent(meetup_url, meetup_key):
    """
    Returns a score for an event in an organization's history

    :param meetup_url: url for meetup event
    :type meetup_url: str
    :param meetup_key: api key for meetup account
                       (https://secure.meetup.com/meetup_api/key/)
    :type meetup_key: str
    """

    magic = 5 # tbd

    # Get event info
    event_id = re.search("events/(\d+)/", meetup_url).groups(0)
    api_url = "https://api.meetup.com/2/event/%s" % event_id
    params = {"key": meetup_key}
    r = requests.get(api_url, params=params)
    sleep(0.5)
    info = r.json()

    # Calculate score (defaults to zero if error occurred in request
    score = info.get("yes_rsvp_count", 0) * magic
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
    params = {"per_page": 100}

    while True:
        continued = (last_sha != "")
        if continued:
            params["sha"] = last_sha
        response = requests.get(api_url, params=params,
                                auth=(github_user, github_password))
        sleep(3600/5000) # so the rate limit is never exceeded
        info = response.json()
        next_sha = info[-1]['sha']
        if last_sha == next_sha:
            break
        if continued:
            info.pop(0) # first commit will be the same as the last commit
                        # from the previous request

        def makeRow(obj):
            try:
                commit = obj['commit']
                row = (obj['sha'], commit['author']['email'], name,
                       commit['author']['date'])
                return row
            except KeyError:
                return ("error", "error", "error", "error")

        rows = (makeRow(obj) for obj in info)
        map(csv_writer.writerow, rows)
        last_sha = next_sha
        if len(info) < 100:
            break
