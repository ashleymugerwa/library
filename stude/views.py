from django.views.generic import TemplateView, UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import Http404


from. import models
from. import forms


class HomeView(TemplateView):
    template_name = 'stude/home.html'


class AdminView(TemplateView):
    template_name = 'stude/admin.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(AdminView, self).dispatch(request, *args, **kwargs)


class PostUpdateView(UpdateView):
    model = models.Student
    form_class = forms.PostForm
    template_name = 'stude/update.html'
    success_url = '/'

    def post(self, request, *args, **kwargs):
        if getattr(request.user, 'first_name', None) == 'Ashley':
            raise Http404()
        return super(PostUpdateView, self).post(request, *args, **kwargs)