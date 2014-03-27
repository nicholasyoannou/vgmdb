import os
try:
	from .config_private import *
except:
	pass

BASE_URL = 'http://vgmdb.info/'
AUTO_RELOAD = False
CELERY_BROKER = 'amqp://guest@127.0.0.1//'
CELERY_RESULT_BACKEND = 'cache'
CELERY_CACHE_BACKEND = 'memcached://127.0.0.1:11211/'
CELERY_PING = True


if os.environ.has_key('GAE_BASEURL'):
	BASE_URL = os.environ['GAE_BASEURL']

class Settings(object):
	pass

def get_defaults():
	settings = Settings()
	settings.BASE_URL = BASE_URL
	settings.AUTO_RELOAD = AUTO_RELOAD
	settings.jsonp_callback = 'jsonp_callback'
	return settings

def for_request(request):
	settings = get_defaults()
	if request.get_header('Host'):
		settings.BASE_URL = 'http://%s/'%(request.get_header('Host'),)
	if request.get_header('base_url'):
		settings.BASE_URL = request.get_header('base_url')
	if request.query.get('callback'):
		settings.jsonp_callback = request.query.get('callback')
	return settings
