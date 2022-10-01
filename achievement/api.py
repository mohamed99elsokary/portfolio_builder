from rest_framework.response import Response
from rest_framework.decorators import api_view
import profiles.models as profiles_model
from . import models
from . import serializers
from status import *
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

# ----------------------------------------------------------------awards


@swagger_auto_schema(
    method="post",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "id": openapi.Schema(
                type=openapi.TYPE_INTEGER,
                description="user id ",
            ),
            "text": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="award it self",
            ),
            "order": openapi.Schema(
                type=openapi.TYPE_STRING, description="htzhr rkm kam"
            ),
        },
    ),
    responses={
        "200": openapi.Response(
            description="created successfully",
            examples={"application/json": {"status": 1000}},
        ),
        "201": openapi.Response(
            description="something went wrong",
            examples={"application/json": {"status": 2000}},
        ),
    },
)
@api_view(["POST"])
def create_awards(request):
    try:
        id = request.data.get("id")
        text = request.data.get("text")
        order = request.data.get("order")

        profile = profiles_model.profiles.objects.get(id=id)
        award = models.award.objects.create(profile_id=profile, text=text, order=order)
        return Response({"status": successful})
    except:
        return Response({"status": unexpected})


@swagger_auto_schema(
    method="post",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "id": openapi.Schema(
                type=openapi.TYPE_INTEGER,
                description="award id ",
            ),
            "text": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="award it self",
            ),
            "order": openapi.Schema(
                type=openapi.TYPE_STRING, description="htzhr rkm kam"
            ),
        },
    ),
    responses={
        "200": openapi.Response(
            description="created successfully",
            examples={"application/json": {"status": 1000}},
        ),
        "201": openapi.Response(
            description="something went wrong",
            examples={"application/json": {"status": 2000}},
        ),
    },
)
@api_view(["POST"])
def edit_awards(request):
    try:
        id = request.data.get("id")
        text = request.data.get("text")
        order = request.data.get("order")

        award = models.award.objects.get(id=id)

        def edit():
            if text not in [None, ""]:
                award.text = text
            if order not in [None, ""]:
                award.order = order

        edit()
        award.save()
        return Response({"status": successful})
    except:
        return Response({"status": unexpected})


@swagger_auto_schema(
    method="post",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "id": openapi.Schema(
                type=openapi.TYPE_INTEGER,
                description="award id ",
            ),
        },
    ),
    responses={
        "200": openapi.Response(
            description="created successfully",
            examples={"application/json": {"status": 1000}},
        ),
        "201": openapi.Response(
            description="something went wrong",
            examples={"application/json": {"status": 2000}},
        ),
    },
)
@api_view(["POST"])
def delete_awards(request):
    try:
        id = request.data.get("id")

        award = models.award.objects.get(id=id).delete()
        return Response({"status": successful})
    except:
        return Response({"status": unexpected})


# ----------------------------------------------------------------achievements
@swagger_auto_schema(
    method="post",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "id": openapi.Schema(
                type=openapi.TYPE_INTEGER,
                description="user id ",
            ),
            "text": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="achievement it self ",
            ),
            "order": openapi.Schema(
                type=openapi.TYPE_INTEGER,
                description="htzhr rkm kam",
            ),
        },
    ),
    responses={
        "200": openapi.Response(
            description="created successfully",
            examples={"application/json": {"status": 1000}},
        ),
        "201": openapi.Response(
            description="something went wrong",
            examples={"application/json": {"status": 2000}},
        ),
    },
)
@api_view(["POST"])
def create_achievements(request):
    try:
        id = request.data.get("id")
        text = request.data.get("text")
        order = request.data.get("order")

        profile = profiles_model.profiles.objects.get(id=id)
        achievement = models.achievement.objects.create(
            profile_id=profile, text=text, order=order
        )
        return Response({"status": successful})
    except:
        return Response({"status": unexpected})


@swagger_auto_schema(
    method="post",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "id": openapi.Schema(
                type=openapi.TYPE_INTEGER,
                description="achievement id ",
            ),
            "text": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="achievement it self ",
            ),
            "order": openapi.Schema(
                type=openapi.TYPE_INTEGER,
                description="htzhr rkm kam",
            ),
        },
    ),
    responses={
        "200": openapi.Response(
            description="created successfully",
            examples={"application/json": {"status": 1000}},
        ),
        "201": openapi.Response(
            description="something went wrong",
            examples={"application/json": {"status": 2000}},
        ),
    },
)
@api_view(["POST"])
def edit_achievements(request):
    try:
        id = request.data.get("id")
        text = request.data.get("text")
        order = request.data.get("order")

        achievement = models.achievement.objects.get(id=id)

        def edit():
            if text not in [None, ""]:
                achievement.text = text
            if order not in [None, ""]:
                achievement.order = order

        edit()
        achievement.save()
        return Response({"status": successful})
    except:
        return Response({"status": unexpected})


