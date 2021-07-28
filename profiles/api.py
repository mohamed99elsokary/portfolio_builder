from rest_framework import viewsets, permissions
from rest_framework.response import Response
from django.contrib.auth.models import User

from rest_framework.decorators import api_view

from .serializers import *
from . import models
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from status import *


# ----------------------------------------------------------- user
@swagger_auto_schema(
    method="post",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "email": openapi.Schema(
                type=openapi.TYPE_INTEGER,
                description="email (unique)",
            ),
            "password": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="password",
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
        email = request.data.get("email")
        password = request.data.get("password")
        user = User.objects.create_user(email=email, username=email, password=password)
        profile = models.profiles.objects.create(id=user.id, user=user)
        # data = userSerializer(user).data
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
                description="user id",
            ),
            "birth_date": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="birth_date",
            ),
            "about": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="about",
            ),
            "image": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="image",
            ),
            "name": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="name",
            ),
            "country": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="country",
            ),
            "city": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="city",
            ),
            "field": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="field",
            ),
            "job_title": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="job_title",
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
        birth_date = request.data.get("birth_date")
        about = request.data.get("about")
        image = request.data.get("image")
        name = request.data.get("name")
        country = request.data.get("country")
        city = request.data.get("city")
        field = request.data.get("field")
        job_title = request.data.get("job_title")

        profile = models.profiles.objects.get(id=id)

        def edit():
            if birth_date != None:
                if birth_date != "":
                    profile.birth_date = birth_date
            if about != None:
                if about != "":
                    profile.about = about
            if image != None:
                if image != "":
                    profile.image = image
            if name != None:
                if name != "":
                    profile.name = name
            if country != None:
                if country != "":
                    new_country = models.country.objects.get(country=country)
                    profile.country_id = new_country
            if city != None:
                if city != "":
                    new_city = models.city.objects.get(city=city)
                    profile.city_id = new_city
            if field != None:
                if field != "":
                    new_field = models.fields.objects.get(field=field)
                    profile.field_id = new_field
            if job_title != None:
                if job_title != "":
                    new_job_title = models.job_titles.objects.get(job_title=job_title)
                    profile.job_titles_id = new_job_title
            profile.save()

        edit()
        data = profilesSerializer(profile).data
        return Response({"data": data, "status": successful})
    except:
        return Response({"data": data, "status": unexpected})


