from rest_framework import serializers

from . import models


class hyperlinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.hyperlinks
        # fields = "__all__"
        exclude = ("achievement_id", "award_id")


class achievementSerializer(serializers.ModelSerializer):
    hyperlinks = hyperlinksSerializer(many=True, source="achievement_hyperlinks")

    class Meta:
        model = models.achievement
        # fields = "__all__"
        exclude = ("profile_id",)


class awardSerializer(serializers.ModelSerializer):
    hyperlinks = hyperlinksSerializer(many=True, source="award_hyperlinks")

    class Meta:
        model = models.achievement
        # fields = "__all__"
        exclude = ("profile_id",)
