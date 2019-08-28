"""Default RG Gamification backend."""

import json
import requests
import urlparse

from gamma_bridge import exceptions, settings


class GammaStorage(object):
    """
    RG Gamification default backend known as GAMMA.
    """
    def __init__(self, enabled=False, endpoint=None, key=None, secret=None):
        self.is_enabled = all((enabled, endpoint, key, secret))
        self.endpoint = endpoint
        self.key = key
        self.secret = secret

    def save(self, event):
        headers = {
            'App-key': self.key,
            'App-secret': self.secret
        }
        if self.is_enabled:
            return requests.put(
                urlparse.urljoin(self.endpoint, settings.GAMMA_API_SUFFIX),
                data=event,
                headers=headers,
                verify=False
            )

    def response_has_errors(self, response_data):
        return 'Error' in json.loads(response_data.content)

    def request_unauthorised(self, response_data):
        return 'unauthorised' in json.loads(response_data.content).get('Error', '')

    def response_has_storage_errors(self, response_data):
        return 'warnings' in json.loads(response_data.content).get('Error', '')
