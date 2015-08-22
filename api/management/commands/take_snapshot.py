from django.core.management import BaseCommand
from api.scrapers.cfa_scraper import scrape_brigades_and_projects


class Command(BaseCommand):
    help = 'Runs all of the scrapers.  Good for setting up a development machine with new data.'

    def handle(self, *args, **options):
        self.stdout.write('Scraping Brigades and Projects from CfA website...')
        scrape_brigades_and_projects()
        self.stdout.write('Finished scraping brigades and projects!')
