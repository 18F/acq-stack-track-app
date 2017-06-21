from django.db import models
from django.contrib.auth.models import User

class Request(models.Model):
    below_mp_threshold = models.NullBooleanField()
    is_training = models.NullBooleanField()
    is_internal = models.NullBooleanField()
    client_has_approval = models.NullBooleanField()
    client_contact = models.CharField(max_length=200, null=True)
    urgency = models.TextField(null=True)
    description = models.TextField(null=True)
    submitted_at = models.DateTimeField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
