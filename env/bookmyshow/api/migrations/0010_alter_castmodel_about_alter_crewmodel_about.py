# Generated by Django 4.2.3 on 2024-01-25 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_remove_castmodel_movie_role_remove_crewmodel_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='castmodel',
            name='about',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='crewmodel',
            name='about',
            field=models.TextField(blank=True, null=True),
        ),
    ]
