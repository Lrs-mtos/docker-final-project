from flask import Flask, request, redirect
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(host=os.getenv('DATABASE_HOST'),
                            dbname=os.getenv('DATABASE_NAME'),
                            user=os.getenv('DATABASE_USER'),
                            password=os.getenv('DATABASE_PASSWORD'))
    return conn


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Processa os dados enviados pelo formulário
        nome = request.form['nome']
        descricao = request.form['descricao']
        # Assume-se que data_criacao é automaticamente definida pelo banco de dados
        
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO exemplo (nome, descricao) VALUES (%s, %s)", (nome, descricao))
        conn.commit()
        cur.close()
        conn.close()
        return redirect('/')
    
    # Se não for um POST, mostra os registros existentes e o formulário
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM exemplo;')
    exemplo_data = cur.fetchall()
    cur.close()
    conn.close()
    
    items = '<br>'.join([f"{row[0]}, {row[1]}, {row[2]}, {row[3]}" for row in exemplo_data])
    form = '''
        <form method="post">
            Nome:<br>
            <input type="text" name="nome"><br>
            Descrição:<br>
            <input type="text" name="descricao"><br>
            <input type="submit" value="Adicionar Item">
        </form>
    '''
    return f"<html><body>{form}{items}</body></html>"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
