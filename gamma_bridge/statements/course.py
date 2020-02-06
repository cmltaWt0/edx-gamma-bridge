from . base import BaseGammaEvent


class BaseCourse(BaseGammaEvent):
    def get_uid(self, event):
        event_dict = event.get('event', {})
        if event_dict:
            uid = '{}:{}:{}:{}'.format(
                self.__class__.__name__,
                event_dict.get('course_id', ''),
                event_dict.get('user_id', ''),
                event_dict.get('mode', '')
            )
        return uid or ''
    
    def is_allowed_to_save(self, event):
        return True


class CourseEnrollmentStatement(BaseCourse):
    pass


class CourseUnenrollmentStatement(BaseCourse):
    pass


class CourseCompletionStatement(BaseCourse):
    pass
