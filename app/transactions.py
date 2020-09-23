from app import settings
from app.db.engine import create_engine
from app.db.gateways import UserTableGateway

db_engine = create_engine(settings.DATABASES['main']['DSN'])


class UserNotAddedError(Exception):
    """Exception."""


def add_user(user_id):
    try:
        UserTableGateway(db_engine).insert_one(user_id=user_id)
    except db_engine.driver.IntegrityError as e:
        raise UserNotAddedError(e)


def get_user(user_id):
    return UserTableGateway(db_engine).find_by_user_id(user_id=user_id)
