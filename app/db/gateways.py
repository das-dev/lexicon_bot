class DataTableGateway(object):
    _query_table = {}

    def __init__(self, engine):
        self.engine = engine

    def find_all(self):
        with self.engine.connect() as conn:
            return list(conn.execute(self._query_table['select_all_query']))

    def insert_one(self, **card):
        card['pk'] = card.get('pk')
        with self.engine.connect() as conn:
            conn.execute(self._query_table['insert_one_query'], card)

    def insert_many(self, cards):
        with self.engine.connect() as conn:
            conn.executemany(self._query_table['insert_many_query'], cards)

    def delete(self):
        ...  # TODO: to implement

    def update(self):
        ...  # TODO: to implement


class CardsTableGateway(DataTableGateway):
    _query_table = {
        'insert_one_query': 'INSERT INTO cards VALUES (:pk, :front_side, :back_side, :languages);',
        'select_all_query': 'SELECT * FROM cards;',
        'select_by_langs_query': 'SELECT * FROM cards WHERE "languages"=?;',
    }

    def find_by_lang(self, langs):
        with self.engine.connect() as conn:
            return list(conn.execute(self._query_table['select_by_langs_query'], (langs, )))


class UserTableGateway(DataTableGateway):
    _query_table = {
        'insert_one_query': 'INSERT INTO users VALUES (:pk, :user_id);',
        'select_all_query': 'SELECT * FROM users;',
        'select_by_user_id_query': 'SELECT * FROM users WHERE "user_id"=?;',
    }

    def find_by_user_id(self, user_id):
        with self.engine.connect() as conn:
            return list(conn.execute(self._query_table['select_by_user_id_query'], (user_id, )))
