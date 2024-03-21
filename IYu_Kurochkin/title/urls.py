from django.urls import path
from . import views

urlpatterns = [
    path('', views.TitlePage.as_view(), name='home'),
    path('edu', views.EducationWorkView.as_view(), name='edu'),
    path('project_part', views.ProjectsPart.as_view(), name='project_part'),
    path('publications', views.Publ.as_view(), name='publications'),
    path('skills', views.SkillsView.as_view(), name='skills'),
]