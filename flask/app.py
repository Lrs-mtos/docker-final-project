from flask import Flask
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(host=os.getenv('DATABASE_HOST'),
                            dbname=os.getenv('DATABASE_NAME'),
                            user=os.getenv('DATABASE_USER'),
                            password=os.getenv('DATABASE_PASSWORD'))
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM exemplo;')
    exemplo_data = cur.fetchall()
    cur.close()
    conn.close()
    
    # Construindo uma lista HTML para visualização no navegador
    items = '<br>'.join([f"{row[0]}, {row[1]}, {row[2]}, {row[3]}" for row in exemplo_data])
    return f"<html><body>{items}</body></html>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
