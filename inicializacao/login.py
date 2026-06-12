from inicializacao.autenticacao import *
from modulos.cidadao import *
from modulos.empresa import *
from modulos.gestor import *

def login():
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")

    usuario = autenticar_usuario(email, senha)
    tipo_usuario = email.split("@")[1]

    if usuario:
             
        if tipo_usuario == "prefeitura":
            menu_gestor(usuario)
        
        elif tipo_usuario == "empresa":
            menu_empresa(usuario)
            
        elif tipo_usuario == "cidadao":
            menu_cidadao(usuario)

        return usuario

    else:
        print("Email ou senha incorretos.")

        return None


