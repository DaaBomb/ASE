from django.contrib import admin
from accounts.models import UserProfile,Company,teamtable,GroupUserTable

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Company)
admin.site.register(teamtable)
admin.site.register(GroupUserTable)
