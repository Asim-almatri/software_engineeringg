SECRET_KEY = 'your-secret-key'
DEBUG = True
ALLOWED_HOSTS = []
INSTALLED_APPS = ['django.contrib.contenttypes', 'django.contrib.staticfiles', 'pages']
MIDDLEWARE = ['django.middleware.common.CommonMiddleware']
ROOT_URLCONF = 'mysite.urls'
TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [],
    'APP_DIRS': True,
    'OPTIONS': {},
}]
WSGI_APPLICATION = 'mysite.wsgi.application'
STATIC_URL = '/static/'
