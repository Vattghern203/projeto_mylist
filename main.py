from flask import Flask, render_template, flash, url_for, request, session, send_from_directory, redirect

from dao import UsuarioDao, FilmeDao, SerieDao, StudioDao, GeneroDao

from flask_mysqldb import MySQL

from models import Serie, Filme, Usuario, Studio, Genero

import os

app = Flask(__name__)
app.secret_key = 'Mylist'

app.config['UPLOAD_PATH'] = os.path.dirname(os.path.abspath(__file__))+'/uploads'
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'admin'
app.config['MYSQL_DB'] = 'mylista'
app.config['MYSQL_PORT'] = 3306

db = MySQL(app)

# Variáveis Dao
usuario_dao = UsuarioDao(db)
serie_dao = SerieDao(db)
filme_dao = FilmeDao(db)
estudio_dao = StudioDao(db)
genero_dao = GeneroDao(db)


# paginas
@app.route('/')
def index():
    lista = serie_dao.listar()
    listaf = filme_dao.listar_filmes()
    
    return render_template('index.html', series=lista, filmes=listaf)


# Login / Autenticar / ID
@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    u_id = request.args.get('u_id')
    if proxima == None:
        proxima = ''
    if u_id == None:
        u_id = ''
    return render_template('login.html', proxima=proxima)


@app.route('/autenticar', methods=['POST', ])
def autenticar():
    usuario = usuario_dao.busca_por_nome(request.form['usuario'])
    print(usuario._id)
    if usuario:
        if usuario._senha == request.form['senha']:
            session['usuario_logado'] = usuario._id
            flash(request.form['usuario'] + ' logou com sucesso!')
            proxima_pagina = request.form['proxima']
            if proxima_pagina == '':
                return redirect('/')
            else:
                return redirect('/'.format(proxima_pagina))

    flash('Erro ao logar! Tente novamente.')
    return redirect('/login')


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Nenhum usuário logado')
    return redirect('/login')


# Atualizar
@app.route('/atualizar', methods=['POST', ])
def atualizar():
    nome = request.form['nome']
    eps = request.form['eps']
    temps = request.form['temps']
    nota = request.form['nota']
    sinopse = request.form['sinopse']
    estudio_id = request.form['studio']
    genero_id = request.form['genero']
    ano = request.form['ano']
    id = request.form['id']

    serie = Serie(nome, eps, temps, nota, sinopse, estudio_id, genero_id, ano, id)
    
    arquivo = request.files['arquivo']
    
    if arquivo:
        upload_path = app.config['UPLOAD_PATH']
        arquivo.save(f'{upload_path}/capa_serie{serie._id}.jpg')

    serie_dao.salvar(serie)
    return redirect('/tabela')


@app.route('/atualizar_filme', methods=['POST', ])
def atualizar_filme():
    nomef = request.form['nome-f']
    duracao = request.form['duracao']
    notaf = request.form['nota-f']
    anof = request.form['ano-f']
    sinopsef = request.form['sinopse-f']
    studiof = request.form['studio-f']
    generof = request.form['genero-f']
    id = request.form['id']

    filme = Filme(nomef, duracao, sinopsef, notaf, anof, generof, studiof, id)
    
    arquivo = request.files['arquivo']
    
    if arquivo:
        upload_path = app.config['UPLOAD_PATH']
        arquivo.save(f'{upload_path}/capa_filme{filme._id}.jpg')
        
    filme_dao.salvar_filme(filme)

    return redirect('/tabela_filmes')


# Criar
@app.route('/criar', methods=['POST', ])
def criar():
    nome = request.form['nome']
    eps = request.form['eps']
    temps = request.form['temps']
    nota = request.form['nota']
    sinopse = request.form['sinopse']
    estudio_id = request.form['studio']
    genero_id = request.form['genero']
    ano = request.form['ano']

    serie = Serie(nome, eps, temps, nota, sinopse, estudio_id, genero_id, ano)
    
    serie = serie_dao.salvar(serie)
    
    arquivo = request.files['arquivo']
    upload_path = app.config['UPLOAD_PATH']
    arquivo.save(f'{upload_path}/capa_serie{serie._id}.jpg')
    
    return redirect('/novo')


