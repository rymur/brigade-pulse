from celery.schedules import crontab
from celery.task import periodic_task
from api.scrapers.cfa_scraper import scrape_brigades_and_projects
from api.scrapers.github_scraper import scrape_github_repos_for_all_projects
from api.scrapers.meetup_scraper import scrape_events_from_meetup


@periodic_task(run_every=crontab(hour=0, minute=0), expires=60 * 60, time_limit=60 * 60, retry=False)
def run_scrapers_nightly():
    scrape_brigades_and_projects()
    scrape_events_from_meetup()
    scrape_github_repos_for_all_projects()
