from django.db import models
from django.urls import reverse


class work_experience(models.Model):

    # Relationships
    profile_id = models.ForeignKey(
        "profiles.profiles",
        related_name="profile_work_experience",
        on_delete=models.CASCADE,
    )
    organizations_id = models.ForeignKey(
        "work_experience.organizations", on_delete=models.CASCADE
    )
    # Fields
    job_title = models.CharField(max_length=50, null=True, blank=True, default=None)
    end_date = models.DateField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.pk)


class bullet_points(models.Model):

    # Relationships
    work_experience_id = models.ForeignKey(
        "work_experience.work_experience",
        on_delete=models.CASCADE,
        related_name="work_bullet_points",
    )

    # Fields
    point_text = models.TextField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.pk)


class organizations(models.Model):

    # Fields
    icon = models.ImageField(
        upload_to="upload/organizations_icon/", null=True, blank=True
    )
    icon_url = models.URLField(max_length=200, null=True, blank=True, default=None)

    name = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return str(self.name)


class tags(models.Model):
    # Relationships

    organization_id = models.ManyToManyField(
        organizations,
        related_name="organization_tags",
    )
    # Fields

    tag = models.CharField(
        max_length=150,
        null=True,
        blank=True,
    )

    def __str__(self):
        return str(self.tag)
