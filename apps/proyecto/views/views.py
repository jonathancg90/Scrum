from django.contrib.auth.decorators import login_required

class LoginRequired(object):

    def dispatch(self, *args, **kwargs):
        bound_dispatch = super(LoginRequired, self).dispatch   
        return login_required(bound_dispatch)(login_url='/scrum/login/',*args, **kwargs)