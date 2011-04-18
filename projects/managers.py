from django.db.models import Manager, Q
import datetime

class OngoingManager(Manager):
    """Returns all objects with no end date, or an end date after our current date"""
    def get_query_set(self):
        return super(OngoingManager, self).get_query_set().filter(Q(end__gte=datetime.now())|Q(end=None))

class FinishedManager(Manager):
    """Returns all objects with an end date before our current date"""
    def get_query_set(self):
        return super(FinishedManager, self).get_query_set().filter(end__lte=datetime.now())
