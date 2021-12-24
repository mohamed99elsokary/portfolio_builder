from django.urls import path

from .api import *


urlpatterns = [
    path("create_awards/", create_awards),
    path("edit_awards/", edit_awards),
    path("delete_awards/", delete_awards),
    path("create_achievements/", create_achievements),
    path("edit_achievements/", edit_achievements),
    path("delete_achievements/", delete_achievements),
    path("create_hyperlink/", create_hyperlinks),
    path("edit_hyperlink/", edit_hyperlinks),
    path("delete_hyperlink/", delete_hyperlinks),
]
