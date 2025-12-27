from django.db import models

# Create your models here.
class newWebhhook(models.Model):
    user_id = models.CharField(max_length=100)
    webhook_id = models.CharField(max_length=100)

    def __str__(self):
        return self.user_id