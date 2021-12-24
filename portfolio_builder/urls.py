from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from django.conf import settings
from django.conf.urls.static import static

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from profiles import views as profiles

schema_view = get_schema_view(
    openapi.Info(
        title="Portofolio Maker ",
        default_version="V1",
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path("", profiles.portfolio),
    path("portfolio/", profiles.portfolio),
    path("cv/", profiles.cv),
    path("profiles/", include("profiles.urls")),
    path("skills/", include("skills.urls")),
    path("work_experience/", include("work_experience.urls")),
    path("education/", include("education.urls")),
    path("projects/", include("projects.urls")),
    path("achievement/", include("achievement.urls")),
    path("admin/", admin.site.urls),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0)),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
