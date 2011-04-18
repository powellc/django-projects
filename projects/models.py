from datetime import datetime
from django.db import models
from django.db.models import permalink
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

from django_extensions.db.models import TitleSlugDescriptionModel,  TimeStampedModel
from markup_mixin.models import MarkupMixin

from projects.managers import OngoingManager, FinishedManager
from projects.related_items import RelatedArticle, RelatedPhoto
from eventy.models import RelatedEvent

class Project(MarkupMixin, TimeStampedModel, TitleSlugDescriptionModel):
    start      = models.DateField(_('Start'), blank=True, null=True, auto_now=True)
    end        = models.DateField(_('End'), blank=True, null=True)
    created_by = models.ForeignKey(User)
    template   = models.CharField(_('Template'), max_length=255, blank=True, null=True, help_text="Defaults to projects/project_detail.html")
    try:
        from committees.models import Group, Person


        group   = models.ForeignKey(Group)
        contact = models.ForeignKey(Person)
    except:
        group = models.CharField(_('Group'), max_length=144, blank=True, null=True)
        contact = models.CharField(_('Contact'), max_length=144, blank=True, null=True)

    articles = generic.GenericRelation(RelatedArticle)
    photos   = generic.GenericRelation(RelatedPhoto)
    events   = generic.GenericRelation(RelatedEvent)

    class Meta:
        verbose_name = _('Project')
        verbose_name_plural = _('Projects')
        get_latest_by = 'start'

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        args=[self.slug]
        return reverse('pj-project-detail', args=args)

