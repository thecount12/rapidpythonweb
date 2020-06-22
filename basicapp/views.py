from django.shortcuts import render

from django import forms 
from basicapp.models import Traffic
import datetime
from blog import views 


def index(request):
    ipforwarded = request.META.get('HTTP_X_FORWARDED_FOR', None)
    # print ipforwarded
    if ipforwarded:
        ipforwarded = ipforwarded.split(", ")[0]
    else:
        ipforwarded = request.META.get("REMOTE_ADDR", "")
        # print ipforwarded
    try:
        Traffic.objects.create(ip=ipforwarded, created=datetime.datetime.now(), session=request.session.session_key)
    except Exception as err:
        print("Error: %s" % str(err)	)
    # print request.session.session_key
    return render(None, "index.html")

