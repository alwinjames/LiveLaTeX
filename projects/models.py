import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class Project(models.Model):
	user = models.ForeignKey(User, verbose_name=_('Username'))
	proj_name = models.CharField(_('Project Name'), max_length=30)
	proj_id = models.AutoField(_('Project ID'), primary_key=True)
	added = models.DateTimeField(_('Added On'), auto_now=True)

def __unicode__(self):
	return self.proj_name

