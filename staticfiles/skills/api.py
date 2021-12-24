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
                description="user_id",
            ),
            "category": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="category that we will add the skills in it ",
            ),
            "skill": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="the skill name it self ",
            ),
            "project_number": openapi.Schema(
                type=openapi.TYPE_INTEGER,
                description="how many projects done in that skill",
            ),
            "sample_url": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="url to prove that the user have the skill already",
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
def add_skill(request):
    try:

        id = request.data.get("id")
        category = request.data.get("category")
        skill = request.data.get("skill")
        project_number = request.data.get("project_number")
        sample_url = request.data.get("sample_url")

        profile = profiles_model.profiles.objects.get(id=id)
        category = models.categories.objects.get(name=category)
        skill = models.skills.objects.get(name=skill)
        new_skill = models.user_skills.objects.create(
            projects_number=project_number,
            sample_url=sample_url,
            category_id=category,
            skills_id=skill,
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
                description="skill id",
            ),
            "category": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="category that we will add the skills in it ",
            ),
            "skill": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="the skill name it self ",
            ),
            "project_number": openapi.Schema(
                type=openapi.TYPE_INTEGER,
                description="how many projects done in that skill",
            ),
            "sample_url": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="url to prove that the user have the skill already",
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
def edit_skill(request):
    try:
        id = request.data.get("skill id")
        category = request.data.get("category")
        skill = request.data.get("skill")
        project_number = request.data.get("project_number")
        sample_url = request.data.get("sample_url")

        user_skill = models.user_skills.objects.get(id=id)
        category = models.categories.objects.get(name=category)
        skill = models.skills.objects.get(name=skill)

        def edit():
            if category != None:
                if category != "":
                    user_skill.category_id = category
            if skill != None:
                if skill != "":
                    user_skill.skills_id = skill
            if project_number != None:
                if project_number != "":
                    user_skill.projects_number = project_number
            if sample_url != None:
                if sample_url != "":
                    user_skill.sample_url = sample_url

        edit()
        user_skill.save()
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
                description="skill id",
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
def delete_skill(request):
    try:
        id = request.data.get("id")
        user_skill = models.user_skills.objects.get(id=id).delete()

        return Response({"status": successful})
    except:
        return Response({"status": unexpected})
