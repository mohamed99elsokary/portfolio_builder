from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from . import api


urlpatterns = [
    # path("login/", include("rest_framework.urls")),
    path("login/", api.login),
    path("register/", api.register),
    path("edit/", api.edit),
    path("<int:id>", api.get),
    path("", api.get_all),
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
