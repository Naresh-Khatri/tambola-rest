from rest_framework import serializers
from . import models

class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.UserProfile
        fields = ('id','email', 'password', 'name', 'city', 'phone_no')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': { 'input_type': 'password' }
            }
        }


class TicketSerializer(serializers.ModelSerializer):

    class Meta:

        model = models.Ticket
        fields = '__all__'
