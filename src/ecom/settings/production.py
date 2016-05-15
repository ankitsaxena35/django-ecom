
#static is here mvpland_static
#postgresql -- mvpland
#username -- cfedeploy
#password -- ##


"""
Django settings for ecom project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

from django.conf import settings

if not settings.DEBUG:
	import os

	BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
	#root of project

	# Quick-start development settings - unsuitable for production
	# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

	# SECURITY WARNING: keep the secret key used in production secret!
	SECRET_KEY = 'csqwlmc8s55o($rt6ozh7u+ui9zb-et00w$d90j8$^!nvj41_r'

	# SECURITY WARNING: don't run with debug turned on in production!
	DEBUG = False

	ADMINS = (
		("Justin", "codingforentrepreneurs@gmail.com"),

		)

	ALLOWED_HOSTS = ['cfedeploy.webfactional.com', 'trydjango.com', 'www.trydjango.com']
	#purchasing domain name http://name.com

	EMAIL_HOST = 'smtp.gmail.com'
	EMAIL_HOST_USER = 'yourgmail@gmail.com'
	EMAIL_HOST_PASSWORD = 'yourpassword'
	EMAIL_PORT = 587
	EMAIL_USE_TLS = True

	''' 
	If using gmail, you will need to
	unlock Captcha to enable Django 
	to  send for you:
	https://accounts.google.com/displayunlockcaptcha
	'''



	# Application definition

	INSTALLED_APPS = (
	    #django app
	    'django.contrib.admin',
	    'django.contrib.auth',
	    'django.contrib.contenttypes',
	    'django.contrib.sessions',
	    'django.contrib.sites',
	    'django.contrib.messages',
	    'django.contrib.staticfiles',
	    #third party apps
	    'crispy_forms',
	    'registration',
	    #my apps
	    'newsletter',
	)

	MIDDLEWARE_CLASSES = (
	    'django.contrib.sessions.middleware.SessionMiddleware',
	    'django.middleware.common.CommonMiddleware',
	    'django.middleware.csrf.CsrfViewMiddleware',
	    'django.contrib.auth.middleware.AuthenticationMiddleware',
	    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
	    'django.contrib.messages.middleware.MessageMiddleware',
	    'django.middleware.clickjacking.XFrameOptionsMiddleware',
	    'django.middleware.security.SecurityMiddleware',
	)

	ROOT_URLCONF = 'ecom.urls'

	TEMPLATES = [
	    {
	        'BACKEND': 'django.template.backends.django.DjangoTemplates',
	        'DIRS': [os.path.join(BASE_DIR, "templates")],
	        'APP_DIRS': True,
	        'OPTIONS': {
	            'context_processors': [
	                'django.template.context_processors.debug',
	                'django.template.context_processors.request',
	                'django.contrib.auth.context_processors.auth',
	                'django.contrib.messages.context_processors.messages',
	            ],
	        },
	    },
	]

	WSGI_APPLICATION = 'ecom.wsgi.application'


	# Database
	# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

	from .db_password import DBPASS

	DATABASES = {
	    'default': {
	        'ENGINE': 'django.db.backends.postgresql_psycopg2',
	        'NAME': "mvpland",
	        'USER': "cfedeploy",
	        'PASSWORD': DBPASS,
	    }
	}


	# Internationalization
	# https://docs.djangoproject.com/en/1.8/topics/i18n/

	LANGUAGE_CODE = 'en-us'

	TIME_ZONE = 'UTC'

	USE_I18N = True

	USE_L10N = True

	USE_TZ = True


	# Static files (CSS, JavaScript, Images)
	# https://docs.djangoproject.com/en/1.8/howto/static-files/

	STATIC_URL = '/static/'

	STATIC_ROOT = '/home/cfedeploy/webapps/mvpland_static/'
	#os.path.join(os.path.dirname(BASE_DIR), "static_in_env", "static_root")
	    
	STATICFILES_DIRS = (
	    os.path.join(BASE_DIR, "static_in_pro", "our_static"),
	    #os.path.join(BASE_DIR, "static_in_env"),
	    #'/var/www/static/',
	)

	MEDIA_URL = '/media/'
	MEDIA_ROOT = '/home/cfedeploy/webapps/mvpland_media/'
	#os.path.join(os.path.dirname(BASE_DIR), "static_in_env", "media_root")


	#Crispy FORM TAGs SETTINGS
	CRISPY_TEMPLATE_PACK = 'bootstrap3'


	#DJANGO REGISTRATION REDUX SETTINGS
	ACCOUNT_ACTIVATION_DAYS = 7
	REGISTRATION_AUTO_LOGIN = True
	SITE_ID = 1
	LOGIN_REDIRECT_URL = '/'





