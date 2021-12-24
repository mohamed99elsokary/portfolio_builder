from django.urls import path

from .api import *


urlpatterns = [
    path("add_skill/", add_skill),
    path("edit_skill/", edit_skill),
    path("delete_skill/", delete_skill),
]
