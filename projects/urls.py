from django.conf.urls.defaults import *
from django.conf import settings

from django.views.generic import ListView, DetailView
from projects.models import Project

urlpatterns = patterns('projects.views',
    url (r'^$', view=ListView.as_view(model=Project), name='pj-project-list', ),
    url (r'^(?P<slug>[-\w]+)/$',
        view=DetailView.as_view(model=Project,template_name_field='template'), 
        name='pj-project-detail', ),
)
