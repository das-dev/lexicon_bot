from app import settings
from app.db.engine import create_engine

db_engine = create_engine(settings.DATABASES['main']['DSN'])


def create_cards_table():
    sql = 'CREATE TABLE IF NOT EXISTS cards (' \
          'pk INTEGER PRIMARY KEY AUTOINCREMENT,' \
          'back_side,' \
          'languages' \
          ');'
    with db_engine.connect() as conn:
        conn.execute(sql)


def create_users_table():
    sql = 'CREATE TABLE IF NOT EXISTS users (' \
          'pk INTEGER PRIMARY KEY AUTOINCREMENT,' \
          'user_id INTEGER' \
          ');'
    with db_engine.connect() as conn:
        conn.execute(sql)


if __name__ == '__main__':
    create_cards_table()
    create_users_table()
