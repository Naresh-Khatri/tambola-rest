from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register('profiles', views.UserProfileViewSet)
router.register('tickets', views.TicketViewSet)
router.register('ticketsGet', views.TicketGetViewSet)
router.register('winners', views.WinnerViewSet)
router.register('winnersGet', views.WinnerGetViewSet)
router.register('games', views.GameViewSet)
router.register('gamesGet', views.GameGetViewSet)

urlpatterns = [
    path('', include(router.urls)),
     path('getToken/', views.CustomAuthToken.as_view())
]
