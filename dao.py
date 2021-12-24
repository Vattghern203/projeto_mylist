from models import Serie, Filme, Usuario, Studio, Genero, SerieList, MovieList

# Cria
SQL_CRIA_SERIE = 'INSERT into SERIE (NOME, EPS, TEMPS, SINOPSE, NOTA, ANO, STUDIO_ID, GENERO_ID) values (%s, %s, %s, %s, %s, %s, %s, %s)'
SQL_CRIA_FILME = 'INSERT into MOVIE (NOME, DURATION, SINOPSE, NOTA, STUDIO_ID, GENERO_ID, ANO) values (%s, %s, %s, %s, %s, %s, %s)'
SQL_CRIA_STUDIO = 'INSERT into STUDIO (NOME) values (%s)'
SQL_CRIA_GENERO = 'INSERT into GENERO (NOME) values (%s)'
SQL_CRIA_USUARIO = 'INSERT into USUARIO (NOME, EMAIL, SENHA) values (%s, %s, %s)'
SQL_ADD_LIST_SERIE = 'INSERT into SERIE_LIST (USUARIO_ID, SERIE_ID) values (%s, %s)'
SQL_ADD_LIST_MOVIE = 'INSERT into MOVIE_LIST (USUARIO_ID, MOVIE_ID) values (%s, %s)'

# Atualiza
SQL_ATUALIZA_SERIE = 'UPDATE SERIE SET NOME = %s, EPS = %s, TEMPS = %s,  SINOPSE = %s, NOTA = %s, ANO = %s, STUDIO_ID = %s, GENERO_ID = %s where ID = %s'
SQL_ATUALIZA_FILME = 'UPDATE MOVIE SET NOME = %s, DURATION = %s, SINOPSE = %s, NOTA = %s, STUDIO_ID = %s, GENERO_ID = %s, ANO = %s where ID = %s'
SQL_ATUALIZA_STUDIO = 'UPDATE STUDIO SET NOME = %s where ID = %s'
SQL_ATUALIZA_GENERO = 'UPDATE GENERO SET NOME = %s where ID = %s'
SQL_ATUALIZA_USUARIO = 'UPDATE USUARIO SET NOME = %s, EMAIL = %s, SENHA = %s where ID = %s'

# ID
SQL_BUSCA_SERIE = 'SELECT SERIE.ID, SERIE.NOME, SERIE.EPS, SERIE.TEMPS, SERIE.SINOPSE, SERIE.NOTA, SERIE.ANO, SERIE.STUDIO_ID, SERIE.GENERO_ID, STUDIO.NOME, GENERO.NOME FROM SERIE INNER JOIN STUDIO ON SERIE.STUDIO_ID = STUDIO.ID INNER JOIN GENERO ON SERIE.GENERO_ID = GENERO.ID'
SQL_BUSCA_FILME = 'SELECT MOVIE.ID, MOVIE.NOME, MOVIE.DURATION, MOVIE.SINOPSE, MOVIE.NOTA, MOVIE.STUDIO_ID, MOVIE.GENERO_ID, MOVIE.ANO, STUDIO.NOME, GENERO.NOME FROM MOVIE INNER JOIN STUDIO ON MOVIE.STUDIO_ID = STUDIO.ID INNER JOIN GENERO ON MOVIE.GENERO_ID = GENERO.ID'
SQL_BUSCA_USUARIO = 'SELECT ID, NOME, EMAIL, SENHA from USUARIO'
SQL_BUSCA_STUDIO = 'SELECT ID, NOME from STUDIO'
SQL_BUSCA_GENERO = 'SELECT ID, NOME from GENERO'
# Teste
SQL_BUSCA_MINHAS_SERIES = 'SELECT SERIE_ID from SERIE_LIST where USUARIO_ID = %s'
SQL_BUSCA_MEUS_FILMES = 'SELECT MOVIE_ID from MOVIE_LIST where USUARIO_ID = %s'
SQL_BUSCA_FAVORITO = 'SELECT USUARIO_ID, SERIE_ID FROM SERIE_LIST where USUARIO_ID = %s and SERIE_ID = %s'
SQL_BUSCA_FAVORITO_FILME = 'SELECT USUARIO_ID, MOVIE_ID FROM MOVIE_LIST where USUARIO_ID = %s and MOVIE_ID = %s'


