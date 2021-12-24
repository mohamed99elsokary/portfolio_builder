from rest_framework.response import Response
from rest_framework.decorators import api_view
import profiles.models as profiles_model
import work_experience.models as organizations_model
from . import models
from . import serializers
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from status import *

# ----------------------------------------------------------- work experience


@swagger_auto_schema(
    method="post",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "id": openapi.Schema(
                type=openapi.TYPE_INTEGER,
                description="user id",
            ),
            "start_date": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="start_date ",
            ),
            "end_date": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="end_date",
            ),
            "organization": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="organization",
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
def create_work_experience(request):
    try:
        id = request.data.get("id")
        start_date = request.data.get("start_date")
        end_date = request.data.get("end_date")
        organization = request.data.get("organization")

        profile = profiles_model.profiles.objects.get(id=id)
        organization = organizations_model.organizations.objects.get(name=organization)

        models.work_experience.objects.create(
            start_date=start_date,
            end_date=end_date,
            organizations_id=organization,
            profile_id=profile,
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
                description="work experience id",
            ),
            "start_date": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="start_date ",
            ),
            "end_date": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="end_date",
            ),
            "organization": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="organization",
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
def edit_work_experience(request):
    try:
        id = request.data.get("id")
        start_date = request.data.get("start_date")
        end_date = request.data.get("end_date")
        organization = request.data.get("organization")

        work_experience = models.work_experience.objects.get(id=id)

        def edit():
            if start_date != None:
                if start_date != "":
                    work_experience.start_date = start_date
            if end_date != None:
                if end_date != "":
                    work_experience.end_date = end_date
            if organization != None:
                if organization != "":

                    new_organization = organizations_model.organizations.objects.get(
                        name=organization
                    )
                    work_experience.organization = new_organization

        edit()
        work_experience.save()
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
                description="work experience id",
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
def delete_work_experience(request):
    try:
        id = request.data.get("id")

        work_experience = models.work_experience.objects.get(id=id).delete()

        return Response({"status": successful})
    except:
        return Response({"status": unexpected})


# ---------------------------------------------------------------- bullet points
@swagger_auto_schema(
    method="post",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "id": openapi.Schema(
                type=openapi.TYPE_INTEGER,
                description="work experience id",
            ),
            "point_text": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="bullet point text",
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
def add_bullet_points(request):
    try:
        work_experience_id = request.data.get("work_experience_id")
        point_text = request.data.get("point_text")
        work_experience = models.work_experience.objects.get(id=work_experience_id)

        bullet_point = models.bullet_points.objects.create(
            point_text=point_text, work_experience_id=work_experience
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
                description="bullet point id",
            ),
            "point_text": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="bullet point text",
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
def edit_bullet_points(request):
    try:
        id = request.data.get("id")
        point_text = request.data.get("point_text")

        bullet_point = models.bullet_points.objects.get(id=id)
        if point_text != None:
            if point_text != "":
                bullet_point.point_text = point_text
                bullet_point.save()
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
                description="bullet point id",
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
def delete_bullet_points(request):
    try:
        id = request.data.get("id")

        bullet_point = models.bullet_points.objects.get(id=id).delete()

        return Response({"status": successful})
    except:
        return Response({"status": unexpected})
