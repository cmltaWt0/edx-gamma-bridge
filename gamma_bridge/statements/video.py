import json

from . base import BaseGammaEvent


class BaseVideo(BaseGammaEvent):
    def get_uid(self, event):
        event_dict = event.get('event', '{}')
        event_dict = json.loads(event_dict)
        if event_dict:
            uid = '{}:{}:{}'.format(
                self.__class__.__name__,
                self.get_course_id(event),
                event_dict.get('id', ''),
            )
        return uid or ''

    def is_allowed_to_save(self, event):
        return True


class VideoStatement(BaseVideo):
    pass


class VideoPlayStatement(BaseVideo):
    pass


class VideoPauseStatement(BaseVideo):
    pass


class VideoCompleteStatement(BaseVideo):
    pass


class VideoSeekStatement(BaseVideo):
    pass


class VideoTranscriptStatement(BaseVideo):
    pass
