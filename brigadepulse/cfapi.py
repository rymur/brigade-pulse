import requests


def get_all_organizations():
    '''
    Get all CFA organizations from the CFA organizations API
    http://codeforamerica.org/api/#api-organizations
    '''
    brigades = get_all_pages_cfa_api_endpoint("http://codeforamerica.org/api/organizations?per_page=1000")

    return brigades


def get_organization_projects(all_projects_urls):
    '''
    Get all projects for a CFA organization from the CFA projects API given
    the url to its projects endpoint
    http://codeforamerica.org/api/#api-projects
    '''
    projects = get_all_pages_cfa_api_endpoint(all_projects_urls + "?per_page=1000")
    return projects


def get_all_pages_cfa_api_endpoint(url):
    '''
    Execute a call against the CFA organizations API, paging until it reaches
    the end (http://codeforamerica.org/api)

    CFA limits result sets from its API to 1000 items.  We can page using the
    "pages" dict included in the response, which has the url of the next page
    of API results in the "next_page" key.  If there are no more pages the
    "pages" dict is empty.

    Returns: Complete list of concatenated "objects" properties from a normal
    CFA API call
    '''
    results, next_page_url = get_page_of_cfa_api_endpoint(url)

    # CFA limits responses to 1000 objects.  It pages with a "pages" dict that
    # has the url of the next page of API results in the "next_page" key.  If
    # there are no more pages the "pages" dict is empty.
    while next_page_url:
        page_of_results, next_page_url = get_page_of_cfa_api_endpoint(next_page_url)
        results.extend(page_of_results)

    return results


def get_page_of_cfa_api_endpoint(url):
    response = requests.get(url).json()
    page_of_objects = response["objects"]
    next_page_url = response["pages"].get("next_page", None)

    return page_of_objects, next_page_url
