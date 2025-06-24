import sqlite3 as sql
from config import DB

def request_query(query,paramaters=()):
    with sql.connect(DB) as conn :
        cursor = conn.cursor()
        date = cursor.execute(query,paramaters)
        conn.commit()
    return date


def create_tables():
    pass