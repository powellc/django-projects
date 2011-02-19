from django.db.models import Manager
import datetime


class PublicManager(Manager):
    """Returns published sermons that are not in the future."""

    def published(self):
        return self.get_query_set().filter(published=True, publish_on__lte=datetime.datetime.now())