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

    # Privacy Policy
    url(r"^privacy-policy/$", "direct_to_template", {
        "template": "privacy.html",
    }, name="privacy"),

    # Terms & Conditions
    url(r"^terms/$", "direct_to_template", {
        "template": "terms.html",
    }, name="terms"),

    # Contact
    url(r"^contact/$", "direct_to_template", {
        "template": "contact.html",
    }, name="contact"),
)
