from django.views import generic
from . import models
from . import forms


class skillsListView(generic.ListView):
    model = models.skills
    form_class = forms.skillsForm


class skillsCreateView(generic.CreateView):
    model = models.skills
    form_class = forms.skillsForm


class skillsDetailView(generic.DetailView):
    model = models.skills
    form_class = forms.skillsForm


class skillsUpdateView(generic.UpdateView):
    model = models.skills
    form_class = forms.skillsForm
    pk_url_kwarg = "pk"


class categoriesListView(generic.ListView):
    model = models.categories
    form_class = forms.categoriesForm


class categoriesCreateView(generic.CreateView):
    model = models.categories
    form_class = forms.categoriesForm


class categoriesDetailView(generic.DetailView):
    model = models.categories
    form_class = forms.categoriesForm


class categoriesUpdateView(generic.UpdateView):
    model = models.categories
    form_class = forms.categoriesForm
    pk_url_kwarg = "pk"


class user_skillsListView(generic.ListView):
    model = models.user_skills
    form_class = forms.user_skillsForm


class user_skillsCreateView(generic.CreateView):
    model = models.user_skills
    form_class = forms.user_skillsForm


class user_skillsDetailView(generic.DetailView):
    model = models.user_skills
    form_class = forms.user_skillsForm


class user_skillsUpdateView(generic.UpdateView):
    model = models.user_skills
    form_class = forms.user_skillsForm
    pk_url_kwarg = "pk"
