from django.conf.urls.defaults import *


urlpatterns = patterns('contact.views',
    url(r'^$', 'contact', name='contact'),
    url(r'^thanks/$', 'thanks', name='contact_thanks'),
)
