from django.conf.urls.defaults import *
from django.contrib import admin


admin.autodiscover()


urlpatterns = patterns('',
    # Admin Docs
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Admin
    (r'^admin/', include(admin.site.urls)),
    
    # Contests
    (r'^contest/', include('contests.urls')),
)

urlpatterns += patterns('django.views.generic.simple',
    # Home
    url(r"^$", "direct_to_template", {
        "template": "home.html",
    }, name="home"),
)
