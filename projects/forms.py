from django import forms
from . import models


class bullet_pointsForm(forms.ModelForm):
    class Meta:
        model = models.bullet_points
        fields = "__all__"


class urlsForm(forms.ModelForm):
    class Meta:
        model = models.urls
        fields = "__all__"


class projectsForm(forms.ModelForm):
    class Meta:
        model = models.projects
        fields = "__all__"
