# Generated by Django 5.0.4 on 2024-07-20 13:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("title", "0014_alter_drawworkexamples_img_file"),
    ]

    operations = [
        migrations.AddField(
            model_name="drawworkexamples",
            name="img_file_max_quality",
            field=models.ImageField(
                blank=True,
                default=None,
                null=True,
                upload_to="work_examples/max_quality/",
                verbose_name="draw_works_img_max_quality",
            ),
        ),
    ]