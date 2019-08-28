"""Statements base for Gamma Event Log."""
from abc import ABCMeta, abstractmethod
import json
import re

from django.core.serializers.json import DjangoJSONEncoder
from django.conf import settings


class BaseGammaEvent(object):
    """
    Base class for Gamification Event Logs.
    """
    __metaclass__ = ABCMeta

    def __init__(self, event, *args, **kwargs):
        """
        Initialize an Gamma event statement from a tracking log event.
        """
        self.data = dict(
            event_type=self.get_type(event),
            username=self.get_username(event),
            course_id=self.get_course_id(event),
            org=self.get_org(event),
            uid=self.get_uid(event),
            event=json.dumps(self.get_event(event), cls=DjangoJSONEncoder) if settings.DEBUG else None,
            context=json.dumps(self.get_context(event), cls=DjangoJSONEncoder) if settings.DEBUG else None,
            full_event=json.dumps(event, cls=DjangoJSONEncoder) if settings.DEBUG else None,
        )

    def get_type(self, event):
        return re.sub('\.+', '_', event['event_type'])

    def get_username(self, event):
        return event['username']

    def get_course_id(self, event):
        return event.get('context', {}).get('course_id', '')
    
    def get_org(self, event):
        return event.get('context', {}).get('org_id', '')

    def get_event(self, event):
        return event.get('event', {})

    def get_context(self, event):
        return event.get('context', {})

    @abstractmethod
    def is_allowed_to_save(self, event):
        """
        THis is for a possible filtering on provider side.
        """
        pass

    @abstractmethod
    def get_uid(self, event):
        pass
