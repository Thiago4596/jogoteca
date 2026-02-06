from jogoteca import app
from flask import render_template, request, redirect, url_for, flash, session
from models import Usuarios, db
from helpers import FormularioUsuario, CriarUsuario
from flask_bcrypt import check_password_hash, generate_password_hash


@app.route('/cadastro')
def cadastro():
    proxima = request.args.get('proxima')
    form = CriarUsuario()
    return render_template('cadastro.html', proxima=proxima, form=form)

@app.route('/criar_usuario', methods=['POST',])
def criar_usuario():
    form = CriarUsuario(request.form)
    usuario = Usuarios.query.filter_by(nickname=form.nickname.data).first()

    if usuario:
        flash('Usuário já existe.')
        return redirect(url_for('cadastro'))

    senha_criptografada = generate_password_hash(form.senha.data).decode('utf-8')
    novo_usuario = Usuarios(nome=form.nome.data, nickname=form.nickname.data, senha=senha_criptografada)
    db.session.add(novo_usuario)
    db.session.commit()
    flash('Usuário criado com sucesso!')
    proxima_pagina = request.form['proxima']
    return redirect(proxima_pagina)

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    form = FormularioUsuario()
    return render_template('login.html', proxima=proxima, form=form)

@app.route('/autenticar', methods=['POST',])
def autenticar():
    form = FormularioUsuario(request.form)
    usuario = Usuarios.query.filter_by(nickname=form.nickname.data).first()
    senha = check_password_hash(usuario.senha, form.senha.data)

    if usuario and senha:
        session['usuario_logado'] = usuario.nickname
        flash(usuario.nickname + ' logado com sucesso!')
        proxima_pagina = request.form['proxima']
        return redirect(proxima_pagina)
    else:
        flash('Usuário não logado.')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('index'))
