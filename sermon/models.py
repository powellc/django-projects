from django.db import models
from django.db.models import permalink
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from datetime import datetime

class StandardMetadata(models.Model):
    """
    A basic (abstract) model for metadata.

        Included in each model file to maintain application separation.

        Subclass new models from 'StandardMetadata' instead of 'models.Model'.
    """
    created = models.DateTimeField(default=datetime.now, editable=False)
    updated = models.DateTimeField(default=datetime.now, editable=False)
    owner = models.ForeignKey(User, blank=True, null=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.updated = datetime.now()
        super(StandardMetadata, self).save(*args, **kwargs)

class Speaker(models.Model):
    title = models.CharField(max_length=30, blank=True, null=True)
    name = models.CharField(max_length=60)
    
    def __unicode__(self):
	return self.title + " " + self.name	


class Reading(models.Model):
    source = models.CharField(_('source'), max_length=255)
    text = models.TextField(_('text'))

    def __unicode__(self):
        return self.source


class Sermon(StandardMetadata):
    speaker = models.ForeignKey(Speaker)
    date = models.DateField()
    title = models.CharField(_('title'), max_length=150)
    slug = models.SlugField(_('slug'), unique=True)
    readings = models.ManyToManyField(Reading, blank=True, null=True)
    mp3file = models.FileField(upload_to="sermons/",help_text=_("This should be a low quality version (preferably 18kbps), because it will be used for the Flash player."))
    largemp3file = models.FileField(upload_to="sermons/",blank=True,help_text=_("Optional. Preferably a 64kps version."))
    body = models.TextField(_('body'))
    published = models.BooleanField(_('published'), default=True)

    def __unicode__(self):
        return self.date.isoformat() + " - '" + self.title + "' - " + self.speaker.name

    def get_absolute_url(self):
        args=[self.slug]
        return reverse('sr-sermon-detail', args=args)