@swagger_auto_schema(
    method="post",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "id": openapi.Schema(
                type=openapi.TYPE_INTEGER,
                description="user id",
            ),
        },
    ),
    responses={
        "200": openapi.Response(
            description="created successfully",
            examples={
                "application/json": {
                    "data": {
                        "id": 22,
                        "education": [
                            {
                                "id": 7,
                                "courses": [
                                    {
                                        "id": 3,
                                        "certificate_url": "www.google.come",
                                        "name": "django rest",
                                        "start_date": "2021-07-20",
                                        "course_expected_time": "100 days",
                                        "end_date": "2021-07-20",
                                        "is_highlighted": True,
                                        "certificate_file": None,
                                        "education_id": 7,
                                    },
                                    {
                                        "id": 4,
                                        "certificate_url": "www.google.come",
                                        "name": "Flask",
                                        "start_date": "2021-07-20",
                                        "course_expected_time": "100 days",
                                        "end_date": "2021-07-20",
                                        "is_highlighted": False,
                                        "certificate_file": None,
                                        "education_id": 7,
                                    },
                                ],
                                "organization": {
                                    "id": 1,
                                    "tags": [
                                        {"id": 1, "tag": "ud"},
                                        {"id": 2, "tag": "udaaaa"},
                                    ],
                                    "icon": None,
                                    "icon_url": None,
                                    "name": "udacity",
                                },
                                "end_date": "2021-12-20",
                                "start_date": "2021-07-01",
                                "profile_id": 22,
                                "organization_id": 1,
                            }
                        ],
                        "work_experience": [
                            {
                                "id": 4,
                                "organization": {
                                    "id": 1,
                                    "tags": [
                                        {"id": 1, "tag": "ud"},
                                        {"id": 2, "tag": "udaaaa"},
                                    ],
                                    "icon": None,
                                    "icon_url": None,
                                    "name": "udacity",
                                },
                                "bullet_points": [
                                    {"id": 4, "point_text": "point_text"}
                                ],
                                "end_date": "2021-07-20",
                                "start_date": "2021-07-20",
                            }
                        ],
                        "projects": [
                            {
                                "id": 3,
                                "bullet_points": [
                                    {
                                        "id": 2,
                                        "point_text": "point_text",
                                        "project_id": 3,
                                    }
                                ],
                                "urls": [
                                    {
                                        "id": 3,
                                        "url": "www.google.com",
                                        "name": "name",
                                        "project_id": 3,
                                    }
                                ],
                                "descreption": "descreption",
                                "icon": None,
                                "start_date": "2021-07-20",
                                "name": "name",
                                "icon_url": "www.google.com",
                                "end_date": None,
                                "profile_id": 22,
                            }
                        ],
                        "awards": [
                            {
                                "id": 4,
                                "hyperlinks": [
                                    {
                                        "id": 6,
                                        "url": "www.google.com",
                                        "start_index": 2,
                                        "end_index": 15,
                                    }
                                ],
                                "text": "asadasdasd",
                                "order": 2,
                            },
                            {
                                "id": 5,
                                "hyperlinks": [],
                                "text": "asadasdasd",
                                "order": 2,
                            },
                        ],
                        "achievements": [
                            {
                                "id": 4,
                                "hyperlinks": [
                                    {
                                        "id": 7,
                                        "url": "www.google.com",
                                        "start_index": 2,
                                        "end_index": 15,
                                    }
                                ],
                                "text": "asadasdasd",
                                "order": 2,
                            }
                        ],
                        "skills": [
                            {
                                "id": 2,
                                "category": "backend",
                                "skill": "python",
                                "projects_number": 5,
                                "sample_url": "",
                            },
                            {
                                "id": 4,
                                "category": "backend",
                                "skill": "django",
                                "projects_number": 10,
                                "sample_url": "string",
                            },
                        ],
                        "contact_info": [
                            {
                                "id": 2,
                                "name": "facebook",
                                "icon": None,
                                "url": "www.facebook.com",
                            }
                        ],
                        "phone_numbers": [
                            {"id": 1, "number": "+201111155856", "name": "English"}
                        ],
                        "Languages": [{"id": 1, "name": "English", "level": 1}],
                        "country": "Egypt",
                        "city": "Cairo",
                        "job_title": "django developer",
                        "field": "developer",
                        "email": "jzzxcozxckcasdzsdaasdsdzccasdc@gmail.com",
                        "about": "any about for now ",
                        "image": None,
                        "name": "joker",
                        "birth_date": "2021-07-20",
                    },
                    "status": 1000,
                }
            },
        ),
        "201": openapi.Response(
            description="something went wrong",
            examples={"application/json": {"status": 2000}},
        ),
    },
)
@api_view(["POST", "GET"])
def get(request, id):
    try:
        # id = request.data.get("id")
        user = models.profiles.objects.get(id=id)
        data = profilesSerializer(user).data
        return Response({"data": data, "status": successful})
    except:
        return Response({"data": data, "status": unexpected})


