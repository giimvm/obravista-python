import json

def carregar_usuarios():
    with open("dados/usuarios.json", "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def autenticar_usuario(email, senha):
    usuarios = carregar_usuarios()
    
def cadastrar_usuario(nome, email, senha):
    print()