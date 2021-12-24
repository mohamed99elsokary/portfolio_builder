from django.db import models


class education(models.Model):

    # Relationships
    profile_id = models.ForeignKey(
        "profiles.profiles", related_name="profile_education", on_delete=models.CASCADE
    )

    organization_id = models.ForeignKey(
        "work_experience.organizations",
        on_delete=models.CASCADE,
        related_name="organization_educations",
    )

    # Fields
    end_date = models.DateField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    field_name = models.CharField(max_length=255 , null=True, blank=True , default=None)

    def __str__(self):
        return str(self.profile_id)


class courses(models.Model):

    # Relationships
    profile_id = models.ForeignKey(
        "profiles.profiles", related_name="profile_courses", on_delete=models.CASCADE , null=True , blank=True, default=None  )

    organization = models.ForeignKey(
        "work_experience.organizations",
        on_delete=models.CASCADE,
        related_name="organization_courses",
        null=True, blank=True, default=None )
    # Fields
    certificate_url = models.URLField(null=True, blank=True)
    name = models.CharField(max_length=300, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    course_expected_time = models.CharField(max_length=30, null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    is_highlighted = models.BooleanField(default=False, blank=True)
    certificate_file = models.FileField(
        upload_to="upload/files/course_certificate", null=True, blank=True
    )

    def __str__(self):
        return str(self.name)
