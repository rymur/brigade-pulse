import json
from django.http import HttpResponse
from api.models import Brigade


def index(request):
    brigades = Brigade.objects.all()
    brigades = [brigade.name for brigade in brigades]

    return HttpResponse(json.dumps(brigades))
