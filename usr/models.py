from django.db import models
from uuidfield import UUIDField
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model):  
	user = models.ForeignKey(User)  
	user_id = UUIDField(auto=True)
	email_id = models.EmailField(User)
	password = models.CharField(User, max_length=10)

def __str__(self):  
          return "%s's profile" % self.user  

def create_user_profile(sender, instance, created, **kwargs):  
    if created:  
       profile, created = UserProfile.objects.get_or_create(user=instance)  

post_save.connect(create_user_profile, sender=User) 

