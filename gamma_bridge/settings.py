"""
Settings for RG Gamification tracking app known as GAMMA.
"""

GAMMA_API_VERSION = 'v0'

RG_GAMIFICATION_TRACKING_PROCESSOR = 'gamma_bridge.processor.GamificationProcessor'

RG_GAMIFICATION_TRACKING_BACKENDS = {
    'logger': {
        'ENGINE': RG_GAMIFICATION_TRACKING_PROCESSOR,
        'OPTIONS': {
            'name': 'tracking'
        }
    }
}


GAMMA_API_SUFFIX = '/api/{}/gamma-profile/'.format(GAMMA_API_VERSION)

# TODO: Move this settings into the Edx settings.
GAMMA_FIRST_SLEEP_INTERVAL = 2
GAMMA_CELERY_MAX_RETRIES = 10
