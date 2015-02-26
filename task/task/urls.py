from django.conf.urls import patterns, include, url
from django.contrib import admin

from lst import views

urlpatterns = patterns('',
    url(r'^', include('lst.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
