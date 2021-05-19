from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register('profile', views.UserProfileViewSet)
router.register('tickets', views.TicketViewSet)

urlpatterns = [
    path('', include(router.urls))
]
