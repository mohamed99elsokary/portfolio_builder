from django.views import generic
from . import models
from . import forms


class achievementListView(generic.ListView):
    model = models.achievement
    form_class = forms.achievementForm


class achievementCreateView(generic.CreateView):
    model = models.achievement
    form_class = forms.achievementForm


class achievementDetailView(generic.DetailView):
    model = models.achievement
    form_class = forms.achievementForm


class achievementUpdateView(generic.UpdateView):
    model = models.achievement
    form_class = forms.achievementForm
    pk_url_kwarg = "pk"


class hyperlinksListView(generic.ListView):
    model = models.hyperlinks
    form_class = forms.hyperlinksForm


class hyperlinksCreateView(generic.CreateView):
    model = models.hyperlinks
    form_class = forms.hyperlinksForm


class hyperlinksDetailView(generic.DetailView):
    model = models.hyperlinks
    form_class = forms.hyperlinksForm


class hyperlinksUpdateView(generic.UpdateView):
    model = models.hyperlinks
    form_class = forms.hyperlinksForm
    pk_url_kwarg = "pk"
