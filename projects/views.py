from django.views import generic
from . import models
from . import forms


class bullet_pointsListView(generic.ListView):
    model = models.bullet_points
    form_class = forms.bullet_pointsForm


class bullet_pointsCreateView(generic.CreateView):
    model = models.bullet_points
    form_class = forms.bullet_pointsForm


class bullet_pointsDetailView(generic.DetailView):
    model = models.bullet_points
    form_class = forms.bullet_pointsForm


class bullet_pointsUpdateView(generic.UpdateView):
    model = models.bullet_points
    form_class = forms.bullet_pointsForm
    pk_url_kwarg = "pk"


class urlsListView(generic.ListView):
    model = models.urls
    form_class = forms.urlsForm


class urlsCreateView(generic.CreateView):
    model = models.urls
    form_class = forms.urlsForm


class urlsDetailView(generic.DetailView):
    model = models.urls
    form_class = forms.urlsForm


class urlsUpdateView(generic.UpdateView):
    model = models.urls
    form_class = forms.urlsForm
    pk_url_kwarg = "pk"


class projectsListView(generic.ListView):
    model = models.projects
    form_class = forms.projectsForm


class projectsCreateView(generic.CreateView):
    model = models.projects
    form_class = forms.projectsForm


class projectsDetailView(generic.DetailView):
    model = models.projects
    form_class = forms.projectsForm


class projectsUpdateView(generic.UpdateView):
    model = models.projects
    form_class = forms.projectsForm
    pk_url_kwarg = "pk"
