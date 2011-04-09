from django.contrib.auth.models import User, UserManager
from django.db import models
from uuidfield import UUIDField

class UserProfile(User):
	user_id = UUIDField(auto=True)		
	objects = UserManager()

def __unicode__ (self):
	return self.user_name

def save(self):
	User.save(self)
