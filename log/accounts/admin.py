from django.contrib import admin
from accounts.models import UserProfile,Company

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Company)
