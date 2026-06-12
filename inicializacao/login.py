from inicializacao.autenticacao import *

def login():
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")

    usuario = autenticar_usuario(email, senha)

    if usuario:
        tipo_usuario = email.split("@")[1]
        
        if tipo_usuario == "prefeitura":
            print("Abrir dashboard da prefeitura")
        
        elif tipo_usuario == "empresa":
            print("Abrir dashboard da empresa")
            
        elif tipo_usuario == "cidadao":
            print("Abrir dashboard do cidadão")

        return usuario

    else:
        print("Email ou senha incorretos.")

        return None