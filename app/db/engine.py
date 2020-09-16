from importlib import import_module
from urllib.parse import urlparse

IN_MEMORY = ':memory:'
db_engines = {
    'sqlite3': 'sqlite3',
}


class DBEngineException(Exception):
    """DB engine error."""


def create_engine(db_url):
    scheme, *path = urlparse(db_url)
    dbpath = ''.join(path)
    if dbpath == IN_MEMORY:
        scheme = 'sqlite3'
    if scheme not in db_engines or not dbpath:
        raise DBEngineException
    driver = import_module(db_engines[scheme])
    return DbEngine(driver, dbpath)


class DbEngine(object):
    def __init__(self, driver, dbpath):
        self.driver = driver
        self.dbpath = dbpath

    def connect(self):
        return self.driver.connect(self.dbpath)
