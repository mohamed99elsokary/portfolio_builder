from django.urls import path

from .api import *


urlpatterns = [
    path("create_project/", create_project),
    path("edit_project/", edit_project),
    path("delete_project/", delete_project),
    path("add_bullet_point/", add_bullet_point),
    path("edit_bullet_point/", edit_bullet_point),
    path("delete_bullet_point/", delete_bullet_point),
    path("add_url/", add_url),
    path("edit_url/", edit_url),
    path("delete_url/", delete_url),
]
