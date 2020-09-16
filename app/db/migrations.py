import settings
from app.db.engine import create_engine

db_engine = create_engine(settings.DATABASES['main']['DSN'])


def create_cards_table():
    sql = 'CREATE TABLE cards(front_side, back_side, languages);'
    with db_engine.connect() as conn:
        conn.execute(sql)
