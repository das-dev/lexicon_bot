import unittest

from app.db import gateways


class MockConnection:
    def __repr__(self):
        return 'connection exist'


class TestDb(unittest.TestCase):
    ...  # TODO: to implement
