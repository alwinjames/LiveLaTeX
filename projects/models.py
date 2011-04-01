from django.db import models

class Project(models.Model):
	user_id = models.IntegerField()
	project_name = models.CharField(max_length=30)
	project_id = models.IntegerField()

def __unicode__(self):
	return u'%s %s' %(self.first_name,self.last_name)

