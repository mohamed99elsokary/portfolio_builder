from django.db import models
from django.urls import reverse


class award(models.Model):

    # Relationships
    profile_id = models.ForeignKey(
        "profiles.profiles",
        on_delete=models.CASCADE,
        related_name="profile_awards",
    )

    # Fields
    text = models.CharField(max_length=300, null=True, blank=True)
    order = models.IntegerField(default=None)

    def __str__(self):
        return str(self.pk)


class achievement(models.Model):

    # Relationships
    profile_id = models.ForeignKey(
        "profiles.profiles",
        on_delete=models.CASCADE,
        related_name="profile_achievements",
    )

    # Fields
    text = models.CharField(max_length=300, null=True, blank=True)
    order = models.IntegerField(default=None)

    def __str__(self):
        return str(self.pk)


class hyperlinks(models.Model):

    # Relationships
    achievement_id = models.ForeignKey(
        "achievement.achievement",
        on_delete=models.CASCADE,
        related_name="achievement_hyperlinks",
        null=True,
        blank=True,
    )
    award_id = models.ForeignKey(
        "achievement.award",
        on_delete=models.CASCADE,
        related_name="award_hyperlinks",
        null=True,
        blank=True,
    )

    # Fields
    url = models.URLField(null=True, blank=True)
    start_index = models.IntegerField(null=True, blank=True)
    end_index = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.pk)
