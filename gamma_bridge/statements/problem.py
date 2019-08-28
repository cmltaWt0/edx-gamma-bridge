from . base import BaseGammaEvent


class BaseProblem(BaseGammaEvent):
    def get_uid(self, event):
        event_dict =  event.get('event', {})
        if event_dict:
            uid = '{}:{}:{}'.format(
                event_dict.get('problem_id', ''),
                self.get_course_id(event),
                self.get_username(event)
            )
        return uid or ''
    
    def is_allowed_to_save(self, event):
        return True


class ProblemCheckStatement(BaseProblem):   
    def get_uid(self, event):
        event_dict =  event.get('event', {})
        if event_dict:
            uid = '{}:{}:{}'.format(
                event_dict[0] if isinstance(event_dict, list) and len(event_dict) > 0 else event_dict,
                self.get_course_id(event),
                self.get_username(event)
            )
        return uid or ''

    def is_allowed_to_save(self, event):
        return True

class ProblemSubmittedStatement(BaseProblem):
    pass


class ProblemResetStatement(BaseProblem):
    pass


class ProblemGradedStatement(ProblemCheckStatement):
    pass
