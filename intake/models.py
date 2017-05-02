from django.db import models

class Request(models.Model):
    below_mp_threshold = models.NullBooleanField()
    is_training = models.NullBooleanField()
    is_internal = models.NullBooleanField()
    client_has_approval = models.NullBooleanField()
    client_contact = models.CharField(max_length=200)
    urgency = models.TextField()
    description = models.TextField()
    submitted_at = models.DateTimeField(null=True)
