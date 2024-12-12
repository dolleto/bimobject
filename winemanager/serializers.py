from winemanager.models import WineBottle, Winemaker
from rest_framework import serializers


class WinemakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Winemaker
        fields = "__all__"


class WineBottleSerializer(serializers.ModelSerializer):
    class Meta:
        model = WineBottle
        fields = "__all__"
