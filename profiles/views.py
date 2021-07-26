from django.views import generic
from . import models
from . import forms


class cityListView(generic.ListView):
    model = models.city
    form_class = forms.cityForm


class cityCreateView(generic.CreateView):
    model = models.city
    form_class = forms.cityForm


class cityDetailView(generic.DetailView):
    model = models.city
    form_class = forms.cityForm


class cityUpdateView(generic.UpdateView):
    model = models.city
    form_class = forms.cityForm
    pk_url_kwarg = "pk"


class usersListView(generic.ListView):
    model = models.users
    form_class = forms.usersForm


class usersCreateView(generic.CreateView):
    model = models.users
    form_class = forms.usersForm


class usersDetailView(generic.DetailView):
    model = models.users
    form_class = forms.usersForm


class usersUpdateView(generic.UpdateView):
    model = models.users
    form_class = forms.usersForm
    pk_url_kwarg = "pk"


class phone_numbersListView(generic.ListView):
    model = models.phone_numbers
    form_class = forms.phone_numbersForm


class phone_numbersCreateView(generic.CreateView):
    model = models.phone_numbers
    form_class = forms.phone_numbersForm


class phone_numbersDetailView(generic.DetailView):
    model = models.phone_numbers
    form_class = forms.phone_numbersForm


class phone_numbersUpdateView(generic.UpdateView):
    model = models.phone_numbers
    form_class = forms.phone_numbersForm
    pk_url_kwarg = "pk"


class profilesListView(generic.ListView):
    model = models.profiles
    form_class = forms.profilesForm


class profilesCreateView(generic.CreateView):
    model = models.profiles
    form_class = forms.profilesForm


class profilesDetailView(generic.DetailView):
    model = models.profiles
    form_class = forms.profilesForm


class profilesUpdateView(generic.UpdateView):
    model = models.profiles
    form_class = forms.profilesForm
    pk_url_kwarg = "pk"


class job_titlesListView(generic.ListView):
    model = models.job_titles
    form_class = forms.job_titlesForm


class job_titlesCreateView(generic.CreateView):
    model = models.job_titles
    form_class = forms.job_titlesForm


class job_titlesDetailView(generic.DetailView):
    model = models.job_titles
    form_class = forms.job_titlesForm


class job_titlesUpdateView(generic.UpdateView):
    model = models.job_titles
    form_class = forms.job_titlesForm
    pk_url_kwarg = "pk"


class fieldsListView(generic.ListView):
    model = models.fields
    form_class = forms.fieldsForm


class fieldsCreateView(generic.CreateView):
    model = models.fields
    form_class = forms.fieldsForm


class fieldsDetailView(generic.DetailView):
    model = models.fields
    form_class = forms.fieldsForm


class fieldsUpdateView(generic.UpdateView):
    model = models.fields
    form_class = forms.fieldsForm
    pk_url_kwarg = "pk"


class contact_infoListView(generic.ListView):
    model = models.contact_info
    form_class = forms.contact_infoForm


class contact_infoCreateView(generic.CreateView):
    model = models.contact_info
    form_class = forms.contact_infoForm


class contact_infoDetailView(generic.DetailView):
    model = models.contact_info
    form_class = forms.contact_infoForm


class contact_infoUpdateView(generic.UpdateView):
    model = models.contact_info
    form_class = forms.contact_infoForm
    pk_url_kwarg = "pk"


class countryListView(generic.ListView):
    model = models.country
    form_class = forms.countryForm


class countryCreateView(generic.CreateView):
    model = models.country
    form_class = forms.countryForm


class countryDetailView(generic.DetailView):
    model = models.country
    form_class = forms.countryForm


class countryUpdateView(generic.UpdateView):
    model = models.country
    form_class = forms.countryForm
    pk_url_kwarg = "pk"
