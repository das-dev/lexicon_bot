import os

DATABASES = {
    'main': {
        'DSN': 'sqlite3://lexicon.db',
    },
    'testing': {
        'DSN': ':memory:'
    }
}

TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')
