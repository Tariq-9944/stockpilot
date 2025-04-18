import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    ALPACA_API_KEY = os.environ.get('ALPACA_API_KEY', '')
    ALPACA_SECRET_KEY = os.environ.get('ALPACA_SECRET_KEY', '')
    LANGUAGES = ['en', 'ar', 'fr', 'es', 'tr']