@swagger_auto_schema(
    method="post",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "id": openapi.Schema(
                type=openapi.TYPE_INTEGER,
                description="user id",
            ),
        },
    ),
    responses={
        "200": openapi.Response(
            description="created successfully",
            examples={
                "application/json": {
                    "data": {
                        "id": 22,
                        "education": [
                            {
                                "id": 7,
                                "courses": [
                                    {
                                        "id": 3,
                                        "certificate_url": "www.google.come",
                                        "name": "django rest",
                                        "start_date": "2021-07-20",
                                        "course_expected_time": "100 days",
                                        "end_date": "2021-07-20",
                                        "is_highlighted": True,
                                        "certificate_file": None,
                                        "education_id": 7,
                                    },
                                    {
                                        "id": 4,
                                        "certificate_url": "www.google.come",
                                        "name": "Flask",
                                        "start_date": "2021-07-20",
                                        "course_expected_time": "100 days",
                                        "end_date": "2021-07-20",
                                        "is_highlighted": False,
                                        "certificate_file": None,
                                        "education_id": 7,
                                    },
                                ],
                                "organization": {
                                    "id": 1,
                                    "tags": [
                                        {"id": 1, "tag": "ud"},
                                        {"id": 2, "tag": "udaaaa"},
                                    ],
                                    "icon": None,
                                    "icon_url": None,
                                    "name": "udacity",
                                },
                                "end_date": "2021-12-20",
                                "start_date": "2021-07-01",
                                "profile_id": 22,
                                "organization_id": 1,
                            }
                        ],
                        "work_experience": [
                            {
                                "id": 4,
                                "organization": {
                                    "id": 1,
                                    "tags": [
                                        {"id": 1, "tag": "ud"},
                                        {"id": 2, "tag": "udaaaa"},
                                    ],
                                    "icon": None,
                                    "icon_url": None,
                                    "name": "udacity",
                                },
                                "bullet_points": [
                                    {"id": 4, "point_text": "point_text"}
                                ],
                                "end_date": "2021-07-20",
                                "start_date": "2021-07-20",
                            }
                        ],
                        "projects": [
                            {
                                "id": 3,
                                "bullet_points": [
                                    {
                                        "id": 2,
                                        "point_text": "point_text",
                                        "project_id": 3,
                                    }
                                ],
                                "urls": [
                                    {
                                        "id": 3,
                                        "url": "www.google.com",
                                        "name": "name",
                                        "project_id": 3,
                                    }
                                ],
                                "descreption": "descreption",
                                "icon": None,
                                "start_date": "2021-07-20",
                                "name": "name",
                                "icon_url": "www.google.com",
                                "end_date": None,
                                "profile_id": 22,
                            }
                        ],
                        "awards": [
                            {
                                "id": 4,
                                "hyperlinks": [
                                    {
                                        "id": 6,
                                        "url": "www.google.com",
                                        "start_index": 2,
                                        "end_index": 15,
                                    }
                                ],
                                "text": "asadasdasd",
                                "order": 2,
                            },
                            {
                                "id": 5,
                                "hyperlinks": [],
                                "text": "asadasdasd",
                                "order": 2,
                            },
                        ],
                        "achievements": [
                            {
                                "id": 4,
                                "hyperlinks": [
                                    {
                                        "id": 7,
                                        "url": "www.google.com",
                                        "start_index": 2,
                                        "end_index": 15,
                                    }
                                ],
                                "text": "asadasdasd",
                                "order": 2,
                            }
                        ],
                        "skills": [
                            {
                                "id": 2,
                                "category": "backend",
                                "skill": "python",
                                "projects_number": 5,
                                "sample_url": "",
                            },
                            {
                                "id": 4,
                                "category": "backend",
                                "skill": "django",
                                "projects_number": 10,
                                "sample_url": "string",
                            },
                        ],
                        "contact_info": [
                            {
                                "id": 2,
                                "name": "facebook",
                                "icon": None,
                                "url": "www.facebook.com",
                            }
                        ],
                        "phone_numbers": [
                            {"id": 1, "number": "+201111155856", "name": "English"}
                        ],
                        "Languages": [{"id": 1, "name": "English", "level": 1}],
                        "country": "Egypt",
                        "city": "Cairo",
                        "job_title": "django developer",
                        "field": "developer",
                        "email": "jzzxcozxckcasdzsdaasdsdzccasdc@gmail.com",
                        "about": "any about for now ",
                        "image": None,
                        "name": "joker",
                        "birth_date": "2021-07-20",
                    },
                    "status": 1000,
                }
            },
        ),
        "201": openapi.Response(
            description="something went wrong",
            examples={"application/json": {"status": 2000}},
        ),
    },
)
@api_view(["GET"])
def get_all(request):
    try:
        user = models.profiles.objects.all()
        data = profilesSerializer(user, many=True).data
        return Response({"data": data, "status": successful})
    except:
        return Response({"data": data, "status": unexpected})


