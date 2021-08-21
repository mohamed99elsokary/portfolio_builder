from django.db import models
from django.urls import reverse


class bullet_points(models.Model):

    # Relationships

    project_id = models.ForeignKey(
        "projects.projects",
        on_delete=models.CASCADE,
        related_name="project_bullet_points",
    )

    # Fields
    point_text = models.TextField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.point_text)


class urls(models.Model):

    # Relationships

    project_id = models.ForeignKey(
        "projects.projects", on_delete=models.CASCADE, related_name="project_urls"
    )

    # Fields
    url = models.URLField(null=True, blank=True)
    name = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return str(self.name)


class projects(models.Model):

    # Relationships
    profile_id = models.ForeignKey(
        "profiles.profiles", on_delete=models.CASCADE, related_name="profiles_projects"
    )

    # Fields
    descreption = models.CharField(max_length=30, null=True, blank=True)
    icon = models.ImageField(upload_to="upload/projects_icons/", null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    name = models.CharField(max_length=300, null=True, blank=True)
    icon_url = models.URLField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.name)
