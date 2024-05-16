from django.db import models


class EducationWork(models.Model):
    date = models.CharField(max_length=20, verbose_name='Date')
    position = models.CharField(max_length=255, verbose_name='status')
    organisation = models.CharField(max_length=255, verbose_name='organisation_name')
    last_actual_year = models.IntegerField(max_length=4, verbose_name='last_actual_year', blank=True, null=True)
    type = models.CharField(max_length=40, verbose_name='type', blank=True, null=True)

    def __str__(self):
        return self.position

    class Meta:
        verbose_name = 'EducationWork'
        verbose_name_plural = 'EducationWork'
        ordering = ['-last_actual_year']


class Publications(models.Model):
    article_title = models.CharField(max_length=355, verbose_name='article_title')
    authors = models.CharField(max_length=555, verbose_name='article_title')
    doi = models.URLField(max_length=200, verbose_name='doi')
    wos = models.BooleanField()
    scopus = models.BooleanField()
    e_library = models.BooleanField()
    year = models.IntegerField(verbose_name='year')
    journal = models.CharField(max_length=400, verbose_name='journal', default=' ')
    quartile = models.IntegerField(verbose_name='quartile', default=1, null=True, blank=True)

    def __str__(self):
        return self.article_title

    class Meta:
        verbose_name = 'Publications'
        verbose_name_plural = 'Publications'
        ordering = ['year']


class Identificators(models.Model):
    type = models.CharField(max_length=40, verbose_name='index_type')
    number = models.CharField(max_length=30, verbose_name='index_number')

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = 'Identificators'
        verbose_name_plural = 'Identificators'


class ProjectsParticipate(models.Model):
    project_title = models.CharField(max_length=400, verbose_name='project_title')
    foundation = models.CharField(max_length=300, verbose_name='foundation')
    project_number = models.CharField(max_length=50, verbose_name='project_number')
    project_year_start = models.IntegerField(verbose_name='project_year_start', null=True, blank=True)
    project_year_end = models.IntegerField(verbose_name='project_year_end', null=True, blank=True)

    def __str__(self):
        return self.project_title

    class Meta:
        verbose_name = 'ProjectsParticipate'
        verbose_name_plural = 'ProjectsParticipate'
        ordering = ['-project_year_end']

class Skills(models.Model):
    skill = models.CharField(max_length=500, verbose_name='Skill')
    skill_cat = models.ForeignKey('SkillCategory', blank=True, on_delete=models.PROTECT, verbose_name='skill_cat')

    def __str__(self):
        return self.skill

    class Meta:
        verbose_name = 'Skills'
        verbose_name_plural = 'Skills'
        ordering = ['skill_cat']


class SkillCategory(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='SkillCategory')
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'SkillCategory'
        verbose_name_plural = 'SkillCategory'
