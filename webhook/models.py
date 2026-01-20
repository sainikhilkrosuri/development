from django.db import models
import uuid
from django.conf import settings

# Create your models here.
class Webhook(models.Model):
    id = models.UUIDField(primary_key = True, default=uuid.uuid4, editable=False)
    client = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="webhooks",
    )
    target_url = models.URLField()
    secret = models.CharField(max_length=64)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Webhook {self.id}"
    

class WebhookEvent(models.Model):
    webhook = models.ForeignKey(Webhook, on_delete=models.CASCADE)
    payload = models.JSONField()
    status = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)