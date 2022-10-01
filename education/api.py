from rest_framework.response import Response
from rest_framework.decorators import api_view
import profiles.models as profiles_model
import work_experience.models as organizations_model
from . import models
from . import serializers

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from status import *


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
                description="start_date (ex: 2021-07-20)",
            ),
            "end_date": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="end date (ex: 2021-07-20)",
            ),
            "organization": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="organization name",
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
def create(request):
    try:
        id = request.data.get("id")
        start_date = request.data.get("start_date")
        end_date = request.data.get("end_date")
        organization = request.data.get("organization")

        profile = profiles_model.profiles.objects.get(id=id)
        organization = organizations_model.organizations.objects.get(name=organization)

        models.education.objects.create(
            start_date=start_date,
            end_date=end_date,
            organization_id=organization,
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
                description="education id",
            ),
            "start_date": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="start_date (ex: 2021-07-20)",
            ),
            "end_date": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="end date (ex: 2021-07-20)",
            ),
            "organization": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="organization name",
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
def edit(request):
    try:

        id = request.data.get("id")
        start_date = request.data.get("start_date")
        end_date = request.data.get("end_date")
        organization = request.data.get("organization")

        education = models.education.objects.get(id=id)

        def edit():
            if start_date not in [None, ""]:
                education.start_date = start_date
            if end_date not in [None, ""]:
                education.end_date = end_date
            if organization not in [None, ""]:
                new_organization = organizations_model.organizations.objects.get(
                    name=organization
                )

                education.organization = new_organization

        edit()
        education.save()
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
                description="education id",
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
def delete_education(request):
    try:
        id = request.data.get("id")
        education = models.education.objects.get(id=id).delete()
        return Response({"status": successful})
    except:
        return Response({"status": unexpected})


@swagger_auto_schema(
    method="post",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "education_id": openapi.Schema(
                type=openapi.TYPE_INTEGER,
                description="education id",
            ),
            "certificate_url": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="certificate_url ",
            ),
            "name": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="course name",
            ),
            "start_date": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="start_date",
            ),
            "end_date": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="end_date",
            ),
            "course_expected_time": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="el mford el course kan y5las fe ad eh",
            ),
            "is_highlighted": openapi.Schema(
                type=openapi.TYPE_BOOLEAN,
                description="is_highlighted",
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
def add_course(request):
    try:
        education_id = request.data.get("education_id")
        certificate_url = request.data.get("certificate_url")
        name = request.data.get("name")
        start_date = request.data.get("start_date")
        end_date = request.data.get("end_date")
        course_expected_time = request.data.get("course_expected_time")
        is_highlighted = request.data.get("is_highlighted")

        education = models.education.objects.get(id=education_id)
        course = models.courses.objects.create(
            certificate_url=certificate_url,
            name=name,
            start_date=start_date,
            end_date=end_date,
            course_expected_time=course_expected_time,
            is_highlighted=is_highlighted,
            education_id=education,
        )
        return Response({"status": successful})
    except:
        return Response({"status": unexpected})


@swagger_auto_schema(
    method="post",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "course_id": openapi.Schema(
                type=openapi.TYPE_INTEGER,
                description="course_id",
            ),
            "certificate_url": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="certificate_url ",
            ),
            "name": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="course name",
            ),
            "start_date": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="start_date",
            ),
            "end_date": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="end_date",
            ),
            "course_expected_time": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="el mford el course kan y5las fe ad eh",
            ),
            "is_highlighted": openapi.Schema(
                type=openapi.TYPE_BOOLEAN,
                description="is_highlighted",
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
def edit_course(request):
    try:
        course_id = request.data.get("course_id")
        certificate_url = request.data.get("certificate_url")
        name = request.data.get("name")
        start_date = request.data.get("start_date")
        end_date = request.data.get("end_date")
        course_expected_time = request.data.get("course_expected_time")
        is_highlighted = request.data.get("is_highlighted")

        course = models.courses.objects.get(id=course_id)

        def edit():
            if certificate_url not in [None, ""]:
                course.certificate_url = certificate_url
            if name not in [None, ""]:
                course.name = name
            if start_date not in [None, ""]:
                course.start_date = start_date
            if end_date not in [None, ""]:
                course.end_date = end_date
            if course_expected_time not in [None, ""]:
                course.course_expected_time = course_expected_time
            if is_highlighted not in [None, ""]:
                course.is_highlighted = is_highlighted

        edit()
        course.save()

        return Response({"status": successful})
    except:
        return Response({"status": unexpected})


@swagger_auto_schema(
    method="post",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "course_id": openapi.Schema(
                type=openapi.TYPE_INTEGER,
                description="course_id",
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
def delete_course(request):
    try:
        course_id = request.data.get("course_id")
        course = models.courses.objects.get(id=course_id).delete()
        return Response({"status": successful})
    except:
        return Response({"status": unexpected})
