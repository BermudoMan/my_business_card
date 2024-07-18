from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView
from .models import EducationWork, Publications, SkillCategory, ProjectsParticipate, Skills, DrawWorkExamples


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

class DrawWorkExamplesView(ListView):
    model = DrawWorkExamples
    template_name = 'title/drawing_examples.html'
    context_object_name = 'draw_examples'



class EducationWorkView(ListView):
    model = EducationWork
    template_name = 'title/education_work.html'


class ProjectsPart(ListView):
    model = ProjectsParticipate
    template_name = 'title/projects_part.html'


class Publ(ListView):
    model = Publications
    template_name = 'title/publications.html'


### ENG VERSION ###

def title_page_en(request):
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

    return render(request, 'title/index_en.html', context=data)


class SkillsViewEn(ListView):
    model = Skills
    template_name = 'title/skills.html'
    context_object_name = 'skills'

class SkillsViewProgEn(ListView):
    model = Skills
    template_name = 'title/skills_prog_en.html'
    context_object_name = 'skills'

class SkillsOtherEn(ListView):
    model = Skills
    template_name = 'title/other_skills_en.html'
    context_object_name = 'skills'

class SkillsQCEn(ListView):
    model = Skills
    template_name = 'title/qc_skills_en.html'
    context_object_name = 'skills'

class SkillsViewDrawEn(ListView):
    model = Skills
    template_name = 'title/drawing_skills_en.html'
    context_object_name = 'skills'



class EducationWorkViewEn(ListView):
    model = EducationWork
    template_name = 'title/education_work_en.html'


class ProjectsPartEn(ListView):
    model = ProjectsParticipate
    template_name = 'title/projects_part_en.html'


class PublEn(ListView):
    model = Publications
    template_name = 'title/publications_en.html'
