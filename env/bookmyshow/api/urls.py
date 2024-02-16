from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import * 


from rest_framework_simplejwt.views import (
    TokenRefreshView,
)



router = DefaultRouter()
router.register(r'movie', MovieViewSet, basename='movie')
router.register(r'rating', RatingViewSet, basename='rating')
router.register(r'cast', CastViewSet, basename='cast')
router.register(r'crew', CrewViewSet, basename='crew')
router.register(r'theatershow', TheaterShowViewSet, basename='theatershow')
router.register(r'seatbooking', SeatBookingViewSet, basename='seatbooking')

app_name = 'bookmyshow'

urlpatterns = [
    path('',include(router.urls)),
    path('register/', register_user, name='register_user'),
    path('movie/search/', MovieSearchView.as_view(), name='movie_search'),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]

