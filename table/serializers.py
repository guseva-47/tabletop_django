from rest_framework import serializers
from .models import Usr, Tabletop


class UsrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usr
        fields = '__all__'

class TabletopSerializer(serializers.ModelSerializer):
    owner = UsrSerializer()
    players = UsrSerializer(many=True)
    class Meta:
        model = Tabletop
        fields = '__all__'