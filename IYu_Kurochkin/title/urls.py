from django.urls import path
from . import views

urlpatterns = [
    # path('', views.TitlePage.as_view(), name='home'),
    path('', views.title_page,),
    path('edu', views.EducationWorkView.as_view(), name='edu'),
    path('project_part', views.ProjectsPart.as_view(), name='project_part'),
    path('publications', views.Publ.as_view(), name='publications'),
    path('skills', views.SkillsView.as_view(), name='skills'),
    path('skills_prog', views.SkillsViewProg.as_view(), name='skills_prog'),
    path('drawing_skills', views.SkillsViewDraw.as_view(), name='drawing_skills'),
    path('other_skills', views.SkillsOther.as_view(), name='other_skills'),
    path('qc_skills', views.SkillsQC.as_view(), name='qc_skills'),
    path('en', views.title_page_en, ),
    path('edu/en', views.EducationWorkViewEn.as_view(), name='edu'),
    path('project_part/en', views.ProjectsPartEn.as_view(), name='project_part'),
    path('publications/en', views.PublEn.as_view(), name='publications'),
    path('skills/en', views.SkillsViewEn.as_view(), name='skills'),
    path('skills_prog/en', views.SkillsViewProgEn.as_view(), name='skills_prog'),
    path('drawing_skills/en', views.SkillsViewDrawEn.as_view(), name='drawing_skills'),
    path('other_skills/en', views.SkillsOtherEn.as_view(), name='other_skills'),
    path('qc_skills/en', views.SkillsQCEn.as_view(), name='qc_skills'),
]