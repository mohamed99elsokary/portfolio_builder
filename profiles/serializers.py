from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer

import skills.serializers as skills_serializers
import skills.models as skills_models

import achievement.serializers as achievements_serializers
import achievement.models as achievements_models
import projects.serializers as projects_serializers
import projects.models as projects_models
import work_experience.serializers as work_experience_serializers
import work_experience.models as work_experience_models
import education.serializers as education_serializers
import education.models as education_models


from . import models
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


# from skills import serializers
class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class citySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.city
        fields = "__all__"


class phone_numbersSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.phone_numbers
        # fields = "__all__"
        exclude = ("profile_id",)


class LanguagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Languages
        # fields = "__all__"
        exclude = ("profile_id",)


class job_titlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.job_titles
        fields = "__all__"


class contact_infoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.contact_info
        # fields = "__all__"
        exclude = ("profile_id",)


class fieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.fields
        fields = "__all__"


class countrySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.country
        fields = "__all__"


class profilesSerializer(serializers.ModelSerializer):
    education = education_serializers.educationSerializer(
        many=True, source="profile_education"
    )
    work_experience = work_experience_serializers.work_experienceSerializer(
        many=True, source="profile_work_experience"
    )
    projects = projects_serializers.projectsSerializer(
        many=True, source="profiles_projects"
    )
    awards = achievements_serializers.awardSerializer(
        many=True, source="profile_awards"
    )
    achievements = achievements_serializers.achievementSerializer(
        many=True, source="profile_achievements"
    )

    skills = skills_serializers.user_skillsSerializer(
        many=True, source="profile_skills"
    )
    contact_info = contact_infoSerializer(many=True, source="profile_contacts")
    # phone_numbers = phone_numbersSerializer(many=True, source="profile_phones")

    Languages = LanguagesSerializer(many=True, source="profile_Languages")
    country = serializers.SlugRelatedField(
        queryset=models.country.objects.all(), slug_field="country", source="country_id"
    )
    city = serializers.SlugRelatedField(
        queryset=models.city.objects.all(), slug_field="city", source="city_id"
    )
    job_title = serializers.SlugRelatedField(
        queryset=models.job_titles.objects.all(),
        slug_field="job_title",
        source="job_titles_id",
    )
    field = serializers.SlugRelatedField(
        queryset=models.fields.objects.all(), slug_field="field", source="field_id"
    )

    email = serializers.SlugRelatedField(
        read_only=True, slug_field="email", source="user"
    )

    class Meta:
        model = models.profiles
        exclude = ("country_id", "id", "city_id", "field_id", "job_titles_id", "user")


class loginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ["key"]