@swagger_auto_schema(
    method="post",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "id": openapi.Schema(
                type=openapi.TYPE_INTEGER,
                description="achievement id ",
            ),
        },
    ),
    responses={
        "200": openapi.Response(
            description="created successfully",
            examples={"application/json": {"status": 1000}},
        ),
        "201": openapi.Response(
            description="something went wrong",
            examples={"application/json": {"status": 2000}},
        ),
    },
)
@api_view(["POST"])
def delete_achievements(request):
    try:
        id = request.data.get("id")

        achievement = models.achievement.objects.get(id=id).delete()
        return Response({"status": successful})
    except:
        return Response({"status": unexpected})


# ----------------------------------------------------------------hyperlinks
@swagger_auto_schema(
    method="post",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "achievement_id": openapi.Schema(
                type=openapi.TYPE_INTEGER,
                description="achievement id (u have to send ony one award or one achievement)",
            ),
            "award_id": openapi.Schema(
                type=openapi.TYPE_INTEGER,
                description="award id (u have to send ony one award or one achievement)",
            ),
            "url": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="url for the hyperlink",
            ),
            "start_index": openapi.Schema(
                type=openapi.TYPE_INTEGER,
                description="start_index",
            ),
            "end_index": openapi.Schema(
                type=openapi.TYPE_INTEGER,
                description="end_index",
            ),
        },
    ),
    responses={
        "200": openapi.Response(
            description="created successfully",
            examples={"application/json": {"status": 1000}},
        ),
        "201": openapi.Response(
            description="something went wrong",
            examples={"application/json": {"status": 2000}},
        ),
    },
)
@api_view(["POST"])
def create_hyperlinks(request):
    try:
        achievement_id = request.data.get("achievement_id")
        award_id = request.data.get("award_id")
        url = request.data.get("url")
        start_index = request.data.get("start_index")
        end_index = request.data.get("end_index")

        if achievement_id is None:
            award = models.award.objects.get(id=award_id)
            achievement = None
        elif achievement_id != "":
            achievement = models.achievement.objects.get(id=achievement_id)
            award = None
        hyperlink = models.hyperlinks.objects.create(
            url=url,
            start_index=start_index,
            end_index=end_index,
            award_id=award,
            achievement_id=achievement,
        )
        return Response({"status": successful})
    except:
        return Response({"status": unexpected})


@swagger_auto_schema(
    method="post",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "id": openapi.Schema(
                type=openapi.TYPE_INTEGER,
                description="hyper link it self",
            ),
            "url": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="url for the hyperlink",
            ),
            "start_index": openapi.Schema(
                type=openapi.TYPE_INTEGER,
                description="start_index",
            ),
            "end_index": openapi.Schema(
                type=openapi.TYPE_INTEGER,
                description="end_index",
            ),
        },
    ),
    responses={
        "200": openapi.Response(
            description="created successfully",
            examples={"application/json": {"status": 1000}},
        ),
        "201": openapi.Response(
            description="something went wrong",
            examples={"application/json": {"status": 2000}},
        ),
    },
)
@api_view(["POST"])
def edit_hyperlinks(request):
    try:
        id = request.data.get("id")
        url = request.data.get("url")
        start_index = request.data.get("start_index")
        end_index = request.data.get("end_index")
        hyperlink = models.hyperlinks.objects.get(id=id)

        def edit():
            if url not in [None, ""]:
                hyperlink.url = url
            if start_index not in [None, ""]:
                hyperlink.start_index = start_index
            if end_index not in [None, ""]:
                hyperlink.end_index = end_index

        edit()
        hyperlink.save()
        return Response({"status": successful})
    except:
        return Response({"status": unexpected})


@swagger_auto_schema(
    method="post",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "id": openapi.Schema(
                type=openapi.TYPE_INTEGER,
                description="hyper link it self",
            ),
        },
    ),
    responses={
        "200": openapi.Response(
            description="created successfully",
            examples={"application/json": {"status": 1000}},
        ),
        "201": openapi.Response(
            description="something went wrong",
            examples={"application/json": {"status": 2000}},
        ),
    },
)
@api_view(["POST"])
def delete_hyperlinks(request):
    try:

        id = request.data.get("id")
        hyperlink = models.hyperlinks.objects.get(id=id).delete()
        return Response({"status": successful})
    except:
        return Response({"status": unexpected})
