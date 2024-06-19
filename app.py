import os

os.environ.setdefault(DJANGO_SETTINGS, projectcore.settings)
application = get_wsgi_application()
