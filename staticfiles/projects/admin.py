from django.contrib import admin
from django import forms

from . import models


admin.site.register(models.bullet_points)
admin.site.register(models.urls)
admin.site.register(models.projects)
