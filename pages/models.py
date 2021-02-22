from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Expert(models.Model):
    name = models.CharField(blank=True, max_length=300)


class Meeting(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    expert = models.ForeignKey(Expert, on_delete=models.SET_NULL, blank=True, null=True)
    objective = models.TextField(null=True, blank=True)