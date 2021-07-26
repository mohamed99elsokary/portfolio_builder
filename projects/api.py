from rest_framework.response import Response
from rest_framework.decorators import api_view
import profiles.models as profiles_model
from . import models
from . import serializers


@api_view(["POST"])
def create_project(request):
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
    return Response({"status": "successful"})


@api_view(["POST"])
def edit_project(request):
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
    return Response({"status": "successful"})


@api_view(["POST"])
def delete_project(request):
    id = request.data.get("id")

    project = models.projects.objects.get(id=id).delete()
    return Response({"status": "successful"})


@api_view(["POST"])
def add_bullet_point(request):
    project_id = request.data.get("project_id")
    point_text = request.data.get("point_text")

    project = models.projects.objects.get(id=project_id)

    bullet_point = models.bullet_points.objects.create(
        project_id=project, point_text=point_text
    )
    return Response({"status": "successful"})


@api_view(["POST"])
def edit_bullet_point(request):
    id = request.data.get("id")
    point_text = request.data.get("point_text")

    bullet_point = models.bullet_points.objects.get(id=id)

    def edit():
        if point_text != None:
            if point_text != "":
                bullet_point.point_text = point_text

    edit()
    bullet_point.save()
    return Response({"status": "successful"})


@api_view(["POST"])
def delete_bullet_point(request):
    id = request.data.get("id")

    bullet_point = models.bullet_points.objects.get(id=id).delete()
    return Response({"status": "successful"})


@api_view(["POST"])
def add_url(request):
    project_id = request.data.get("project_id")
    url = request.data.get("url")
    name = request.data.get("name")

    project = models.projects.objects.get(id=project_id)

    url = models.urls.objects.create(project_id=project, url=url, name=name)
    return Response({"status": "successful"})


@api_view(["POST"])
def edit_url(request):
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
    return Response({"status": "successful"})


@api_view(["POST"])
def delete_url(request):
    id = request.data.get("id")

    url = models.urls.objects.get(id=id).delete()
    return Response({"status": "successful"})
