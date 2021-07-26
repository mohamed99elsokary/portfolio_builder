from rest_framework import serializers

from . import models


class skillsSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        read_only=True, slug_field="name", source="category_id"
    )

    class Meta:
        model = models.skills
        fields = "__all__"
        # exclude = ("category_id",)


class categoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.categories
        fields = "__all__"
        # exclude = ("id",)


class user_skillsSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        queryset=models.categories.objects.all(),
        slug_field="name",
        source="category_id",
    )
    skill = serializers.SlugRelatedField(
        queryset=models.skills.objects.all(), slug_field="name", source="skills_id"
    )

    class Meta:
        model = models.user_skills
        # fields = "__all__"
        exclude = ("profile_id", "skills_id", "category_id")
