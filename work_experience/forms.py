from django import forms
from . import models


class work_experienceForm(forms.ModelForm):
    class Meta:
        model = models.work_experience
        fields = [
            "end_date",
            "start_date",
            "profile_id",
            "organizations_id",
        ]


class bullet_pointsForm(forms.ModelForm):
    class Meta:
        model = models.bullet_points
        fields = [
            "point_text",
            "work_experience_id",
        ]


class organizationsForm(forms.ModelForm):
    class Meta:
        model = models.organizations
        fields = [
            "icon",
            "name",
        ]
