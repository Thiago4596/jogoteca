import psycopg2
from flask_bcrypt import generate_password_hash
from urllib.parse import quote_plus

# 1. Configurações de Conexão (Substitua pelos seus dados)
senha_db = quote_plus('3570@Supa@3570') # Escapando o @ da senha
user_db = 'postgres.xwsbcqcyvvgvttdkeqrf'
host_db = 'aws-1-us-east-2.pooler.supabase.com'
port_db = '6543'
database_name = 'postgres'

print("Conectando ao Supabase...")
try:
    conn = psycopg2.connect(
        host=host_db,
        user=user_db,
        password='3570@Supa@3570', # Aqui no connect pode usar a senha real
        port=port_db,
        database=database_name
    )
    cursor = conn.cursor()
except Exception as err:
    print(f'Erro ao conectar: {err}')
    exit()

# 2. Resetando Tabelas
# No Postgres (Supabase), não usamos "CREATE DATABASE", trabalhamos dentro do banco 'postgres'
print("Limpando tabelas antigas...")
cursor.execute("DROP TABLE IF EXISTS jogos;")
cursor.execute("DROP TABLE IF EXISTS usuarios;")

# 3. Criando Tabelas (Sintaxe Postgres)
# Nota: AUTO_INCREMENT vira SERIAL no Postgres
TABLES = {}
TABLES['Jogos'] = ('''
    CREATE TABLE jogos (
        id SERIAL PRIMARY KEY,
        nome VARCHAR(50) NOT NULL,
        categoria VARCHAR(40) NOT NULL,
        console VARCHAR(20) NOT NULL
    );''')

TABLES['Usuarios'] = ('''
    CREATE TABLE usuarios (
        nome VARCHAR(20) NOT NULL,
        nickname VARCHAR(8) NOT NULL PRIMARY KEY,
        senha VARCHAR(100) NOT NULL
    );''')

for tabela_nome in TABLES:
    try:
        print(f'Criando tabela {tabela_nome}:', end=' ')
        cursor.execute(TABLES[tabela_nome])
        print('OK')
    except Exception as err:
        print(f'Erro: {err}')

# 4. Inserindo Usuários
# No Postgres, o placeholder é %s (igual ao MySQL no psycopg2)
usuario_sql = 'INSERT INTO usuarios (nome, nickname, senha) VALUES (%s, %s, %s)'
usuarios = [
    ("Bruno Divino", "BD", generate_password_hash("alohomora").decode('utf-8')),
    ("Camila Ferreira", "Mila", generate_password_hash("paozinho").decode('utf-8')),
    ("Guilherme Louro", "Cake", generate_password_hash("python_eh_vida").decode('utf-8'))
]
cursor.executemany(usuario_sql, usuarios)

# 5. Inserindo Jogos
jogos_sql = 'INSERT INTO jogos (nome, categoria, console) VALUES (%s, %s, %s)'
jogos = [
    ('Tetris', 'Puzzle', 'Atari'),
    ('God of War', 'Hack n Slash', 'PS2'),
    ('Mortal Kombat', 'Luta', 'PS2'),
    ('Valorant', 'FPS', 'PC'),
    ('Crash Bandicoot', 'Hack n Slash', 'PS2'),
    ('Need for Speed', 'Corrida', 'PS2'),
]
cursor.executemany(jogos_sql, jogos)

# 6. Verificando Dados
print('\n-------------  Usuários Cadastrados:  -------------')
cursor.execute('SELECT nickname FROM usuarios')
for user in cursor.fetchall():
    print(user[0])

print('\n-------------  Jogos Cadastrados:  -------------')
cursor.execute('SELECT nome FROM jogos')
for jogo in cursor.fetchall():
    print(jogo[0])

# Commit e Fechamento
conn.commit()
cursor.close()
conn.close()
print("\nBanco de dados preparado com sucesso no Supabase!")