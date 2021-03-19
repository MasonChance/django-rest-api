from rest_framework import serializers
from .models import Deck

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'owner', 'league', 'size', 'mana_type')
        model = Deck

    