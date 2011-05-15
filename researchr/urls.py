from django.conf.urls.defaults import *
from django.contrib import admin
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^researchr/', include('researchr.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    (r'^openid/', include('django_openid_consumer.urls')),
    
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^$', 'researchr.entry.views.ShowEntrySetAction'),
    (r'^entries/new$', 'researchr.entry.views.NewEntryAction'),
    (r'^entries/(?P<id>[A-Fa-f0-9]*)/?$', 'researchr.entry.views.ShowEntryAction'),
)
