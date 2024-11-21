import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'costumers'


connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.execute(
    f'DELETE FROM {TABLE_NAME} '
)
cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
)
connection.commit()

cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'   
    ')'
)
connection.commit()

sql = (
    f'INSERT INTO {TABLE_NAME} '
    '(name, weight) '
    'VALUES '
    '(:nome, :peso)'
)
cursor.execute(sql, {'nome': 'Marcelo', 'peso': 81.00})
cursor.executemany(sql, (
    {'nome': 'Ana', 'peso': 68},
    {'nome': 'Maria', 'peso': 65},
    {'nome': 'Helena', 'peso': 82},
    {'nome': 'Joana', 'peso': 86},
))
connection.commit()
if __name__ == '__main__':
    print(sql)

cursor.close()
connection.close()
