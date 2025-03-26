from django.urls import path
from .views import CreateCampaignView

urlpatterns = [
    path('create_campaign/', CreateCampaignView.as_view(), name='create_campaign'),
]
