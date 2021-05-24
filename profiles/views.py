from django.shortcuts import render
from rest_framework import viewsets
from . import serializers 
from . import models


class UserProfileViewSet(viewsets.ModelViewSet):

    queryset = models.UserProfile.objects.all()
    serializer_class = serializers.UserProfileSerializer

class TicketViewSet(viewsets.ModelViewSet):

    queryset = models.Ticket.objects.all()
    serializer_class = serializers.TicketSerializer
    filterset_fields = ['game_id', 'ticket_id']
    ordering_fields = ['game_id', 'ticket_id']
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

