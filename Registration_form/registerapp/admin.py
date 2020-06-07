from django.contrib import admin

from registerapp.models import UserProfileInfo,User

@admin.register(UserProfileInfo)
class userinfo(admin.ModelAdmin):
    list_display=('user','first_name','last_name')
    ordering=('user',)
    search_fields=('user',)
