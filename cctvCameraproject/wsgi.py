import os
import sys

# Python path to your project
path = '/home/sarthkdhage/cctvCameraproject'
if path not in sys.path:
    sys.path.append(path)

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cctvCameraproject.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
