from django.conf.urls import patterns, include, url
from django.contrib import admin

from lst import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'task.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^tasks/$', views.TaskList.as_view()),
    url(r'^tasks/(?P<pk>[0-9]+)/$', views.TaskDetail.as_view()),
)
