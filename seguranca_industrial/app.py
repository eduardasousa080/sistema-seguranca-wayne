from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'

# Função para inicializar o banco de dados
def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # Verificar se a tabela 'users' existe e se a coluna 'email' já existe
    cursor.execute("PRAGMA table_info(users)")
    columns = [column[1] for column in cursor.fetchall()]
    
    if 'email' not in columns:
        cursor.execute("DROP TABLE IF EXISTS users")  # Exclui a tabela se existir
        cursor.execute('''CREATE TABLE users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                role TEXT NOT NULL
            )''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS resources (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            type TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            description TEXT
        )''')
    conn.commit()
    conn.close()

init_db()  # Chama a função para criar o banco de dados e as tabelas

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Verifica se o usuário existe no banco de dados
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE email = ? AND password = ?', (email, password))
        user = cursor.fetchone()
        conn.close()

        if user:
            return redirect(url_for('dashboard'))  # Redireciona para o dashboard
        else:
            flash('Usuário ou senha inválidos!', 'error')
            return render_template('login.html')

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        role = request.form['role']

        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()

        try:
            cursor.execute('INSERT INTO users (username, email, password, role) VALUES (?, ?, ?, ?)', (username, email, password, role))
            conn.commit()
            flash('Registro realizado com sucesso! Verifique seu email para confirmação.')
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash('Usuário ou email já existe!', 'error')
        finally:
            conn.close()
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    # Obter todos os recursos para exibir na tabela
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM resources')
    resources = cursor.fetchall()
    conn.close()
    
    return render_template('dashboard.html', resources=resources)

@app.route('/resources', methods=['GET', 'POST'])
def resources_management():
    conn = sqlite3.connect('users.db')  # Conectar ao banco de dados correto
    cursor = conn.cursor()

    # Processar a ação de adicionar um novo recurso
    if request.method == 'POST':
        action = request.form.get('action')

        if action == 'add':
            resource_name = request.form['resource_name']
            resource_type = request.form['resource_type']
            resource_quantity = request.form['resource_quantity']
            resource_description = request.form['resource_description']
            cursor.execute('INSERT INTO resources (name, type, quantity, description) VALUES (?, ?, ?, ?)',
                           (resource_name, resource_type, resource_quantity, resource_description))
            conn.commit()
            flash('Recurso adicionado com sucesso!')

        elif action == 'remove':
            resource_id = request.form['resource_id']
            cursor.execute('DELETE FROM resources WHERE id = ?', (resource_id,))
            conn.commit()
            flash('Recurso removido com sucesso!')

        elif action == 'update':
            resource_id = request.form['resource_id']
            resource_type = request.form['resource_type']
            resource_quantity = request.form['resource_quantity']
            resource_description = request.form['resource_description']
            cursor.execute('UPDATE resources SET type = ?, quantity = ?, description = ? WHERE id = ?',
                           (resource_type, resource_quantity, resource_description, resource_id))
            conn.commit()
            flash('Recurso atualizado com sucesso!')

    # Obter todos os recursos para exibir na tabela
    cursor.execute('SELECT * FROM resources')
    resources = cursor.fetchall()
    conn.close()

    return render_template('resources.html', resources=resources)

@app.route('/resource_chart')
def resource_chart():
    # Obter todos os recursos agrupados pelo nome e somar suas quantidades
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # Obter recursos por nome
    cursor.execute('SELECT name, SUM(quantity) FROM resources GROUP BY name')
    resources = cursor.fetchall()

    # Obter tipos de recursos
    cursor.execute('SELECT type, SUM(quantity) FROM resources GROUP BY type')
    resource_types = cursor.fetchall()

    # Obter descrições de recursos
    cursor.execute('SELECT description, SUM(quantity) FROM resources GROUP BY description')
    resource_descriptions = cursor.fetchall()
    
    conn.close()

    return render_template('resource_chart.html', resources=resources, resource_types=resource_types, resource_descriptions=resource_descriptions)

if __name__ == '__main__':
    app.run(debug=True)
