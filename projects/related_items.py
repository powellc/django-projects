from django.db import models
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

if 'articles' in settings.INSTALLED_APPS:
    from articles.models import Article
    class RelatedArticle(models.Model):
        article = models.ForeignKey(Article)
        content_type = models.ForeignKey(ContentType)
        object_id = models.PositiveIntegerField()
        content_object = generic.GenericForeignKey('content_type', 'object_id')
        
        def __unicode__(self):
            return self.article.__unicode__()

if 'photologue' in settings.INSTALLED_APPS:
    from photologue.models import Photo
    class RelatedPhoto(models.Model):
        photo = models.ForeignKey(Photo)
        content_type = models.ForeignKey(ContentType)
        object_id = models.PositiveIntegerField()
        content_object = generic.GenericForeignKey('content_type', 'object_id')
        
        def __unicode__(self):
            return self.photo.__unicode__()

