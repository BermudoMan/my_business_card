from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView
from .models import EducationWork, Publications, SkillCategory, ProjectsParticipate, Skills


class TitlePage(TemplateView):
    template_name = 'title/index.html'


class SkillsView(ListView):
    model = Skills
    template_name = 'title/skills.html'


class EducationWorkView(ListView):
    model = EducationWork
    template_name = 'title/education_work.html'


class ProjectsPart(ListView):
    model = ProjectsParticipate
    template_name = 'title/projects_part.html'


class Publ(ListView):
    model = Publications
    template_name = 'title/publications.html'