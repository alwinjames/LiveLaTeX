from django.contrib import admin
from livelatex.usr.models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('username', 'user_id')

admin.site.register(UserProfile, UserProfileAdmin)
