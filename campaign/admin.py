from django.contrib import admin
from .models import Agency, APIKey, AgencyAPIKeyMapping, Campaign

admin.site.register(Agency)
admin.site.register(APIKey)
admin.site.register(AgencyAPIKeyMapping)
admin.site.register(Campaign)
