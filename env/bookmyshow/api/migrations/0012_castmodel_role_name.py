# Generated by Django 4.2.3 on 2024-01-25 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_remove_castmodel_movie_remove_crewmodel_movie_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='castmodel',
            name='role_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
