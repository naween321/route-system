SECRET_KEY = ""
DEBUG = True
if DEBUG:
    ALLOWED_HOSTS = ['*']
else:
    ALLOWED_HOSTS = ['example.domain.com']
