from django.db import models

class User (models.Model):
	user_id = models.IntegerField()
	user_name = models.CharField(max_length=50)
	email_id = models.EmailField(blank=True, verbose_name='e-mail')
	password = models.CharField(max_length=10)

def __unicode__(self):
	return u'%s %s' %(self.first_name,self.last_name)

