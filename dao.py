from models import Serie, Filme, Usuario, Studio, Genero

# Cria
SQL_CRIA_SERIE = 'INSERT into SERIE (NOME, EPS, TEMPS, NOTA, SINOPSE, STUDIO_ID, GENERO_ID, ANO) values (%s, %s, %s, %s, %s, %s, %s, %s)'
SQL_CRIA_FILME = 'INSERT into MOVIE (NOME, DURATION, SINOPSE, NOTA, ANO, STUDIO_ID, GENERO_ID) values (%s, %s, %s, %s, %s, %s, %s)'
SQL_CRIA_STUDIO = 'INSERT into STUDIO (NOME) values (%s)'
SQL_CRIA_GENERO = 'INSERT into GENERO (NOME) values (%s)'
SQL_CRIA_USUARIO = 'INSERT into USUARIO (NOME, EMAIL, SENHA) values (%s, %s, %s)'

# Atualiza
SQL_ATUALIZA_SERIE = 'UPDATE SERIE SET NOME = %s, EPS = %s, TEMPS = %s, NOTA = %s, SINOPSE = %s, STUDIO_ID = %s, GENERO_ID = %s, ANO = %s where ID = %s'
SQL_ATUALIZA_FILME = 'UPDATE MOVIE SET NOME = %s, DURATION = %s, SINOPSE = %s, NOTA = %s, ANO = %s, STUDIO_ID = %s, GENERO_ID = %s where ID = %s'
SQL_ATUALIZA_STUDIO = 'UPDATE STUDIO SET NOME = %s where ID = %s'
SQL_ATUALIZA_GENERO = 'UPDATE GENERO SET NOME = %s where ID = %s'
SQL_ATUALIZA_USUARIO = 'UPDATE USUARIO SET NOME = %s, EMAIL = %s, SENHA = %s where ID = %s'

# ID
SQL_BUSCA_SERIE = 'SELECT ID, NOME, EPS, TEMPS, NOTA, SINOPSE, STUDIO_ID, GENERO_ID, ANO from SERIE'
SQL_BUSCA_FILME = 'SELECT ID, NOME, DURATION, SINOPSE, NOTA, ANO, STUDIO_ID, GENERO_ID, ANO from MOVIE'
SQL_BUSCA_USUARIO = 'SELECT ID, NOME, EMAIL, SENHA from USUARIO'
SQL_BUSCA_STUDIO = 'SELECT ID, NOME from STUDIO'
SQL_BUSCA_GENERO = 'SELECT ID, NOME from GENERO'


SQL_STUDIO_POR_ID = 'SELECT ID, NOME from STUDIO where ID = %s'
SQL_GENERO_POR_ID = 'SELECT ID, NOME from GENERO where ID = %s'
SQL_SERIE_POR_ID = 'SELECT ID, NOME, EPS, TEMPS, NOTA, SINOPSE, STUDIO_ID, GENERO_ID, ANO from SERIE where ID = %s'
SQL_FILME_POR_ID = 'SELECT ID, NOME, DURATION, SINOPSE, NOTA, ANO, STUDIO_ID, GENERO_ID, ANO from MOVIE where ID = %s'
SQL_USUARIO_POR_ID = 'SELECT ID, NOME, EMAIL, SENHA from USUARIO where ID = %s'

# Delete
SQL_DELETA_SERIE = 'delete from SERIE where ID = %s'
SQL_DELETA_FILME = 'delete from MOVIE where ID = %s'
SQL_DELETA_GENERO = 'delete from GENERO where ID = %s'
SQL_DELETA_STUDIO = 'delete from STUDIO where ID = %s'


class SerieDao:
    def __init__(self, db):
        self.__db = db

    def salvar(self, serie):
        cursor = self.__db.connection.cursor()

        if (serie._id):
            cursor.execute(SQL_ATUALIZA_SERIE, (serie._nome, serie._eps, serie._temps, serie._nota, serie._sinopse, serie._estudio_id, serie._genero_id, serie._ano, serie._id))
            
        else:
            cursor.execute(SQL_CRIA_SERIE, (serie._nome, serie._eps, serie._temps, serie._nota, serie._sinopse, serie._estudio_id, serie._genero_id, serie._ano))
            cursor._id = cursor.lastrowid
            serie._id = cursor._id

        self.__db.connection.commit()
        return serie

    def listar(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_SERIE)
        series = traduz_series(cursor.fetchall())
        return series

    def busca_por_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_SERIE_POR_ID, (id,))
        tupla = cursor.fetchone()
        return Serie(tupla[1], tupla[2], tupla[3], tupla[4], tupla[5], tupla[6], tupla[7], tupla[8], id=tupla[0])

    def deletar(self, id):
        self.__db.connection.cursor().execute(SQL_DELETA_SERIE, (id,))
        self.__db.connection.commit()


