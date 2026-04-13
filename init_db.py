from app import get_db_connection

def init_db():
    conn = get_db_connection()
    with open('schema.sql') as f:
        conn.executescript(f.read())
    conn.close()

if __name__ == '__main__':
    init_db()
