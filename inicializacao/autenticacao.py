import json
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def carregar_usuarios():
    with open("dados/usuarios.json", "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)
    
def salvar_usuarios(usuarios):
    with open("dados/usuarios.json", "w", encoding="utf-8") as arquivo:
        json.dump(usuarios, arquivo, indent=4, ensure_ascii=False)


def autenticar_usuario(email, senha):
    usuarios = carregar_usuarios()

    for usuario in usuarios:
        if usuario["email"] == email and usuario["senha"] == senha:
            return usuario

    return None




