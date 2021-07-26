from django.contrib import admin
from django import forms

from . import models


admin.site.register(models.city)
admin.site.register(models.phone_numbers)
admin.site.register(models.profiles)
admin.site.register(models.job_titles)
admin.site.register(models.fields)
admin.site.register(models.contact_info)
admin.site.register(models.country)
admin.site.register(models.Languages)
