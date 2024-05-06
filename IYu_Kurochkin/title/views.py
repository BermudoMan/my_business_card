from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView
from .models import EducationWork, Publications, SkillCategory, ProjectsParticipate, Skills


def title_page(request):
    edu = EducationWork.objects.all()
    skills = Skills.objects.all()
    publ = Publications.objects.all()
    proj = ProjectsParticipate.objects.all()
    data = {
        'skills': skills,
        'edu': edu,
        'publ': publ,
        'proj': proj,
    }

    return render(request, 'title/index.html', context=data)



class SkillsView(ListView):
    model = Skills
    template_name = 'title/skills.html'
    context_object_name = 'skills'

class SkillsViewProg(ListView):
    model = Skills
    template_name = 'title/skills_prog.html'
    context_object_name = 'skills'

class SkillsOther(ListView):
    model = Skills
    template_name = 'title/other_skills.html'
    context_object_name = 'skills'

class SkillsQC(ListView):
    model = Skills
    template_name = 'title/qc_skills.html'
    context_object_name = 'skills'

class SkillsViewDraw(ListView):
    model = Skills
    template_name = 'title/drawing_skills.html'
    context_object_name = 'skills'



class EducationWorkView(ListView):
    model = EducationWork
    template_name = 'title/education_work.html'


class ProjectsPart(ListView):
    model = ProjectsParticipate
    template_name = 'title/projects_part.html'


class Publ(ListView):
    model = Publications
    template_name = 'title/publications.html'