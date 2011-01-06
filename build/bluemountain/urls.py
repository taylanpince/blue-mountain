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
    
    # Contact
    (r'^contact/', include('contact.urls')),
    
    # Conditions
    (r'^conditions/', include('conditions.urls')),
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

    # About / Resort Map
    url(r"^about/$", "direct_to_template", {
        "template": "about/resort-map.html",
    }, name="about_resort_map"),

    # About / Ticket Info
    url(r"^about/ticket-info/$", "direct_to_template", {
        "template": "about/ticket-info.html",
    }, name="about_ticket_info"),

    # About / Restaurants and Hotels
    url(r"^about/restaurants-hotels/$", "direct_to_template", {
        "template": "about/restaurants-hotels.html",
    }, name="about_restaurants_hotels"),
)
