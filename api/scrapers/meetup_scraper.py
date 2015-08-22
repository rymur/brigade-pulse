import json
import datetime
import time
import requests
from api.models import MeetupEvent, Brigade
from api.models.meetup.meetup_group import MeetupGroup
from api.snapshots.meetup_snapshots import MeetupGroupSnapshot, MeetupEventSnapshot

from settings import MEETUP_API_KEY


def scrape_events_from_meetup():
    for brigade in Brigade.objects.filter(events_url__isnull=False):
        if brigade.events_url == '':
            continue
        group_urlname = brigade.events_url
        if 'meetup.com/' in group_urlname:
            group_urlname = group_urlname.split('meetup.com/')[-1].replace('/', '')
        else:
            continue
        current_url = 'https://api.meetup.com/2/groups?group_urlname={}&key={}&sign=true&status=upcoming,past'.format(
            group_urlname, MEETUP_API_KEY)
        response = requests.get(current_url)
        time.sleep(.5)
        if response.status_code == 429:
            print "TOO MANY REQUESTS"
            print response.content
            print response.headers
        if response.status_code == 200:
            json_response = json.loads(response.content)
            results = json_response.get('results', None)
            if results and len(results) == 1:
                result = results[0]
                meetup_group = MeetupGroup.objects.filter(id=result['id']).first()
                if not meetup_group:
                    meetup_group = MeetupGroup(id=result['id'])
                meetup_group.name = result['name']
                meetup_group.description = result.get('description', None)
                meetup_group.rating = result.get('rating', None)
                meetup_group.organizer_name = result['organizer']['name']
                meetup_group.topics = ','.join([x['name'] for x in result.get('topics', None)])
                meetup_group.members = result['members']
                meetup_group.brigade = brigade
                meetup_group.save()
                MeetupGroupSnapshot().create_snapshot(meetup_group)

        current_url = 'https://api.meetup.com/2/events?group_urlname={}&key={}&sign=true&status=upcoming,past'.format(
            group_urlname, MEETUP_API_KEY)
        while current_url != '':
            response = requests.get(current_url)
            time.sleep(.5)
            if response.status_code == 429:
                print "TOO MANY REQUESTS"
                print response.content
                print response.headers
            if response.status_code != 200:
                break
            json_response = json.loads(response.content)
            results = json_response.get('results', None)
            if not results:
                break
            for result in results:
                meetup_event = MeetupEvent.objects.filter(id=result['id']).first()
                if not meetup_event:
                    meetup_event = MeetupEvent(id=result['id'])
                meetup_event.name = result['name']
                meetup_event.description = result.get('description', None)
                if result.get('venue', None):
                    meetup_event.venue_name = result['venue']['name']
                meetup_event.group_name = result['group']['name']
                meetup_event.event_url = result['event_url']
                meetup_event.start_time = datetime.datetime.utcfromtimestamp(result['time']/1000)
                meetup_event.end_time = meetup_event.start_time + datetime.timedelta(milliseconds=result.get('duration', 0))
                meetup_event.yes_rsvp_count = result['yes_rsvp_count']
                meetup_event.maybe_rsvp_count = result['maybe_rsvp_count']
                meetup_event.waitlist_count = result['waitlist_count']
                meetup_event.headcount = result['headcount']
                meetup_event.created_at = datetime.datetime.utcfromtimestamp(result['created']/1000)
                meetup_event.brigade = brigade
                meetup_event.save()
                MeetupEventSnapshot().create_snapshot(meetup_event)

            meta = json_response.get('meta', None)
            if not meta:
                break
            current_url = meta.get('next', '')
