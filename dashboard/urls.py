from django.contrib import admin
from django.conf.urls import include, url
from assignments.views import index_view

urlpatterns = [
    url('admin/', admin.site.urls),
    url('assignments/', include('assignments.urls')),
    url('notifications/', include('notifications.urls')),
    url('clients/', include('clients.urls')),
    url('^$',index_view)
]
