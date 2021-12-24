from rest_framework import fields, serializers
import work_experience.models as work_experience_models
from work_experience.serializers import *

from . import models


class coursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.courses
        fields = "__all__"


class educationSerializer(serializers.ModelSerializer):
    courses = coursesSerializer(many=True, source="education_courses")
    organization = organizationsSerializer(source="organization_id")

    class Meta:
        model = models.education
        fields = "__all__"
