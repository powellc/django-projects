from datetime import datetime

from django.template.context import RequestContext
from django.views.generic import list_detail
from django.shortcuts import render_to_response, get_object_or_404

from sermon.models import Sermon, Speaker, Reading

def index(request):
    sermons = Sermon.objects.all()[:5]
    return render_to_response('sermon/index.html', locals(),
                              context_instance=RequestContext(request))

def sermon_detail(request, slug):
    sermon=Sermon.objects.get(slug=slug)
    return render_to_response('sermon/sermon_detail.html', locals(),
                              context_instance=RequestContext(request))

def readings(request):
    readings=Reading.objects.all()
    return render_to_response('sermon/readings.html', locals(),
			      context_instance=RequestContext(request))
