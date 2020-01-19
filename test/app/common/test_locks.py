import inspect
import unittest

from pynamodb.attributes import UnicodeAttribute, UTCDateTimeAttribute, NumberAttribute, BinaryAttribute

from app.common.models.locks import LockManager, LockTable


class LockManagerTests(unittest.TestCase):

    def setUp(self):
        self.lock_manager = LockManager()

    def tearDown(self):
        pass

    def test_LockTable_class_exists(self):
        self.assertTrue(inspect.isclass(LockTable))

    def test_LockTable_class_properties_exists(self):
        self.assertTrue(isinstance(LockTable.lock_name, UnicodeAttribute))
        self.assertTrue(isinstance(LockTable.creation_time, UTCDateTimeAttribute))
        self.assertTrue(isinstance(LockTable.expiration_time, UTCDateTimeAttribute))
        self.assertTrue(isinstance(LockTable.version_number, NumberAttribute))
        self.assertTrue(isinstance(LockTable.is_released, BinaryAttribute))

    def test_LockTable_class_methods_exists(self):
        self.assertTrue(inspect.ismethod(LockTable.get_future_datetime))

    def test_LockManager_class_exists(self):
        self.assertTrue(inspect.isclass(LockManager))
        # self.assertTrue(inspect.ismethod(LockManager.describe))
        # self.assertTrue(inspect.ismethod(LockManager.acquire))
        # self.assertTrue(inspect.ismethod(LockManager.renew))
        # self.assertTrue(inspect.ismethod(LockManager.release))