def traduz_series(series):
    def cria_series_com_tupla(tupla):
        return Serie(tupla[1], tupla[2], tupla[3], tupla[4], tupla[5], tupla[6], tupla[7], tupla[8], id=tupla[0])
    return list(map(cria_series_com_tupla, series))


def traduz_filmes(filmes):
    def cria_filmes_com_tupla(tupla):
        return Filme(tupla[1], tupla[2], tupla[3], tupla[4], tupla[5], tupla[6], tupla[7], id=tupla[0])
    return list(map(cria_filmes_com_tupla, filmes))


def traduz_usuario(tupla):
    return Usuario(tupla[0], tupla[1], tupla[2])


def traduz_estudio(studios):
    def cria_studios_com_tupla(tupla):
        return Studio(tupla[1], tupla[0])
    return list(map(cria_studios_com_tupla, studios))


def traduz_genero(generos):
    def cria_generos_com_tupla(tupla):
        return Genero(tupla[1], tupla[0])
    return list(map(cria_generos_com_tupla, generos))


class FilmeDao:
    def __init__(self, db):
        self.__db = db

    def salvar_filme(self, filme):
        cursor = self.__db.connection.cursor()

        if (filme._id):
            cursor.execute(SQL_ATUALIZA_FILME, (filme._nome, filme._duracao, filme._sinopse, filme._nota, filme._ano, filme._estudio_id, filme._genero_id, filme._id))

        else:
            cursor.execute(SQL_CRIA_FILME, (filme._nome, filme._duracao, filme._sinopse, filme._nota, filme._ano, filme._estudio_id, filme._genero_id))
            cursor._id = cursor.lastrowid
            filme._id = cursor._id

        self.__db.connection.commit()
        return filme

    def listar_filmes(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_FILME)
        filmes = traduz_filmes(cursor.fetchall())
        return filmes

    def busca_filme_por_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_FILME_POR_ID, (id,))
        tupla = cursor.fetchone()
        return Filme(tupla[1], tupla[2], tupla[3], tupla[4], tupla[5], tupla[6], tupla[7], id=tupla[0])

    def deletar_filme(self, id):
        self.__db.connection.cursor().execute(SQL_DELETA_FILME, (id,))
        self.__db.connection.commit()


class StudioDao:
    def __init__(self, db):
        self.__db = db

    def salvar_estudio(self, studio):
        cursor = self.__db.connection.cursor()

        if (studio._id):
            cursor.execute(SQL_ATUALIZA_STUDIO, (studio._nome, studio._id))

        else:
            cursor.execute(SQL_CRIA_STUDIO, [studio._nome])
            cursor._id = cursor.lastrowid

        self.__db.connection.commit()
        return studio

    def listar_estudio(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_STUDIO)
        studios = traduz_estudio(cursor.fetchall())
        return studios


class UsuarioDao:
    def __init__(self, db):
        self.__db = db

    def cria_conta(self, usuario):
        cursor = self.__db.connection.cursor()

        if (usuario._id):
            cursor.execute(SQL_ATUALIZA_USUARIO, (usuario._nome, usuario._email, usuario._senha, usuario._id))

        else:
            cursor.execute(SQL_CRIA_USUARIO, (usuario._nome, usuario._email, usuario._senha))
            cursor._id = cursor.lastrowid

        self.__db.connection.commit()
        return usuario

    def busca_por_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_USUARIO_POR_ID, (id,))
        dados = cursor.fetchone()
        usuario = traduz_usuario(dados) if dados else None
        return usuario


class GeneroDao:
    def __init__(self, db):
        self.__db = db

    def criar_genero(self, genero):
        cursor = self.__db.connection.cursor()

        if (genero._id):
            cursor.execute(SQL_ATUALIZA_GENERO, (genero._nome, genero._id))

        else:
            cursor.execute(SQL_CRIA_GENERO, [genero._nome])
            cursor._id = cursor.lastrowid

        self.__db.connection.commit()
        return genero
    
    def listar_genero(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_GENERO)
        generos = traduz_genero(cursor.fetchall())
        return generos