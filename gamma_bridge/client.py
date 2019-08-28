"""Gamification Client to send payload data."""
import json
import socket
import logging
import importlib

from django.conf import settings

from gamma_bridge.storage import GammaStorage
from gamma_bridge import exceptions


GAMIFICATION_CONF = settings.FEATURES.get('RG_GAMIFICATION')
params = dict()

if (GAMIFICATION_CONF and GAMIFICATION_CONF.get('ENABLED') == True and
    GAMIFICATION_CONF.get('RG_GAMIFICATION_ENDPOINT')):

    params.update({
        'enabled': True,
        'endpoint': GAMIFICATION_CONF.get('RG_GAMIFICATION_ENDPOINT'),
        'secret': GAMIFICATION_CONF.get('KEY'),
        'key': GAMIFICATION_CONF.get('SECRET')
    })


LOGGER = logging.getLogger(__name__)
g_storage = GammaStorage(**params)


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
        try:
            g_resp = g_storage.save(event)
        except socket.gaierror as e:  # can't connect at all, no response
            raise exceptions.GammaConnectionError(message=event)

        if g_resp is None:
            return

        if g_resp.status_code == 200:
            LOGGER.info("Succeeded sending statement {}".format(event))
        elif g_storage.response_has_errors(g_resp):
            if g_storage.response_has_storage_errors(g_resp):
                LOGGER.info(
                    "Storage error during saving event statement {}/{} Details: {}".format
                    (event.get('username'), event.get('event_type'), g_resp.content))
            elif g_storage.request_unauthorised(g_resp):
                LOGGER.info("Unauthorized request during saving event statement {}/{} Details: {}".format
                    (event.get('username'), event.get('event_type'), g_resp.content))
            else:
                LOGGER.info("Error during saving event statement {}/{} Details: {}".format
                    (event.get('username'), event.get('event_type'), g_resp.content))


publisher = GamificationPublisher()