SQL_STUDIO_POR_ID = 'SELECT ID, NOME from STUDIO where ID = %s'
SQL_GENERO_POR_ID = 'SELECT ID, NOME from GENERO where ID = %s'
SQL_SERIE_POR_ID = 'SELECT SERIE.ID, SERIE.NOME, SERIE.EPS, SERIE.TEMPS, SERIE.SINOPSE, SERIE.NOTA, SERIE.ANO, SERIE.STUDIO_ID, SERIE.GENERO_ID, STUDIO.NOME, GENERO.NOME FROM SERIE INNER JOIN STUDIO ON SERIE.STUDIO_ID = STUDIO.ID INNER JOIN GENERO ON SERIE.GENERO_ID = GENERO.ID where SERIE.ID = %s'
SQL_FILME_POR_ID = 'SELECT MOVIE.ID, MOVIE.NOME, MOVIE.DURATION, MOVIE.SINOPSE, MOVIE.NOTA, MOVIE.STUDIO_ID, MOVIE.GENERO_ID, MOVIE.ANO, STUDIO.NOME, GENERO.NOME FROM MOVIE INNER JOIN STUDIO ON MOVIE.STUDIO_ID = STUDIO.ID INNER JOIN GENERO ON MOVIE.GENERO_ID = GENERO.ID where MOVIE.ID = %s'
SQL_USUARIO_POR_NOME = 'SELECT ID, NOME, EMAIL, SENHA from USUARIO where NOME = %s'
SQL_USUARIO_POR_ID = 'SELECT ID, NOME, EMAIL, SENHA from USUARIO where ID = %s'

# Delete
# Esse primeiro SQL serve para remover todas as chaves ligadas com a obra que estão no serie.list. Repetir com filmes
SQL_DESFAVORITA_SERIE_ALL = 'delete from SERIE_LIST where SERIE_LIST.SERIE_ID = %s'
SQL_DESFAVORITA_FILME_ALL = 'delete from MOVIE_LIST where MOVIE_LIST.MOVIE_ID = %s'
SQL_DELETA_SERIE = 'delete from SERIE where ID = %s'
SQL_DELETA_FILME = 'delete from MOVIE where ID = %s'
SQL_DELETA_GENERO = 'delete from GENERO where ID = %s'
SQL_DELETA_STUDIO = 'delete from STUDIO where ID = %s'

SQL_REMOVE_LISTA_SERIE = 'delete from SERIE_LIST where USUARIO_ID = %s and SERIE_ID = %s'
SQL_REMOVE_LISTA_FILME = 'delete from MOVIE_LIST where USUARIO_ID = %s and MOVIE_ID = %s'
SQL_MINHAS_SERIES_POR_ID = 'SELECT USUARIO_ID, SERIE_ID from SERIE_LIST'
SQL_MEUS_FILMES_POR_ID = 'SELECT USUARIO_ID, MOVIE_ID from MOVIE_LIST'

class SerieDao:
    def __init__(self, db):
        self.__db = db

    def salvar(self, serie):
        cursor = self.__db.connection.cursor()

        if (serie._id):
            cursor.execute(SQL_ATUALIZA_SERIE, (serie._nome, serie._eps, serie._temps, serie._sinopse, serie._nota,  serie._ano, serie._estudio_id, serie._genero_id, serie._id))
            
        else:
            cursor.execute(SQL_CRIA_SERIE, (serie._nome, serie._eps, serie._temps, serie._sinopse, serie._nota, serie._ano, serie._estudio_id, serie._genero_id))
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
        return Serie(tupla[1], tupla[2], tupla[3], tupla[4], tupla[5], tupla[6], tupla[7], tupla[8], tupla[9], tupla[10], id=tupla[0])

    def deletar(self, id):
        self.__db.connection.cursor().execute(SQL_DELETA_SERIE, (id,))
        self.__db.connection.commit()


def traduz_series(series):
    def cria_series_com_tupla(tupla):
        return Serie(tupla[1], tupla[2], tupla[3], tupla[4], tupla[5], tupla[6], tupla[7], tupla[8], tupla[9], tupla[10], id=tupla[0])
    return list(map(cria_series_com_tupla, series))


def traduz_filmes(filmes):
    def cria_filmes_com_tupla(tupla):
        return Filme(tupla[1], tupla[2], tupla[3], tupla[4], tupla[5], tupla[6], tupla[7], tupla[8], tupla[9], id=tupla[0])
    return list(map(cria_filmes_com_tupla, filmes))


def traduz_usuario(tupla):
    return Usuario(tupla[1], tupla[2], tupla[3], id=tupla[0])


def traduz_estudio(studios):
    def cria_studios_com_tupla(tupla):
        return Studio(tupla[1], tupla[0])
    return list(map(cria_studios_com_tupla, studios))


def traduz_genero(generos):
    def cria_generos_com_tupla(tupla):
        return Genero(tupla[1], tupla[0])
    return list(map(cria_generos_com_tupla, generos))


def traduz_minhas_series(minhas_series):
    def cria_minhas_series_com_tupla(tupla):
        return SerieList(tupla[0], tupla[1])
    return list(map(cria_minhas_series_com_tupla, minhas_series))


def traduz_meus_filmes(meus_filmes):
    def cria_meus_filmes_com_tupla(tupla):
        return MovieList(tupla[0], tupla[1])
    return list(map(cria_meus_filmes_com_tupla, meus_filmes))
    

