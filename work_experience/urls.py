from django.urls import path

from .api import *


urlpatterns = [
    path("create_work_experience/", create_work_experience),
    path("edit_work_experience/", edit_work_experience),
    path("delete_work_experience/", delete_work_experience),
    path("add_bullet_points/", add_bullet_points),
    path("edit_bullet_points/", edit_bullet_points),
    path("delete_bullet_points/", delete_bullet_points),
    
]
