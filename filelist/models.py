from django.db import models

class Filelist(models.Model):
	file_id = models.CharField(max_length=20)

def __unicode__(self):
	return u'%s %s' %(self.first_name,self.last_name)

