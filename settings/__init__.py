__author__ = 'zachmccormick'

from settings.default_settings import *

if os.getenv('IS_PROD', False):
    from settings.prod_settings import *
else:
    from settings.local import *
