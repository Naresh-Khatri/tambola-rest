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
        
class TicketGetSerializer(serializers.ModelSerializer):
    # winner = WinnerGetSerializer(many=True, read_only=True)
    class Meta:
        model = models.Ticket
        fields = ('id', 'ticket_id', 'ticket', 'customer_name', 'game')

class WinnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Winner
        fields = '__all__'
class WinnerGetSerializer(serializers.ModelSerializer):
    ticket = TicketGetSerializer()
    class Meta:
        model = models.Winner
        fields = ['win_type', 'ticket']

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Game
        # fields = ['game_id', 'winner']
        fields = '__all__'
class GameGetSerializer(serializers.ModelSerializer):
    winner_game = WinnerGetSerializer(many=True, read_only=True)
    # winners = serializers.SerializerMethodField()

    # def get_winners(self, instance):
    #     queryset = [x for x in instance.winners.all()]
    #     return WinnerSerializer(queryset, many=True, context=self.context).data
    class Meta:
        model = models.Game
        #fields = ["game_id","winner_game", 'winners']
        fields = '__all__'