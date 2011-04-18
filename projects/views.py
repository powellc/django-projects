import logging
from datetime import datetime
from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
from django.views.generic import DetailView

from projects.models import Project

class ProjectDetailView(DetailView):
    model = Project
    template_name_field='template'
