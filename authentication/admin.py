from django.contrib import admin

# Register your models here.
from authentication.models import (
    User, BlackList, UserProfile
)

admin.site.register(User)
admin.site.register(BlackList)
admin.site.register(UserProfile)
