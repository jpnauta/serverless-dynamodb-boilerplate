from pynamodb.attributes import UnicodeAttribute, UTCDateTimeAttribute, VersionAttribute

from app.common.models import BaseModel


class UserModel(BaseModel):
    class Meta(BaseModel.Meta):
        table_name = 'User'

    first_name = UnicodeAttribute(range_key=True)
    last_name = UnicodeAttribute(hash_key=True)
    email = UnicodeAttribute(null=True)
    last_updated = UTCDateTimeAttribute(null=True)
