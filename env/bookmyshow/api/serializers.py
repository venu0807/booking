from rest_framework import serializers
from .models import *


class MovieSerializer(serializers.ModelSerializer):

    cast_data = serializers.JSONField(required=False)
    crew_data = serializers.JSONField(required=False)

    class Meta:
        model = MovieModel
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = RatingModel
        fields = '__all__'


class CastSerializer(serializers.ModelSerializer):
    class Meta:
        model = CastModel
        fields = '__all__'


class CrewSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrewModel
        fields = '__all__'


class TheaterShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = TheaterShowModel
        fields = '__all__'


class SeatBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeatBookingModel
        fields = '__all__'






