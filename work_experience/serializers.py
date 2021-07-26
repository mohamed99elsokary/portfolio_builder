from rest_framework import serializers

from . import models


class tagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.tags
        # fields = "__all__"
        exclude = ("organization_id",)


class organizationsSerializer(serializers.ModelSerializer):
    tags = tagsSerializer(many=True, source="organization_tags")

    class Meta:
        model = models.organizations
        fields = "__all__"


class bullet_pointsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.bullet_points
        # fields = "__all__"
        exclude = ("work_experience_id",)


class work_experienceSerializer(serializers.ModelSerializer):
    organization = organizationsSerializer(source="organizations_id")

    """organization = serializers.SlugRelatedField(
        queryset=models.organizations.objects.all(),
        slug_field="name",
        source="organizations_id",
    )"""
    bullet_points = bullet_pointsSerializer(many=True, source="work_bullet_points")

    class Meta:
        model = models.work_experience
        exclude = ("organizations_id", "profile_id")
        # fields = "__all__"
