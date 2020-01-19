from datetime import datetime, timezone, timedelta
from pynamodb.attributes import UnicodeAttribute, NumberAttribute, UTCDateTimeAttribute, BinaryAttribute
from app.common.models import BaseModel


class LockTable(BaseModel):
    lock_name = UnicodeAttribute(hash_key=True)
    creation_time = UTCDateTimeAttribute(range_key=True, default=lambda: datetime.now(timezone.utc))
    expiration_time = UTCDateTimeAttribute()
    version_number = NumberAttribute(default=1)
    is_released = BinaryAttribute(default=False)

    @staticmethod
    def get_future_datetime(minutes_into_future):
        current_datetime = datetime.now()
        time_delta_minutes = timedelta(minutes=minutes_into_future)
        return current_datetime + time_delta_minutes

    class Meta(BaseModel.Meta):
        table_name = 'Lock'
        write_capacity_units = 1
        read_capacity_units = 1


class LockManager(object):

    def __init__(self):
        if not LockTable.exists():
            LockTable.create_table(wait=True)
        self.lock = LockTable()

    def describe(self, lock_name):
        pass

    def acquire(self, lock_name, wait=False):
        pass

    def renew(self, lock_name):
        pass

    def release(self, lock_name):
        pass
