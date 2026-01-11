import psycopg2
from psycopg2.extras import RealDictCursor

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="inventory_db",
        user="postgres",
        password="root",
        port=8080 # Change only if your DB uses another port
    )

def execute_query(query, params=None, fetchone=False):
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(query, params)
            if fetchone:
                result = cur.fetchone()
                conn.commit()
                return result
            conn.commit()
    finally:
        conn.close()

def fetch_query(query, params=None):
    conn = get_connection()
    try:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(query, params)
            return cur.fetchall()
    finally:
        conn.close()
