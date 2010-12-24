from django.conf.urls.defaults import *


urlpatterns = patterns('contests.views',
    url(r'^$', 'enter', name='contests_enter'),
    url(r'^share/$', 'share', name='contests_share'),
    url(r'^rules/$', 'rules', name='contests_rules'),
    url(r'^winners/$', 'winners', name='contests_winners'),
    url(r'^photos/$', 'photos', name='contests_photos'),
    url(r'^thanks/$', 'thanks', name='contests_thanks'),
    url(r'^prizes/$', 'prizes', name='contests_prizes'),
)
