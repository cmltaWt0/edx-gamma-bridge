"""
Add GamificationProcessor to event tracking backends list.
"""
__version__ = "0.0.1"

from django.conf import settings as django_settings

from gamma_bridge.settings import RG_GAMIFICATION_TRACKING_BACKENDS, RG_GAMIFICATION_TRACKING_PROCESSOR


default_app_config = 'gamma_bridge.apps.GamificationTrackingConfig'


GAMIFICATION_CONF = django_settings.FEATURES.get('RG_GAMIFICATION')


if (GAMIFICATION_CONF and GAMIFICATION_CONF.get('ENABLED') == True and
    GAMIFICATION_CONF.get('RG_GAMIFICATION_ENDPOINT') and hasattr(django_settings, 'EVENT_TRACKING_BACKENDS')):

    django_settings.EVENT_TRACKING_BACKENDS['tracking_logs']['OPTIONS']['processors'] += [
        {'ENGINE': RG_GAMIFICATION_TRACKING_PROCESSOR}
    ]
