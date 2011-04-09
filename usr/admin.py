from django.contrib import admin
from livelatex.usr.models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('user_id', 'user', 'email_id')

admin.site.register(UserProfile, UserProfileAdmin)
