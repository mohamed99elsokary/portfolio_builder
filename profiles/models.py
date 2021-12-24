from django.contrib.auth.models import User
from django.db import models
from rest_framework.authtoken.models import Token


class country(models.Model):

    # Fields
    country = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return str(self.country)


class city(models.Model):

    # Fields

    country = models.ForeignKey("profiles.country", on_delete=models.CASCADE)
    city = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return str(self.city)


class job_titles(models.Model):

    # Fields
    job_title = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return str(self.job_title)


class fields(models.Model):

    # Fields
    field = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return str(self.field)


# ----------------------------------------------------------------#


class profiles(models.Model):

    # Relationships

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    field_id = models.ForeignKey(
        "profiles.fields", on_delete=models.CASCADE, null=True, blank=True
    )
    job_titles_id = models.ForeignKey(
        "profiles.job_titles", on_delete=models.CASCADE, null=True, blank=True
    )
    country_id = models.ForeignKey(
        "profiles.country", on_delete=models.CASCADE, null=True, blank=True
    )
    city_id = models.ForeignKey(
        "profiles.city", on_delete=models.CASCADE, null=True, blank=True
    )

    token = models.OneToOneField(Token, on_delete=models.CASCADE, null=True, blank=True)

    # Fields
    bio = models.TextField(null=True, blank=True, default=None)

    about = models.TextField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to="upload/images/", null=True, blank=True)
    name = models.CharField(max_length=30, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    sub_domain = models.CharField(
        max_length=50, unique=True, null=True, blank=True, default=None
    )

    def __str__(self):
        return str(self.name)


class contact_info(models.Model):

    # Relationships

    profile_id = models.ForeignKey(
        "profiles.profiles", on_delete=models.CASCADE, related_name="profile_contacts"
    )

    # Fields
    name = models.CharField(max_length=30, null=True, blank=True)
    icon = models.ImageField(upload_to="upload/icons/", null=True, blank=True)
    url = models.CharField(null=True, blank=True, max_length=255)

    def __str__(self):
        return str(self.name)


class phone_numbers(models.Model):

    # Relationships
    profile_id = models.ForeignKey(
        "profiles.profiles", on_delete=models.CASCADE, related_name="profile_phones"
    )

    # Fields
    number = models.CharField(max_length=30, null=True, blank=True)
    name = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return str(self.number)


class Languages(models.Model):

    # Relationships
    profile_id = models.ForeignKey(
        "profiles.profiles", on_delete=models.CASCADE, related_name="profile_Languages"
    )

    # Fields
    name = models.CharField(max_length=30, null=True, blank=True)
    level = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return str(self.name)


class focus_points(models.Model):
    profile = models.ForeignKey(profiles, on_delete=models.CASCADE)
    point = models.CharField(max_length=150)

    def __str__(self):
        show = f"{str(self.profile)} {str(self.point)}"
        return str(show)
