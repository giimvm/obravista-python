from modulos.autenticacao import * 

def login():
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")

    autenticar_usuario(email, senha)
    
    if autenticar_usuario == True:
        tipo_usuario = email.split("@")[1]
        
        if tipo_usuario == "prefeitura":
            print()
        
        elif tipo_usuario == "empresa":
            print()
            
        elif tipo_usuario == "cidadao":
            print()



        

