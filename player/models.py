from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField


class Player(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    institute_id = models.CharField(max_length=20, unique=True, db_index=True, primary_key=True)
    contact = PhoneNumberField()

@receiver(pre_save, sender=User)
def check_limits(sender, instance, **kwargs):
    if instance.player_set.count() > 2:
        raise ValidationError("Too many players on this team")