from gsi.userprofile.models import UserProfile
from django.contrib import admin
from django.contrib.auth.models import User

class UserProfileInline(admin.StackedInline):
    model = UserProfile

class UserAdmin(admin.ModelAdmin):
    inlines = [
        UserProfileInline
    ]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)