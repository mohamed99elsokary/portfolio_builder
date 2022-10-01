from django.shortcuts import redirect, render
from . import models
from skills import models as skills_models
from rest_framework.authtoken.models import Token
from education import models as education_models
from projects import models as project_models
from work_experience import models as work_experience_models


def data(domain):
    domain = domain.split(".")[0]
    user = models.profiles.objects.get(sub_domain=domain)
    languages = models.Languages.objects.filter(profile_id=user)
    contact_info = models.contact_info.objects.filter(profile_id=user)
    skills = skills_models.user_skills.objects.filter(profile_id=user)
    phone_numbers = models.phone_numbers.objects.filter(profile_id=user)
    educations = (
        education_models.education.objects.filter(profile_id=user)
        .order_by("start_date")
        .reverse()
    )
    courses = (
        education_models.courses.objects.filter(profile_id=user)
        .order_by("start_date")
        .reverse()
    )
    projects = project_models.projects.objects.filter(profile_id=user)
    total_projects = projects.count()
    focus_points = models.focus_points.objects.filter(profile=user)
    work_experience = (
        work_experience_models.work_experience.objects.filter(profile_id=user)
        .order_by("start_date")
        .reverse()
    )
    for contact in contact_info:
        if contact.name == "email":
            email = contact.url

    return {
        "user": user,
        "email": email,
        "languages": languages,
        "skills": skills,
        "contact_info": contact_info,
        "phone_numbers": phone_numbers,
        "phone_number": phone_numbers[0],
        "courses": courses,
        "educations": educations,
        "projects": projects,
        "focus_points": focus_points,
        "work_experience": work_experience,
        "total_projects": total_projects,
    }


def portfolio(request):
    domain = request.META.get("HTTP_HOST")
    return render(request, "portfolio.html", context=data(domain))


def cv(request):
    domain = request.META.get("HTTP_HOST")
    return render(request, "cv.html", context=data(domain))
