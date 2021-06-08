from django.contrib import admin
from accounts.models.user import User
from accounts.models.profile import Profile

admin.site.register(User)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name',
                    'user', 'date_of_birth', 'photo']
