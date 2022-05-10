from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import bank_profile

@receiver(post_save,sender=User)
def create_bank_profile(sender,instance,created,**kwards):
    if created:
        bank_profile.objects.create(user=instance)

@receiver(post_save,sender=User)
def save_bank_profile(sender,instance,**kwards):
    instance.bank_profile.save()