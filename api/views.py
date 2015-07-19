import json
from django.http import HttpResponse
from api.models import Brigade


def index(request):
    """
    Currently, this is an example of how to output JSON generated from something we retreived from the database.
    Eventually this will be replaced with something more useful :-)
    :param request:
    :return:
    """
    brigades = Brigade.objects.all()
    brigades = [brigade.name for brigade in brigades]

    return HttpResponse(json.dumps(brigades))
