from django.db import models
from django.urls import reverse


class skills(models.Model):

    # Relationships
    category_id = models.ForeignKey("skills.categories", on_delete=models.CASCADE)
    # Fields
    name = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return str(self.name)


class categories(models.Model):

    # Fields
    name = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return str(self.name)


class user_skills(models.Model):

    # Relationships
    profile_id = models.ForeignKey(
        "profiles.profiles", on_delete=models.CASCADE, related_name="profile_skills"
    )
    skills_id = models.ForeignKey("skills.skills", on_delete=models.CASCADE)

    category_id = models.ForeignKey(
        "skills.categories",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
        related_name="category",
    )
    # Fields
    projects_number = models.IntegerField(null=True, blank=True)
    sample_url = models.URLField(null=True, blank=True)
    level = models.IntegerField(null=True, blank=True)

    def __str__(self):
        if (self.level is None):
            self.level = ""
        show = f"{self.profile_id} {self.skills_id} {self.level}"
        return str(show)
