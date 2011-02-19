from django.contrib import admin
from sermon.models import Sermon, Reading, Speaker

class SermonAdmin(admin.ModelAdmin):
    
    list_display = ('title', 'speaker', 'date', 'published', 'publish_on')
    search_fields = ('title','body','speaker',)
    list_filter = ('published','speaker',)
    
admin.site.register(Sermon, SermonAdmin)
admin.site.register(Reading)
admin.site.register(Speaker)
