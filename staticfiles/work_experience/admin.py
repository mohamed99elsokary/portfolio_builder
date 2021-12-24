from django.contrib import admin
from django import forms

from . import models


admin.site.register(models.work_experience)
admin.site.register(models.bullet_points)
admin.site.register(models.organizations)
admin.site.register(models.tags)
