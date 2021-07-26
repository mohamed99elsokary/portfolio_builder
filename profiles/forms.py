from django import forms
from . import models


class cityForm(forms.ModelForm):
    class Meta:
        model = models.city
        fields = [
            "city",
        ]


class usersForm(forms.ModelForm):
    class Meta:
        model = models.users
        fields = [
            "password",
            "email",
        ]


class phone_numbersForm(forms.ModelForm):
    class Meta:
        model = models.phone_numbers
        fields = [
            "number",
            "name",
            "profile_id",
        ]


class profilesForm(forms.ModelForm):
    class Meta:
        model = models.profiles
        fields = [
            "about",
            "image",
            "name",
            "birth_date",
            "country_id",
            "field_id",
            "user_id",
            "city_id",
            "job_titles_id",
        ]


class job_titlesForm(forms.ModelForm):
    class Meta:
        model = models.job_titles
        fields = [
            "job_title",
        ]


class fieldsForm(forms.ModelForm):
    class Meta:
        model = models.fields
        fields = [
            "field",
        ]


class contact_infoForm(forms.ModelForm):
    class Meta:
        model = models.contact_info
        fields = [
            "name",
            "icon",
            "url",
            "profile_id",
        ]


class countryForm(forms.ModelForm):
    class Meta:
        model = models.country
        fields = [
            "country",
        ]
