from rest_framework import serializers

from . import models


class bullet_pointsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.bullet_points
        fields = "__all__"
        # exclude = ("project_id",)


class urlsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.urls
        fields = "__all__"
        # exclude = ("project_id",)


class projectsSerializer(serializers.ModelSerializer):
    bullet_points = bullet_pointsSerializer(many=True, source="project_bullet_points")
    urls = urlsSerializer(many=True, source="project_urls")

    class Meta:

        model = models.projects
        fields = "__all__"
        # exclude = ("profile_id",)
