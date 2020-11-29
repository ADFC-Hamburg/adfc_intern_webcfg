from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin

from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin

from django.views.generic import CreateView, UpdateView, DeleteView

# Create your views here.
from django.http import HttpResponse

from openslides_cfg.models import OpenSlidesInstance
from openslides_cfg.tables import OpenSlidesInstanceTable
from openslides_cfg.forms import OpenSlidesForm
#from openslides_cfg.filters import OpenSlidesFilter
from django.http import Http404

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class MainView(LoginRequiredMixin, PermissionRequiredMixin, SingleTableMixin, FilterView):
    login_url = '/saml2/login/'
    permission_required = 'openslides_cfg.view_OpenSlidesInstance'
    #filterset_class = OpenSlidesFilter
    template_name = 'main.html'
    model = OpenSlidesInstance
    table_class = OpenSlidesInstanceTable
    def get_queryset(self):
      return OpenSlidesInstance.objects.filter(created_by=self.request.user)

class DetailView(LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin, UpdateView):
    login_url = '/saml2/login/'
    permission_required = 'openslides_cfg.change_OpenSlidesInstance'
    model = OpenSlidesInstance
    template_name = 'detail.html'
    form_class = OpenSlidesForm
    success_url = '/'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['TITLE_KURZ'] = 'Bearbeiten'
        context['TITLE_LANG'] = 'Eintrag bearbeiten'
        return context
    def test_func(self):
        obj = self.get_object()
        return obj.created_by == self.request.user

class CreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    login_url = '/saml2/login/'
    permission_required = 'openslides_cfg.add_OpenSlidesInstance'
    model = OpenSlidesInstance
    template_name = 'detail.html'
    form_class = OpenSlidesForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['TITLE_KURZ'] = 'Anlegen'
        context['TITLE_LANG'] = 'neues OpenSlides anlegen'
        return context

class OSDeleteView(DeleteView):
    login_url = '/saml2/login/'
    permission_required = 'openslides_cfg.change_OpenSlidesInstance'
    model = OpenSlidesInstance
    template_name = 'confirm_delete.html'
    success_url = '/'