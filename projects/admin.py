from django.contrib import admin
from django.conf import settings
from django.contrib.contenttypes import generic

from projects.models import Project

try:
    from projects.related_items import RelatedArticle
except:
    pass

try:
    from projects.related_items import RelatedPhoto
except:
    pass

try:
    from eventy.models import RelatedEvent
except:
    pass

class GenericArticleInline(generic.GenericStackedInline):
    max_num = 2
    model = RelatedArticle

class GenericPhotoInline(generic.GenericStackedInline):
    max_num = 2
    model = RelatedPhoto

class GenericEventInline(generic.GenericStackedInline):
    max_num = 2
    model = RelatedEvent

class ProjectAdmin(admin.ModelAdmin):
    
    list_display = ('title', 'start', 'end', 'group', 'contact',)
    search_fields = ('title','description',)
    list_filter = ('group','contact',)
    inlines=[]
    if 'articles' in settings.INSTALLED_APPS:
        inlines.insert(0, GenericArticleInline)
    if 'photologue' in settings.INSTALLED_APPS:
        inlines.insert(0, GenericPhotoInline)
    if 'eventy' in settings.INSTALLED_APPS:
        inlines.insert(0, GenericEventInline)
    
admin.site.register(Project, ProjectAdmin)
