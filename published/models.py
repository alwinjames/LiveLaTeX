from django.db import models

class Published(models.Model):
	pub_link = models.CharField(max_length=50)
	file_id = models.IntegerField()

def __unicode__(self):
	return u'%s %s' %(self.first_name,self.last_name)

