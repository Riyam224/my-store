from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator
from django.db.models.signals import post_save
from django.dispatch import receiver





class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name = 'user', null=True, blank=True)
    city = models.ForeignKey('City', on_delete=models.CASCADE , blank=True, null=True )
    phone_number = models.CharField(max_length=15 , blank=True, null=True )
    image = models.ImageField(blank=True, null=True )
    
    
    def __str__(self):
        return str(self.user)
    




@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


class City(models.Model):
    name = models.CharField(max_length=30 , null=True, blank=True)

    def __str__(self):
        return self.name
  


