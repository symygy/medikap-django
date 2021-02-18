import sys, os
sys.path.append(os.getcwd())
os.environ['DJANGO_SETTINGS_MODULE'] = "medikap-django.medikap.settings"
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()