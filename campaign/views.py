from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Campaign, Agency, AgencyAPIKeyMapping
from .serializers import CampaignSerializer
from .tasks import process_campaign

class CreateCampaignView(APIView):
    def post(self, request):
        serializer = CampaignSerializer(data=request.data)
        if serializer.is_valid():
            campaign = serializer.save()
            # Send to Celery
            process_campaign(campaign.id)
            return Response({"message": "Campaign created and queued."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
