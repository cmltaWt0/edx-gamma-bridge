from . base import BaseGammaEvent, validate_event_fields


class BaseCourse(BaseGammaEvent):
    def get_uid(self, event):
        event_dict = event.get('event', {})
        validate_event_fields(event_dict, ['course_id', 'user_id', 'mode'])
        uid = '{}:{}:{}:{}'.format(
            self.__class__.__name__,
            event_dict.get('course_id'),
            event_dict.get('user_id'),
            event_dict.get('mode')
        )
        return uid
    
    def is_allowed_to_save(self, event):
        return True


class CourseEnrollmentStatement(BaseCourse):
    pass


class CourseUnenrollmentStatement(BaseCourse):
    pass


class CourseCompletionStatement(BaseCourse):
    pass
