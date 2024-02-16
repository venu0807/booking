# Generated by Django 4.2.3 on 2024-01-21 14:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='movies/')),
                ('background', models.ImageField(blank=True, null=True, upload_to='movies/')),
                ('moviename', models.CharField(max_length=50)),
                ('runtime', models.CharField(blank=True, max_length=10, null=True)),
                ('certificate', models.CharField(blank=True, max_length=10, null=True)),
                ('screentype', models.CharField(max_length=50)),
                ('genre', models.CharField(max_length=50)),
                ('release_date', models.DateField()),
                ('about', models.CharField(blank=True, max_length=1000, null=True)),
                ('languages', models.CharField(max_length=50)),
                ('trailer_link', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TheaterShowModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('total_rows', models.IntegerField(default=20)),
                ('show_times', models.JSONField(default=list)),
                ('show_dates', models.JSONField(default=list)),
                ('is_active', models.BooleanField(default=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='theater_show', to='api.moviemodel')),
                ('screentype', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='screentype_theater_show', to='api.moviemodel')),
            ],
        ),
        migrations.CreateModel(
            name='SeatBookingModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_number', models.JSONField(default=list)),
                ('is_booked', models.BooleanField(default=False)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('show_date', models.DateField(null=True)),
                ('show_time', models.JSONField(default=list)),
                ('booking_date', models.DateTimeField(auto_now_add=True)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_status', models.CharField(default='Pending', max_length=20)),
                ('movie', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='movie_seat_bookings', to='api.moviemodel')),
                ('screentype', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='screentype_seat_bookings', to='api.moviemodel')),
                ('theater', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seat_bookings', to='api.theatershowmodel')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_seat_bookings', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RatingModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True)),
                ('reviews', models.TextField(blank=True, null=True)),
                ('movie', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.moviemodel')),
            ],
        ),
        migrations.CreateModel(
            name='CrewModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crew_member_name', models.CharField(max_length=50)),
                ('crew_member_image', models.ImageField(blank=True, null=True, upload_to='movies/crew/')),
                ('role', models.CharField(max_length=50)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='crew', to='api.moviemodel')),
            ],
        ),
        migrations.CreateModel(
            name='CastModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actor_name', models.CharField(max_length=50)),
                ('actor_image', models.ImageField(blank=True, null=True, upload_to='movies/cast/')),
                ('movie_role', models.CharField(max_length=50)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cast', to='api.moviemodel')),
            ],
        ),
    ]