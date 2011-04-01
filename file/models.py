from django.db import models

class File(models.Model):
	file_id = models.IntegerField()
	file_name = models.CharField(max_length=20)
	file_link = models.CharField(max_length=100)
	last_edited = models.DateField()

def __unicode__(self):
	return u'%s %s' %(self.first_name,self.last_name)

