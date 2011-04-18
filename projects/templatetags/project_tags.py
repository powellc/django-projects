import re

from django import template
from django.conf import settings
from django.db.models.query import Q
from django.db import models
from projects.models import Project

register = template.Library()

class GetProjectNode(template.Node):
    def __init__(self, slug, var_name):
        self.slug=slug
        self.var_name = var_name

    def render(self, context):
        project = Project.objects.get(slug=self.slug)
        context[self.var_name] = project
        return ''

@register.tag
def get_project(parser, token):
    """
    Gets a project with the specified slug.

    Syntax::

    {% get_project [slug] as [var_name] %}

    Example usage::

    {% get_project crop-walk-2010 as project %}
    """
    args = token.split_contents()
    argc = len(args)

    try:
        assert argc == 4
    except AssertionError:
        raise template.TemplateSyntaxError('Invalid get_project syntax.')
    # determine what parameters to use
    slug = var_name = None
    if argc == 4: t, slug, a, var_name = args

    return GetProjectNode(slug=slug, var_name=var_name)

class GetGroupProjectsNode(template.Node):
    def __init__(self, slug, count, var_name):
        self.slug=slug
        self.count=count
        self.var_name = var_name

    def render(self, context):
        if self.count == "all": projects = Project.objects.filter(group__slug=self.slug)
        elif self.count: projects = Project.objects.filter(group__slug=self.slug)[:self.count]
        context[self.var_name] = projects
        return ''

@register.tag
def get_group_projects(parser, token):
    """
    Gets projects with the specified group slug.

    Syntax::

    {% get_group_projects [count] from [slug] as [var_name] %}

    Example usage::

    {% get_group_projects 5 from social-justice as projects %}
    """
    args = token.split_contents()
    argc = len(args)

    try:
        assert argc == 6
    except AssertionError:
        raise template.TemplateSyntaxError('Invalid get_project syntax.')
    # determine what parameters to use
    slug = count = var_name = None
    if argc == 6: t, count, f, slug, a, var_name = args

    return GetGroupProjectsNode(slug=slug, count=count, var_name=var_name)

class GetProjectsNode(template.Node):
    def __init__(self, count, var_name):
        self.count=count
        self.var_name = var_name

    def render(self, context):
        if self.count == "all": projects = Project.objects.all()
        elif self.count: projects = Project.objects.all()[:self.count]
        context[self.var_name] = projects
        return ''

@register.tag
def get_projects(parser, token):
    """
    Gets active projects 

    Syntax::

    {% get_projects [count] as [var_name] %}

    Example usage::

    {% get_projects 5 as projects %}
    """
    args = token.split_contents()
    argc = len(args)

    try:
        assert argc == 4
    except AssertionError:
        raise template.TemplateSyntaxError('Invalid get_project syntax.')
    # determine what parameters to use
    count = var_name = None
    if argc == 4: t, count, a, var_name = args

    return GetProjectsNode(count=count, var_name=var_name)
