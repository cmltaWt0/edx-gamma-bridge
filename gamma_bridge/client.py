"""Gamification Client to send payload data."""
import logging

from django.conf import settings as django_settings

from gamma_bridge import settings
from gamma_bridge.tasks import publish_event_to_gamma

LOGGER = logging.getLogger(__name__)

GAMIFICATION_CONF = django_settings.FEATURES.get('RG_GAMIFICATION')
params = dict()

if (GAMIFICATION_CONF and GAMIFICATION_CONF.get('ENABLED') == True and
    GAMIFICATION_CONF.get('RG_GAMIFICATION_ENDPOINT')):

    params.update({
        'enabled': True,
        'endpoint': GAMIFICATION_CONF.get('RG_GAMIFICATION_ENDPOINT'),
        'secret': GAMIFICATION_CONF.get('SECRET'),
        'key': GAMIFICATION_CONF.get('KEY')
    })


class GamificationPublisher(object):
    """
    Gamification publisher.

    Work with Gamma default storage to interact with storage backend.
    """
    def publish_event(self, event):
        """
        params:
        event gamification event
        """
        publish_event_to_gamma(params, event, settings.GAMMA_FIRST_SLEEP_INTERVAL)


publisher = GamificationPublisher()
