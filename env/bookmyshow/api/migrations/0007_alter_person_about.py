# Generated by Django 4.2.3 on 2024-01-24 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_person_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='about',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
    ]
