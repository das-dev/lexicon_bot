import settings
from app.db.engine import create_engine
from app.db.gateways import CardsTableGateway

db_engine = create_engine(settings.DATABASES['main']['DSN'])


def add_card(card_data):
    CardsTableGateway(db_engine).insert_one(**card_data)


def fetch_all_cards():
    return CardsTableGateway(db_engine).find_all()
