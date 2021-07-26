from django import forms
from . import models


class skillsForm(forms.ModelForm):
    class Meta:
        model = models.skills
        fields = [
            "name",
        ]


class categoriesForm(forms.ModelForm):
    class Meta:
        model = models.categories
        fields = [
            "name",
        ]


class user_skillsForm(forms.ModelForm):
    class Meta:
        model = models.user_skills
        fields = [
            "projects_number",
            "sample_url",
            "profile_id",
            "skills_id",
        ]
