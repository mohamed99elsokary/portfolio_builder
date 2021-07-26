from django.urls import path

from .api import *


urlpatterns = [
    path("create/", create),
    path("edit/", edit),
    path("delete_education/", delete_education),
    path("add_course/", add_course),
    path("edit_course/", edit_course),
    path("delete_course/", delete_course),
]
