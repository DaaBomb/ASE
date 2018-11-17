from django.contrib import admin
from accounts.models import UserProfile,Company, recent_activity

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Company)
admin.site.register(recent_activity)
