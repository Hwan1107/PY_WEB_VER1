from django.views.generic.base import TemplateView

from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required

class IndexView(TemplateView):
    template_name = 'index.html'

class UserCreationView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done')

class UserCreationDoneTV(TemplateView):
    template_name = 'registration/register_done.html'

class LoginRequiredMixin(object):
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)