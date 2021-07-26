from django import forms
from . import models


class achievementForm(forms.ModelForm):
    class Meta:
        model = models.achievement
        fields = [
            "text",
            "profile_id",
        ]


class hyperlinksForm(forms.ModelForm):
    class Meta:
        model = models.hyperlinks
        fields = [
            "url",
            "start_index",
            "end_index",
            "achievement_id",
        ]
