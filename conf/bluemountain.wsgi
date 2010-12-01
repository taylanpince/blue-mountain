import os
import sys
import site

site.addsitedir('/home/bluemountainteam/sites/blue-mountain/lib/python2.6/site-packages')

sys.path.append("/home/bluemountainteam/sites/blue-mountain/src/blue-mountain/build/backend")
sys.path.append("/home/bluemountainteam/sites/blue-mountain/src/blue-mountain/build/backend/bluemountain")

os.environ["DJANGO_SETTINGS_MODULE"] = "bluemountain.settings"

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
