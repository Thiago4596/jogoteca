import os
from jogoteca import app
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, validators

class CriarUsuario(FlaskForm):
    nickname = StringField('Nickname', [validators.DataRequired(), validators.Length(min=1, max=8)])
    nome = StringField('Nome Completo', [validators.DataRequired(), validators.Length(min=1, max=20)])
    senha = PasswordField('Senha', [validators.DataRequired(), validators.Length(min=1, max=100)])
    criar = SubmitField('Criar')

class FormularioJogo(FlaskForm):
    nome = StringField('Nome do Jogo', [validators.DataRequired(), validators.Length(min=1, max=50)])
    categoria = StringField('Categoria', [validators.DataRequired(), validators.Length(min=1, max=40)])
    console = StringField('Console', [validators.DataRequired(), validators.Length(min=1, max=20)])
    salvar = SubmitField('Salvar')

class FormularioUsuario(FlaskForm):
    nickname = StringField('Nickname', [validators.DataRequired(), validators.Length(min=1, max=8)])
    senha = PasswordField('Senha', [validators.DataRequired(), validators.Length(min=1, max=100)])
    login = SubmitField('Login')

def recupera_imagem(id):
    # Define o prefixo que esperamos encontrar no começo do nome
    prefixo = f'capa{id}'
    
    for nome_arquivo in os.listdir(app.config['UPLOAD_PATH']):
        
        # 1. Verifica o novo formato com timestamp: "capa2-123456.jpg"
        if nome_arquivo.startswith(f'{prefixo}-'):
            return nome_arquivo
            
        # 2. Verifica o formato antigo (caso ainda tenha imagens assim): "capa2.jpg"
        # O ponto depois do ID garante que não confunda capa2 com capa20
        if nome_arquivo.startswith(f'{prefixo}.'):
            return nome_arquivo

    # Se não achar nada, retorna a padrão
    return 'capa_padrao.jpg'

def deleta_arquivo(id):
    arquivo = recupera_imagem(id)
    if arquivo != 'capa_padrao.jpg':
        os.remove(os.path.join(app.config['UPLOAD_PATH'], arquivo))

