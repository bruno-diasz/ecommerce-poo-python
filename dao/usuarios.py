from models.usuario import Usuario
from dao.crud import CRUD
import json

class Usuarios(CRUD):

    @classmethod
    def abrir(cls):
        try:
            cls.objetos = []    
            with open("data/usuarios.json", mode="r") as arquivo:
                usuarios_json = json.load(arquivo)
                for obj in usuarios_json:
                    c = Usuario(obj["id"], obj["nome"], obj["email"], obj["fone"], obj["senha"], obj["funcao"] )
                    cls.objetos.append(c)
        except FileNotFoundError:
            pass
        
    @classmethod
    def salvar(cls):
        lista_usuarios = []
        for obj in cls.objetos:
            lista_usuarios.append(obj.to_dict())
        with open("data/usuarios.json", mode="w") as arquivo:
            json.dump(lista_usuarios , arquivo, indent=4)


