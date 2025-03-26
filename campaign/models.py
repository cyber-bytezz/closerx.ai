from django.db import models

class Agency(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class APIKey(models.Model):
    key = models.CharField(max_length=255, unique=True)
    concurrency_limit = models.IntegerField(default=50)

    def __str__(self):
        return f"Key {self.id}"


class AgencyAPIKeyMapping(models.Model):
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE)
    api_key = models.ForeignKey(APIKey, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.agency.name} → Key {self.api_key.id}"


class Campaign(models.Model):
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    status = models.CharField(max_length=50, default='queued')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.agency.name})"
