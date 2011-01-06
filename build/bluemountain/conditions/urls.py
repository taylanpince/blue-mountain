from django.conf.urls.defaults import *


urlpatterns = patterns('conditions.views',
    url(r'^$', 'live', name='conditions_live'),
    url(r'^trail-map/$', 'trail_map', name='conditions_trail_map'),
)
