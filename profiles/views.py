from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from . import serializers 
from . import models


class UserProfileViewSet(viewsets.ModelViewSet):

    queryset = models.UserProfile.objects.all()
    serializer_class = serializers.UserProfileSerializer

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key,
                        'user_id':token.user.id,
                        'user_name':token.user.name,
                        'user_phone':token.user.phone_no,
                        'user_is_staff':token.user.is_staff,
                        })

class TicketViewSet(viewsets.ModelViewSet):

    queryset = models.Ticket.objects.all()
    serializer_class = serializers.TicketSerializer
    filterset_fields = ['game_id', 'ticket_id', 'booked_by']
    ordering_fields = ['game_id', 'ticket_id']

    #update the booked_by field when booked 
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.booked_by = request.user
        instance.save()
        return super().update(request, *args, **kwargs)

class TicketGetViewSet(viewsets.ModelViewSet):
    queryset = models.Ticket.objects.all()
    serializer_class = serializers.TicketGetSerializer
    filterset_fields = ['game_id', 'ticket_id', 'customer_name']


class WinnerViewSet(viewsets.ModelViewSet):
    queryset = models.Winner.objects.all()
    serializer_class = serializers.WinnerSerializer
    #filterset_field = ['']
class WinnerGetViewSet(viewsets.ModelViewSet):
    queryset = models.Winner.objects.all()
    serializer_class = serializers.WinnerGetSerializer


class GameViewSet(viewsets.ModelViewSet):
    queryset = models.Game.objects.all()
    serializer_class = serializers.GameSerializer
    #filterset_field = ['']
class GameGetViewSet(viewsets.ModelViewSet):
    '''only for public get'''
    queryset = models.Game.objects.all()
    serializer_class = serializers.GameGetSerializer
    #filterset_field = ['']

