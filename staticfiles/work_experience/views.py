from django.views import generic
from . import models
from . import forms


class work_experienceListView(generic.ListView):
    model = models.work_experience
    form_class = forms.work_experienceForm


class work_experienceCreateView(generic.CreateView):
    model = models.work_experience
    form_class = forms.work_experienceForm


class work_experienceDetailView(generic.DetailView):
    model = models.work_experience
    form_class = forms.work_experienceForm


class work_experienceUpdateView(generic.UpdateView):
    model = models.work_experience
    form_class = forms.work_experienceForm
    pk_url_kwarg = "pk"


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


class organizationsListView(generic.ListView):
    model = models.organizations
    form_class = forms.organizationsForm


class organizationsCreateView(generic.CreateView):
    model = models.organizations
    form_class = forms.organizationsForm


class organizationsDetailView(generic.DetailView):
    model = models.organizations
    form_class = forms.organizationsForm


class organizationsUpdateView(generic.UpdateView):
    model = models.organizations
    form_class = forms.organizationsForm
    pk_url_kwarg = "pk"
