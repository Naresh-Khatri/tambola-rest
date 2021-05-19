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