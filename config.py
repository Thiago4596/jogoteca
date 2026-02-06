# config.py
import os
from urllib.parse import quote_plus
from dotenv import load_dotenv

# Carrega variáveis de ambiente (se houver arquivo .env)
load_dotenv()

# --- 1. VARIÁVEIS DE CONFIGURAÇÃO ---

# Chave secreta (agora é uma variável direta, não app.config)
SECRET_KEY = str(os.getenv('SECRET_KEY'))

# Dados de conexão
usuario = str(os.getenv('USER'))
senha = str(os.getenv('DB_PASSWORD'))
servidor = str(os.getenv('SERVER'))
porta = str(os.getenv('DOOR'))
banco = str(os.getenv('BANK'))

# Tratamento da senha para URL
senha_safe = quote_plus(senha)

# A URI de conexão (o Flask procura pelo nome exato 'SQLALCHEMY_DATABASE_URI')
SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://{usuario}:{senha_safe}@{servidor}:{porta}/{banco}"

# Opções do Engine
SQLALCHEMY_ENGINE_OPTIONS = {
    "connect_args": {
        "sslmode": "require"
    }
}

SQLALCHEMY_TRACK_MODIFICATIONS = False

# Caminho de upload (opcional, se o jogoteca.py usar)
UPLOAD_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uploads')