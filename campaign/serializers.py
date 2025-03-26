from rest_framework import serializers
from .models import Campaign

class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = ['id', 'agency', 'name', 'status', 'created_at']
        read_only_fields = ['status', 'created_at']
