from .models import MovieModel, RatingModel, CastModel, CrewModel, TheaterShowModel, SeatBookingModel
from .serializers import MovieSerializer, RatingSerializer, CastSerializer, CrewSerializer, TheaterShowSerializer, SeatBookingSerializer
from  rest_framework import viewsets


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny




from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json




from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token

 
 
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer




@csrf_exempt
def register_user(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return JsonResponse({'detail': 'Invalid data'}, status=400)

        try:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            return JsonResponse({'detail': 'User registered successfully'})
        except Exception as e:
            return JsonResponse({'detail': str(e)}, status=500)
    else:
        return JsonResponse({'detail': 'Invalid request method'}, status=405)








@permission_classes([AllowAny])
class MovieViewSet(viewsets.ModelViewSet):
    queryset = MovieModel.objects.all()
    serializer_class = MovieSerializer

@permission_classes([AllowAny])
class RatingViewSet(viewsets.ModelViewSet):
    queryset = RatingModel.objects.all()
    serializer_class = RatingSerializer


@permission_classes([AllowAny])
class CastViewSet(viewsets.ModelViewSet):
    queryset = CastModel.objects.all()
    serializer_class = CastSerializer

    # def get_queryset(self):
    #     movie_id = self.kwargs['movie_id']
    #     return CastModel.objects.filter(movie_id=movie_id)


@permission_classes([AllowAny])
class CrewViewSet(viewsets.ModelViewSet):
    queryset = CrewModel.objects.all()
    serializer_class = CrewSerializer


@permission_classes([AllowAny])
class TheaterShowViewSet(viewsets.ModelViewSet):
    queryset = TheaterShowModel.objects.all()
    serializer_class = TheaterShowSerializer




@permission_classes([AllowAny])
class SeatBookingViewSet(viewsets.ModelViewSet):
    queryset = SeatBookingModel.objects.all()
    serializer_class = SeatBookingSerializer

    def save(self, *args, **kwargs):
        self.row_number = self.row_number.upper()
        self.is_booked = True  # Mark the seat as booked
        super().save(*args, **kwargs)





from django.views import View
from django.db.models import Q


class MovieSearchView(View):
    def get(self, request, *args, **kwargs):
        query = request.GET.get('query', '')
        print(f"Received query: {query}")
        
        results = MovieModel.objects.filter(Q(moviename__icontains=query) | Q(starring__icontains=query))
        print(f"Results: {results}")

        response_data = [{'id': movie.id, 'moviename': movie.moviename} for movie in results]
        return JsonResponse(response_data, safe=False)
    
