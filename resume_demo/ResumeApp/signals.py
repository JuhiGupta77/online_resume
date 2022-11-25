from django.db.models.signals import post_save
from django.contrib.auth.models import User
# used as a decorator
from django.dispatch import receiver
# User profile that we created
from . models import UserProfile
# we need to wire this signals.py file to apps.py file


# receiver:
# when a User object is created, fires a signal to this signals.py file
# it receives and picks up that signal
@receiver(post_save, sender=User)
# if the user object is created through UserProfile.objects.create,
# then we want to create a userprofile which is then the user (which is a one-to-one field)
# equals instance (user=instance)
def create_profile(sender, instance, created, **kwargs):
    if created:
        userprofile = UserProfile.objects.create(user=instance)


