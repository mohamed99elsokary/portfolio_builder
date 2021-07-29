import re
from rest_framework.response import Response
from rest_framework.decorators import api_view
import profiles.models as profiles_model
from . import models
from . import serializers
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from status import *

# ----------------------------------------------------------- projects
@swagger_auto_schema(
    method="post",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "id": openapi.Schema(
                type=openapi.TYPE_INTEGER,
                description="user id",
            ),
            "descreption": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="project descreption",
            ),
            "start_date": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="start date",
            ),
            "end_date": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="end date",
            ),
            "name": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="project name",
            ),
            "icon_url": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="icon url",
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
def create_project(request):
    try:
        id = request.data.get("id")
        descreption = request.data.get("descreption")
        start_date = request.data.get("start_date")
        end_date = request.data.get("end_date")
        name = request.data.get("name")
        icon_url = request.data.get("icon_url")

        profile = profiles_model.profiles.objects.get(id=id)
        project = models.projects.objects.create(
            descreption=descreption,
            start_date=start_date,
            end_date=end_date,
            name=name,
            icon_url=icon_url,
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
                description="project id",
            ),
            "descreption": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="project descreption",
            ),
            "start_date": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="start date",
            ),
            "end_date": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="end date",
            ),
            "name": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="project name",
            ),
            "icon_url": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="icon url",
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
def edit_project(request):
    try:
        id = request.data.get("id")
        descreption = request.data.get("descreption")
        start_date = request.data.get("start_date")
        end_date = request.data.get("end")
        name = request.data.get("name")
        icon_url = request.data.get("icon_url")

        project = models.projects.objects.get(id=id)

        def edit():
            if descreption != None:
                if descreption != "":
                    project.descreption = descreption
            if start_date != None:
                if start_date != "":
                    project.start_date = start_date
            if end_date != None:
                if end_date != "":
                    project.end_date = end_date
            if name != None:
                if name != "":
                    project.name = name
            if icon_url != None:
                if icon_url != "":
                    project.icon_url = icon_url

        edit()
        project.save()
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
                description="project id",
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
def delete_project(request):
    try:
        id = request.data.get("id")

        project = models.projects.objects.get(id=id).delete()
        return Response({"status": successful})
    except:
        return Response({"status": unexpected})


# ----------------------------------------------------------------bullet points
@swagger_auto_schema(
    method="post",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "id": openapi.Schema(
                type=openapi.TYPE_INTEGER,
                description="project id",
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
def add_bullet_point(request):
    try:
        id = request.data.get("id")
        point_text = request.data.get("point_text")

        project = models.projects.objects.get(id=id)

        bullet_point = models.bullet_points.objects.create(
            project_id=project, point_text=point_text
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
def edit_bullet_point(request):
    try:
        id = request.data.get("id")
        point_text = request.data.get("point_text")

        bullet_point = models.bullet_points.objects.get(id=id)

        def edit():
            if point_text != None:
                if point_text != "":
                    bullet_point.point_text = point_text

        edit()
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
def delete_bullet_point(request):
    try:
        id = request.data.get("id")

        bullet_point = models.bullet_points.objects.get(id=id).delete()
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
                description="project id",
            ),
            "name": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="url name",
            ),
            "url": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="url",
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
def add_url(request):
    try:
        project_id = request.data.get("project_id")
        url = request.data.get("url")
        name = request.data.get("name")

        project = models.projects.objects.get(id=project_id)

        url = models.urls.objects.create(project_id=project, url=url, name=name)
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
                description="url id",
            ),
            "name": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="url name",
            ),
            "url": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="url",
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
def edit_url(request):
    try:
        id = request.data.get("id")
        url = request.data.get("url")
        name = request.data.get("name")

        old_url = models.urls.objects.get(id=id)

        def edit():
            if url != None:
                if url != "":
                    old_url.url = url
            if name != None:
                if name != "":
                    old_url.name = name

        edit()
        old_url.save()
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
                description="url id",
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
def delete_url(request):
    try:
        id = request.data.get("id")

        url = models.urls.objects.get(id=id).delete()
        return Response({"status": successful})
    except:
        return Response({"status": unexpected})
