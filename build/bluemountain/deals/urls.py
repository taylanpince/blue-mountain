from django.conf.urls.defaults import *


urlpatterns = patterns('deals.views',
    url(r'^$', 'deals', name='deals'),
)
