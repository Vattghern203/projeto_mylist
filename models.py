class Serie:
    def __init__(self, nome, eps, temps, nota, sinopse, estudio_id, genero_id, ano, id=None):
        self._id = id
        self._nome = nome
        self._eps = eps
        self._temps = temps 
        self._nota = nota
        self._sinopse = sinopse
        self._genero_id = genero_id
        self._estudio_id = estudio_id
        self._ano = ano
        

class Filme:
    def __init__(self, nome, duracao, sinopse, nota, ano, genero_id, estudio_id, id=None):
        self._nome = nome
        self._duracao = duracao
        self._sinopse = sinopse
        self._nota = nota
        self._ano = ano
        self._genero_id = genero_id
        self._estudio_id = estudio_id
        self._id = id


class Usuario:
    def __init__(self, nome, email, senha, id=None):
        self._nome = nome
        self._email = email
        self._senha = senha
        self._id = id


class Studio:
    def __init__(self, nome, id=None):
        self._id = id
        self._nome = nome
        
        
class Genero:
    def __init__(self, nome, id=None):
        self._id = id
        self._nome = nome
        