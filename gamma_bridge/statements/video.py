import json

from . base import BaseGammaEvent


class BaseCourse(BaseGammaEvent):
    def get_uid(self, event):
        event_dict =  event.get('event', {})
        event_dict = json.loads(event_dict)
        return event_dict.get('id', '') if event_dict else ''
    
    def is_allowed_to_save(self, event):
        return True


class VideoStatement(BaseCourse):
    pass


class VideoPlayStatement(BaseCourse):
    pass


class VideoPauseStatement(BaseCourse):
    pass


class VideoCompleteStatement(BaseCourse):
    pass


class VideoSeekStatement(BaseCourse):
    pass


class VideoTranscriptStatement(BaseCourse):
    pass