@app.route('/criar_filme', methods=['POST', ])
def criar_filme():
    nomef = request.form['nome-f']
    duracao = request.form['duracao']
    notaf = request.form['nota-f']
    anof = request.form['ano-f']
    sinopsef = request.form['sinopse-f']
    studiof = request.form['studio-f']
    generof = request.form['genero-f']

    filme = Filme(nomef, duracao, sinopsef, notaf, anof, generof, studiof)
    
    filme = filme_dao.salvar_filme(filme)
    
    arquivo = request.files['arquivo']
    upload_path = app.config['UPLOAD_PATH']
    arquivo.save(f'{upload_path}/capa_filme{filme._id}.jpg')

    return redirect('/novo_filme')


@app.route('/criar_conta', methods=['POST', ])
def criar_conta():
    nomeu = request.form['nome_usuario']
    email = request.form['email']
    senha = request.form['senha']

    usuario = Usuario(nomeu, email, senha)

    usuario_dao.cria_conta(usuario)
    return redirect('/login')


@app.route('/criar_estudio', methods=['POST', ])
def criar_estudio():
    nomee = request.form['nome-e']

    studio = Studio(nomee)

    estudio_dao.salvar_estudio(studio)
    return redirect('/novo_estudio')


@app.route('/criar_genero', methods=['POST', ])
def criar_genero():
    nomeg = request.form['nome']

    genero = Genero(nomeg)

    genero_dao.criar_genero(genero)
    return redirect('/novo_genero')


# Novo
@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login?proxima=novo')
    lista = estudio_dao.listar_estudio()
    lista_genero = genero_dao.listar_genero()
    return render_template('criar.html', studios=lista, generos=lista_genero)


@app.route('/novo_filme')
def novo_filme():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login?proxima=novo_filme')
    lista = estudio_dao.listar_estudio()
    lista_genero = genero_dao.listar_genero()
    return render_template('criar_filme.html', studios=lista, generos=lista_genero)


@app.route('/nova_conta')
def nova_conta():
    return render_template('criar_conta.html')


@app.route('/novo_estudio')
def novo_estudio():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login?proxima=novo_estudio')
    return render_template('criar_estudio.html')


@app.route('/novo_genero')
def novo_genero():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login?proxima=novo_genero')
    return render_template('criar_genero.html')


# Editar
@app.route('/editar/<int:id>')
def editar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login?proxima=editar')
    if 'usuario_logado' in session:
        usuario = usuario_dao.busca_por_id(session['usuario_logado'])
        print(usuario)
    serie = serie_dao.busca_por_id(id)
    return render_template('editar.html', titulo='Editando uma serie', serie=serie, capa_serie=f'capa_serie{id}.jpg', usuario=usuario)


@app.route('/editar_filme/<int:id>')
def editar_filme(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login?proxima=editar_filme')
    filme = filme_dao.busca_filme_por_id(id)
    return render_template('editar_filme.html', filme=filme, capa_filme=f'capa_filme{id}.jpg')


# Info
@app.route('/serie_info')
def serie_perfil():
    return render_template('template.html')


# Deletar
@app.route('/deletar/<int:id>')
def deletar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login?proxima=index')
    serie_dao.deletar(id)
    arquivo = f'capa_serie{id}.jpg'
    os.remove(os.path.join(app.config['UPLOAD_PATH'], arquivo))
    return redirect(url_for('tabela'))


@app.route('/deletar_filme/<int:id>')
def deletar_filme(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login?proxima=index')
    filme_dao.deletar_filme(id)
    arquivo = f'capa_filme{id}.jpg'
    os.remove(os.path.join(app.config['UPLOAD_PATH'], arquivo))
    return redirect(url_for('tabela_filmes'))


# Apagar Depois
@app.route('/extendido')
def extendido():
    return render_template('extendido.html')


@app.route('/teste')
def teste():
    return render_template('testeteste.html')


# Info
@app.route('/serie_info/<int:id>')
def serie_info(id):
    serie = serie_dao.busca_por_id(id)
    return render_template('serie_info.html', serie=serie, capa_serie=f'capa_serie{id}.jpg')


@app.route('/filme_info/<int:id>')
def filme_info(id):
    filme = filme_dao.busca_filme_por_id(id)
    return render_template('filme_info.html', filme=filme, capa_filme=f'capa_filme{id}.jpg')


# Tabelas/listas
@app.route('/tabela')
def tabela():
    lista = serie_dao.listar()
    return render_template('tabela_serie.html', series=lista)


@app.route('/tabela_filmes')
def tabela_filmes():
    lista = filme_dao.listar_filmes()
    return render_template('tabela_filmes.html', filmes=lista)


@app.route('/uploads/<nome_arquivo>')
def imagem(nome_arquivo):
    return send_from_directory('uploads', nome_arquivo)


# Main
if __name__ == '__main__':
    app.run(debug=True)
