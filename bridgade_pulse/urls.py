from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bridgade_pulse.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', 'api.views.index'),

    url(r'^admin/', include(admin.site.urls)),
)
