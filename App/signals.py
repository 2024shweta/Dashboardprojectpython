# dashboard/signals.py

from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import UserProfile

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(username=instance.username, email=instance.email)

post_save.connect(create_user_profile, sender=User)