# ---------------------------------------------------------------- contact_info
@swagger_auto_schema(
    method="post",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "id": openapi.Schema(
                type=openapi.TYPE_INTEGER,
                description="user id",
            ),
            "name": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="platform name",
            ),
            "url": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="contact url",
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
def create_contact_info(request):
    try:
        id = request.data.get("id")
        name = request.data.get("name")
        url = request.data.get("url")

        profile = models.profiles.objects.get(id=id)
        contact_info = models.contact_info.objects.create(
            name=name, url=url, profile_id=profile
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
                description="contact info id",
            ),
            "name": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="platform name",
            ),
            "url": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="contact url",
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
def edit_contact_info(request):
    try:
        id = request.data.get("id")
        name = request.data.get("name")
        url = request.data.get("url")

        contact_info = models.contact_info.objects.get(id=id)

        def edit():
            if name != None:
                if name != "":
                    contact_info.name = name
            if url != None:
                if url != "":
                    contact_info.url = url

        edit()
        contact_info.save()
        return Response({"status": successful})
    except:
        return Response({"status": successful})


@swagger_auto_schema(
    method="post",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "id": openapi.Schema(
                type=openapi.TYPE_INTEGER,
                description="contact info id",
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
def delete_contact_info(request):
    try:
        id = request.data.get("id")

        contact_info = models.contact_info.objects.get(id=id).delete()

        return Response({"status": successful})
    except:
        return Response({"status": unexpected})


# ---------------------------------------------------------------- langauges
@swagger_auto_schema(
    method="post",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "id": openapi.Schema(
                type=openapi.TYPE_INTEGER,
                description="user id",
            ),
            "name": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="language name",
            ),
            "level": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="language level",
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
def add_language(request):
    try:
        id = request.data.get("id")
        name = request.data.get("name")
        level = request.data.get("level")

        profile = models.profiles.objects.get(id=id)
        language = models.Languages.objects.create(
            name=name, profile_id=profile, level=level
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
                description="language id",
            ),
            "name": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="language name",
            ),
            "level": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="language level",
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
def edit_language(request):
    try:
        id = request.data.get("id")
        name = request.data.get("name")
        level = request.data.get("level")

        language = models.Languages.objects.get(id=id)

        def edit():
            if name != None:
                if name != "":
                    language.name = name
            if level != None:
                if level != "":
                    language.level = level

        edit()
        language.save()
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
                description="language id",
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
def delete_language(request):
    try:
        id = request.data.get("id")

        language = models.Languages.objects.get(id=id).delete()

        return Response({"status": successful})
    except:
        return Response({"status": unexpected})


# ---------------------------------------------------------------- phone_numbers
@swagger_auto_schema(
    method="post",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "id": openapi.Schema(
                type=openapi.TYPE_INTEGER,
                description="user id",
            ),
            "name": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="phone name",
            ),
            "number": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="the number",
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
def add_phone_number(request):
    try:
        id = request.data.get("id")
        name = request.data.get("name")
        number = request.data.get("number")

        profile = models.profiles.objects.get(id=id)
        phone_number = models.phone_numbers.objects.create(
            name=name, profile_id=profile, number=number
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
                description="phone id",
            ),
            "name": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="phone name",
            ),
            "number": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="the number",
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
def edit_phone_number(request):
    try:
        id = request.data.get("id")
        name = request.data.get("name")
        number = request.data.get("number")

        phone_number = models.phone_numbers.objects.get(id=id)

        def edit():
            if name != None:
                if name != "":
                    phone_number.name = name
            if number != None:
                if number != "":
                    phone_number.number = number

        edit()
        phone_number.save()
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
                description="phone id",
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
def delete_phone_number(request):
    try:
        id = request.data.get("id")

        phone_number = models.phone_numbers.objects.get(id=id).delete()

        return Response({"status": successful})
    except:
        return Response({"status": unexpected})
