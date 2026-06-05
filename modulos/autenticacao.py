import json

def carregar_usuarios():
    with open("dados/usuarios.json", "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def fazer_login():
    usuarios = carregar_usuarios()