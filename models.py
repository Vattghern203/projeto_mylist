class Serie:
    def __init__(self, nome, eps, temps, sinopse, nota, ano, estudio_id, genero_id, estudio, genero, id=None):
        self._id = id
        self._nome = nome
        self._eps = eps
        self._temps = temps 
        self._sinopse = sinopse
        self._nota = nota
        self._ano = ano
        self._estudio_id = estudio_id
        self._genero_id = genero_id
        self._estudio = estudio
        self._genero = genero
        

class Filme:
    def __init__(self, nome, duracao, sinopse, nota, estudio_id,  genero_id, ano, estudio, genero, id=None):
        self._nome = nome
        self._duracao = duracao
        self._sinopse = sinopse
        self._nota = nota
        self._estudio_id = estudio_id
        self._genero_id = genero_id
        self._ano = ano
        self._estudio = estudio
        self._genero = genero
        self._id = id


class Usuario:
    def __init__(self, nome, email, senha, id=None):
        self._id = id
        self._nome = nome
        self._email = email
        self._senha = senha
        

class Studio:
    def __init__(self, nome, id=None):
        self._id = id
        self._nome = nome
        
        
class Genero:
    def __init__(self, nome, id=None):
        self._id = id
        self._nome = nome
        
        
class SerieList:
    def __init__(self, usuario_id, serie_id):
        self._usuario_id = usuario_id
        self._serie_id = serie_id
        

class MovieList:
    def __init__(self, usuario_id, filme_id):
        self._usuario_id = usuario_id
        self._filme_id = filme_id
        