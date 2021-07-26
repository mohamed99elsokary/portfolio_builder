from django.urls import path
from rest_framework import routers

from . import api


urlpatterns = [
    path("<int:id>", api.get),
    path("create/", api.create),
    path("edit/", api.edit),
    # ----------------------------------------------------------------contact_info
    path("create_contact_info/", api.create_contact_info),
    path("edit_contact_info/", api.edit_contact_info),
    path("delete_contact_info/", api.delete_contact_info),
    # ----------------------------------------------------------------language
    path("add_language/", api.add_language),
    path("edit_language/", api.edit_language),
    path("delete_language/", api.delete_language),
    # ----------------------------------------------------------------phone_numbers
    path("add_phone_number/", api.add_phone_number),
    path("edit_phone_number/", api.edit_phone_number),
    path("delete_phone_number/", api.delete_phone_number),
]
