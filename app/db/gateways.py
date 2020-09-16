class DataTableGateway(object):
    _query_table = {}

    def __init__(self, engine):
        self.engine = engine

    def find_all(self):
        with self.engine.connect() as conn:
            return list(conn.execute(self._query_table['select_all_query']))

    def insert_one(self, **card):
        with self.engine.connect() as conn:
            conn.execute(self._query_table['insert_query'], card)

    def insert_many(self, cards):
        with self.engine.connect() as conn:
            conn.executemany(self._query_table['insert_query'], cards)

    def delete(self):
        ...  # TODO: to implement

    def update(self):
        ...  # TODO: to implement


class CardsTableGateway(DataTableGateway):
    _query_table = {
        'insert_query': 'INSERT INTO cards VALUES (:front_side, :back_side, :languages);',
        'select_all_query': 'SELECT * FROM cards;',
        'select_by_langs_query': 'SELECT * FROM cards WHERE "languages"=?;',
    }

    def find_by_lang(self, langs):
        with self.engine.connect() as conn:
            return list(conn.execute(self._query_table['select_by_langs_query'], (langs, )))
