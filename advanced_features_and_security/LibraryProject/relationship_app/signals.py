from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.apps import apps

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile = apps.get_model('relationship_app', 'UserProfile')
        UserProfile.objects.create(user=instance, role='Member')

