from django.contrib import admin
from django import forms

from . import models


admin.site.register(models.skills)
admin.site.register(models.categories)
admin.site.register(models.user_skills)