class FilmeDao:
    def __init__(self, db):
        self.__db = db

    def salvar_filme(self, filme):
        cursor = self.__db.connection.cursor()

        if (filme._id):
            cursor.execute(SQL_ATUALIZA_FILME, (filme._nome, filme._duracao, filme._sinopse, filme._nota, filme._estudio_id, filme._genero_id, filme._ano, filme._id))

        else:
            cursor.execute(SQL_CRIA_FILME, (filme._nome, filme._duracao, filme._sinopse, filme._nota, filme._estudio_id, filme._genero_id, filme._ano))
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
        return Filme(tupla[1], tupla[2], tupla[3], tupla[4], tupla[5], tupla[6], tupla[7], tupla[8], tupla[9], id=tupla[0])

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
        
    def busca_por_nome(self, nome):
        cursor = self.__db.connection.cursor()
        if cursor.execute(SQL_USUARIO_POR_NOME, (nome,)):
            dados = cursor.fetchone()
            usuario = traduz_usuario(dados) if dados else None
            return usuario
        else:
            return None
    
    
    def busca_por_id(self, id):
        cursor = self.__db.connection.cursor()
        if cursor.execute(SQL_USUARIO_POR_ID, (id,)):
            tupla = cursor.fetchone()
            return Usuario(tupla[1], tupla[2], tupla[3], id=tupla[0])
        else:
            return None
    
    def listar_usuarios(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_USUARIO)
        usuarios = traduz_usuario(cursor.fetchall())
        return usuarios
        
    def cria_conta(self, usuario):
        cursor = self.__db.connection.cursor()

        if (usuario._id):
            cursor.execute(SQL_ATUALIZA_USUARIO, (usuario._nome, usuario._email, usuario._senha, usuario._id))

        else:
            cursor.execute(SQL_CRIA_USUARIO, (usuario._nome, usuario._email, usuario._senha))
            cursor._id = cursor.lastrowid

        self.__db.connection.commit()
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
    
    
class SerieListDao:
    def __init__(self, db):
        self.__db = db

    def add_serie(self, lista_serie):
        cursor = self.__db.connection.cursor()
        
        if cursor.execute(SQL_BUSCA_FAVORITO, (lista_serie._usuario_id, lista_serie._serie_id)):
            return lista_serie
        
        cursor.execute(SQL_ADD_LIST_SERIE, (lista_serie._usuario_id,lista_serie._serie_id))
        cursor._id = cursor.lastrowid

        self.__db.connection.commit()
        return lista_serie
    
    def listar_minhas_series(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_MINHAS_SERIES_POR_ID)
        minhas_series = traduz_minhas_series(cursor.fetchall())
        return minhas_series
    
    def desfavorita_serie_all(self, id):
        self.__db.connection.cursor().execute(SQL_DESFAVORITA_SERIE_ALL, (id,))
        self.__db.connection.commit()
        
    def desfavorita_serie_lista(self, usuario_id, serie_id):
        self.__db.connection.cursor().execute(SQL_REMOVE_LISTA_SERIE, (usuario_id, serie_id))
        self.__db.connection.commit()
        
    def busca_favorito_por_id(self, usuario_id, serie_id):
        cursor = self.__db.connection.cursor()
        if cursor.execute(SQL_BUSCA_FAVORITO, (usuario_id, serie_id)):
            tupla = cursor.fetchone()
            return SerieList(tupla[0], tupla[1])
        else:
            return None
    
    
class MovieListDao:
    def __init__(self, db):
        self.__db = db
        
    def add_filme(self, lista_filme):
        cursor = self.__db.connection.cursor()
        
        if cursor.execute(SQL_BUSCA_FAVORITO_FILME, (lista_filme._usuario_id, lista_filme._filme_id)):
            return lista_filme
        
        cursor.execute(SQL_ADD_LIST_MOVIE, (lista_filme._usuario_id,lista_filme._filme_id))
        cursor._id = cursor.lastrowid

        self.__db.connection.commit()
        return lista_filme
    
    def listar_meus_filmes(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_MEUS_FILMES_POR_ID)
        meus_filmes = traduz_meus_filmes(cursor.fetchall())
        return meus_filmes
    
    def desfavorita_filme_all(self, id):
        self.__db.connection.cursor().execute(SQL_DESFAVORITA_FILME_ALL, (id,))
        self.__db.connection.commit()
        
    def desfavorita_filme_lista(self, usuario_id, filme_id):
        self.__db.connection.cursor().execute(SQL_REMOVE_LISTA_FILME, (usuario_id, filme_id))
        self.__db.connection.commit()
        
    def busca_filme_favorito_por_id(self, usuario_id, filme_id):
        cursor = self.__db.connection.cursor()
        if cursor.execute(SQL_BUSCA_FAVORITO_FILME, (usuario_id, filme_id)):
            tupla = cursor.fetchone()
            return MovieList(tupla[0], tupla[1])
        else:
            return None
        
    
    