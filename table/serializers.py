from rest_framework import serializers
from .models import Usr, Tabletop


class UsrSerializer(serializers.ModelSerializer):
    # owner = serializers.RelatedField(many=True)
    class Meta:
        model = Usr
        fields = '__all__'

class TabletopSerializer(serializers.ModelSerializer):
    # owner = serializers.PrimaryKeyRelatedField()
    # owner = serializers.RelatedField(many=True)
    class Meta:
        model = Tabletop
        fields = '__all__'
